#!/usr/bin/env python3
"""
update_mapa_estudio.py — actualiza mapa-estudio.json tras aprobar una síntesis.

Invocado únicamente por el agente critico-calidad al aprobar un documento.
Nunca se corre a mano salvo corrección manual deliberada del estado.

Uso:
  python3 update_mapa_estudio.py \
    --tema "Decodificadores convolucionales" \
    --materia comunicaciones-digitales \
    --fuentes libro-fec-lin-costello,paper-viterbi-1967 \
    --herramienta systemverilog \
    --conceptos '[{"concepto":"algoritmo de viterbi","familia":"decodificacion de secuencias","dificultad":"basica"}]' \
    --perfil-version 2026-08-04
"""

import argparse
import json
import os
import sys
from datetime import date


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "mapa-estudio.json")


def load_state(path: str) -> dict:
    if not os.path.exists(path):
        return {
            "sintesis_generadas": [],
            "temas_pendientes": [],
            "secuencia_sugerida": [],
            "conceptos_ya_cubiertos": [],
            "version_perfil_usada": None,
        }
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(path: str, state: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def upsert_concepto(state: dict, concepto: str, familia: str, materia: str, dificultad: str):
    for entry in state["conceptos_ya_cubiertos"]:
        if entry["concepto"] == concepto and entry["materia"] == materia:
            entry["ultima_dificultad"] = dificultad
            entry["veces_reaparecido"] = entry.get("veces_reaparecido", 0) + 1
            entry["familia"] = familia
            return
    state["conceptos_ya_cubiertos"].append(
        {
            "concepto": concepto,
            "materia": materia,
            "familia": familia,
            "ultima_dificultad": dificultad,
            "veces_reaparecido": 0,
        }
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tema", required=False)
    parser.add_argument("--materia", required=True)
    parser.add_argument("--fuentes", required=False, default="", help="lista separada por comas")
    parser.add_argument("--herramienta", default=None)
    parser.add_argument("--conceptos", default="[]", help="JSON list de conceptos cubiertos")
    parser.add_argument("--perfil-version", default=None)
    parser.add_argument("--path", default=DEFAULT_PATH)
    parser.add_argument(
        "--seed-temas-pendientes",
        default=None,
        help="JSON list de strings — carga inicial de temas_pendientes desde el programa de la materia, sin registrar síntesis",
    )
    args = parser.parse_args()

    state = load_state(args.path)

    if args.seed_temas_pendientes:
        try:
            nuevos_temas = json.loads(args.seed_temas_pendientes)
            existentes = set(state.get("temas_pendientes", []))
            for t in nuevos_temas:
                if t not in existentes:
                    state.setdefault("temas_pendientes", []).append(t)
            save_state(args.path, state)
            print(f"✅ {len(nuevos_temas)} tema(s) del programa cargados en temas_pendientes.")
        except json.JSONDecodeError:
            print("⚠️  --seed-temas-pendientes no es JSON válido.", file=sys.stderr)
        return

    if not args.tema:
        print("⚠️  --tema es obligatorio salvo que uses --seed-temas-pendientes.", file=sys.stderr)
        sys.exit(1)

    state["sintesis_generadas"].append(
        {
            "tema": args.tema,
            "materia": args.materia,
            "fecha": date.today().isoformat(),
            "fuentes": [f.strip() for f in args.fuentes.split(",") if f.strip()],
            "herramienta": args.herramienta,
            "estado": "aprobado",
        }
    )

    try:
        conceptos = json.loads(args.conceptos)
    except json.JSONDecodeError:
        print("⚠️  --conceptos no es JSON válido, se omite esa actualización.", file=sys.stderr)
        conceptos = []

    for c in conceptos:
        upsert_concepto(
            state,
            concepto=c["concepto"],
            familia=c.get("familia", "sin-clasificar"),
            materia=args.materia,
            dificultad=c.get("dificultad", "basica"),
        )

    if args.tema in state.get("temas_pendientes", []):
        state["temas_pendientes"].remove(args.tema)

    if args.perfil_version:
        state["version_perfil_usada"] = args.perfil_version

    save_state(args.path, state)
    print(f"✅ mapa-estudio.json actualizado: '{args.tema}' ({args.materia}) registrado como aprobado.")


if __name__ == "__main__":
    main()
