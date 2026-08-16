#!/usr/bin/env python3
"""
rubric_check.py — valida estructura mecánica de una síntesis generada por syntheca.

No reemplaza la revisión cualitativa de critico-calidad — solo chequea cosas
objetivas y automatizables: presencia de secciones, posición de micro-chequeos,
orden de sub-fases de ejercicios, y longitud de citas literales.

Uso: python3 rubric_check.py <ruta-al-archivo-de-sintesis>
Exit code 0 = pasa todos los chequeos mecánicos. Exit code 1 = falló al menos uno.
Si el archivo no parece ser una síntesis de syntheca (no está bajo sintesis/),
sale silenciosamente con 0 para no interferir con otros Write del usuario.
"""

import sys
import re
import os


REQUIRED_SECTIONS = [
    r"#+\s*1\.\s*Motivaci[oó]n",
    r"#+\s*2\.\s*Mapa de fuentes",
    r"#+\s*3\.\s*Marco te[oó]rico",
    r"#+\s*4\.\s*Ejemplo resuelto",
    r"#+\s*5\.\s*Errores comunes",
    r"#+\s*6\.\s*Ejercicios",
]

CONDITIONAL_SECTIONS = [
    r"#+\s*7\.\s*Traducci[oó]n a la herramienta",
    r"#+\s*8\.\s*Ejercicio guiado",
]

MAX_QUOTE_WORDS = 60  # umbral aproximado de alerta para posible copia literal extensa


def is_synthesis_file(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return "/sintesis/" in normalized or normalized.startswith("sintesis/")


def check_sections(text: str) -> list[str]:
    errors = []
    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Falta sección núcleo obligatoria: {pattern}")
    return errors


def check_conditional_sections(text: str) -> list[str]:
    """Si hay UNA sección condicional, debe haber las dos (7 y 8 van juntas)."""
    errors = []
    found = [bool(re.search(p, text, re.IGNORECASE)) for p in CONDITIONAL_SECTIONS]
    if any(found) and not all(found):
        errors.append(
            "Se encontró solo una de las secciones condicionales (7/8) — "
            "si hay herramienta, deben estar ambas."
        )
    return errors


def check_blocked_before_interleaved(text: str) -> list[str]:
    errors = []
    m_a = re.search(r"6\.a|6a\b", text, re.IGNORECASE)
    m_b = re.search(r"6\.b|6b\b", text, re.IGNORECASE)
    if m_a and m_b and m_a.start() > m_b.start():
        errors.append(
            "La sub-fase 6.a (práctica en bloque) aparece DESPUÉS de 6.b "
            "(intercalada) — el orden debe ser bloque primero."
        )
    elif m_b and not m_a:
        errors.append(
            "Se encontró práctica intercalada (6.b) sin práctica en bloque previa (6.a)."
        )
    return errors


def check_mapa_de_fuentes(text: str, fuentes_esperadas: list[str]) -> list[str]:
    errors = []
    if not fuentes_esperadas:
        return errors
    section_match = re.search(
        r"2\.\s*Mapa de fuentes(.*?)(?=\n#+\s*3\.)", text, re.IGNORECASE | re.DOTALL
    )
    section_text = section_match.group(1) if section_match else ""
    for fuente in fuentes_esperadas:
        if fuente not in section_text and fuente not in text:
            errors.append(f"La fuente '{fuente}' no se menciona explícitamente en el documento.")
    return errors


def check_long_verbatim_risk(text: str) -> list[str]:
    """Heurística simple: bloques de comillas largas o citas extensas sin cortar."""
    errors = []
    for match in re.finditer(r"[\"“]([^\"”]{200,})[\"”]", text):
        word_count = len(match.group(1).split())
        if word_count > MAX_QUOTE_WORDS:
            errors.append(
                f"Posible cita literal extensa detectada (~{word_count} palabras) — "
                "revisar que esté parafraseada, no copiada."
            )
    return errors


def main():
    if len(sys.argv) < 2:
        print("Uso: rubric_check.py <ruta-al-archivo>", file=sys.stderr)
        sys.exit(0)  # no bloquear si se invoca mal, solo avisar

    path = sys.argv[1]

    if not is_synthesis_file(path):
        # No es un archivo de síntesis de syntheca — no interferir.
        sys.exit(0)

    if not os.path.exists(path):
        sys.exit(0)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    fuentes_env = os.environ.get("APUNTE_FORGE_FUENTES", "")
    fuentes_esperadas = [f.strip() for f in fuentes_env.split(",") if f.strip()]

    all_errors = []
    all_errors += check_sections(text)
    all_errors += check_conditional_sections(text)
    all_errors += check_blocked_before_interleaved(text)
    all_errors += check_mapa_de_fuentes(text, fuentes_esperadas)
    all_errors += check_long_verbatim_risk(text)

    if all_errors:
        print(f"⚠️  rubric_check.py encontró {len(all_errors)} problema(s) en {path}:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print(f"✅ rubric_check.py: {path} pasa todos los chequeos mecánicos.")
    sys.exit(0)


if __name__ == "__main__":
    main()
