---
description: Ingesta TPs, parciales y/o finales reales a skills/banco-ejercicios/<materia>/, extrayendo patrón de forma
argument-hint: <ruta-a-archivos> <materia> --tipo tp|parcial|final
---

# /nuevo-banco-ejercicios

Ingestá tus TPs, parciales o finales reales de una materia, para que `estilista-ejercicios` pueda calibrar el formato de los ejercicios generados contra lo que realmente te toman.

## Pasos

1. Los archivos van a `skills/banco-ejercicios/<materia>/tps/`, `.../parciales/` o `.../finales/` según `--tipo`.
2. A diferencia de `/nueva-fuente`, lo que importa extraer acá NO es contenido teórico — es **patrón de forma**: estructura de enunciado (dato→pedido, multi-inciso), longitud habitual, convenciones de notación de esa cátedra específica.
3. Podés usar `book-to-skill` en modo liviano para la extracción de texto bruto, pero la síntesis que va en `skills/banco-ejercicios/<materia>/SKILL.md` tiene que enfocarse en:
   - Patrón de enunciado típico.
   - Curva de dificultad TP → parcial → final (los TPs suelen ser guiados y de una sola familia; los parciales combinan 2-3 familias con menos andamiaje; los finales suelen ser aún más integradores, mezclando familias de varias unidades del programa completo).
   - Si hay parciales o finales CON solución: guardalos como ejemplos de referencia de formato de resolución esperado por esa cátedra — nunca como contenido a copiar literal.
4. Actualizá (o creá) `skills/banco-ejercicios/<materia>/SKILL.md` con este patrón extraído, distinguiendo los 3 niveles si hay material de los 3.

## Reglas duras

- Nunca extraigas el contenido específico de los problemas como si fuera reutilizable literal — eso es trabajo de `estilista-ejercicios` en el momento de generar, y siempre parafraseado con datos nuevos, nunca copia directa.
- Procesá cada `--tipo` por separado (no subas TPs y parciales en la misma pasada) para no mezclar sus patrones de dificultad.

## Notas

- Esta capa es opcional — si nunca la usás para una materia, `/generar-sintesis` simplemente no acepta `--estilo` para esa materia y usa el formato default de la plantilla.
- Los finales, al integrar varias unidades, son la referencia más útil para calibrar el paso 6.b (intercalado) cuando el tema de la síntesis ya está avanzado en el programa.
