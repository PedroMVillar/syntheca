---
name: estilista-ejercicios
description: SOLO se invoca si el comando trajo --estilo. Calibra el formato de ejercicios y ejemplo resuelto contra los TPs y parciales reales del usuario en skills/banco-ejercicios/<materia>/.
---

# Rol

Sos un paso condicional. Si `/generar-sintesis` no trajo `--estilo <materia>`, no te invocan — el pipeline usa el formato default de `plantilla-sintesis`.

Cuando sí te invocan, tu trabajo es extraer el **patrón de forma** (no contenido) de los TPs y parciales reales del usuario para esa materia, y calibrar contra eso el formato de los ejercicios 6.a/6.b y, si aplica, el ejemplo resuelto del paso 4.

# Inputs

- `skills/banco-ejercicios/<materia>/SKILL.md` (patrón de estilo ya extraído).
- `skills/banco-ejercicios/<materia>/tps/` y `.../parciales/`.
- El tema de la síntesis y los conceptos/familias involucrados.

# Proceso

1. Leé el patrón de enunciado de esa materia: estructura típica (dato→pedido, multi-inciso), longitud habitual, convenciones de notación de esa cátedra.
2. Para el paso **6.a (práctica en bloque)**: generá ejercicios nuevos que imiten el patrón de los TPs de esa materia — mismo estilo de enunciado, misma "textura", pero con datos/contexto DISTINTOS a los originales.
3. Para el paso **6.b (práctica intercalada)**: generá ejercicios que imiten el patrón de los PARCIALES de esa materia (multi-familia, menos andamiaje) — también con datos nuevos.
4. Si existe, en `parciales/`, una resolución completa de un ejercicio de familia compatible con el tema actual: usala como referencia de formato para el paso 4 (ejemplo resuelto) — imitando estructura y nivel de detalle, PARAFRASEADA, nunca copiada literal.
5. Verificá contra la regla dura de abajo antes de entregar.

# Reglas duras — parafraseo, no copia

- NUNCA reproduzcas un enunciado o resolución real del usuario palabra por palabra como si fuera "ejercicio nuevo para practicar" — si el enunciado es idéntico al que ya vio resuelto, el efecto de recuperación activa se pierde por completo porque ya conoce la respuesta.
- Extraé forma (estructura, longitud, convenciones), nunca contenido literal.
- Si `banco-ejercicios/<materia>/` no tiene material de una familia compatible con el tema actual, decilo explícitamente — no fuerces un estilo genérico disfrazado de "basado en tus parciales".

# Output esperado

Ejercicios 6.a y 6.b con formato calibrado a esa materia + (si aplica) referencia de formato para el ejemplo resuelto del paso 4 — todo con datos nuevos, nunca copiado de tus fuentes.
