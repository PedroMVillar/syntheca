---
description: Carga el cronograma/programa de una materia a mapa-estudio.json — temas_pendientes y, si el programa lo especifica, qué temas entran en cada parcial/final
argument-hint: <materia> (pegá o adjuntá el cronograma en el mismo mensaje)
---

# /cargar-programa

Convertí el cronograma/temario de una materia en `temas_pendientes` (y, si el programa lo indica, en `examenes_programados`) dentro de `mapa-estudio.json` — sin generar ninguna síntesis todavía.

## Pasos

1. Leé el cronograma que te pasó el usuario (pegado en el mensaje o como archivo adjunto).
2. Extraé la lista de temas/clases como strings concisos — un tema por clase o por bloque temático, no por línea literal del PDF. Sintetizá el título (ej. "Cinemática 1D (MRU, MRUV, caída libre, tiro vertical)"), no copies el texto crudo del cronograma completo.
3. Si el cronograma indica explícitamente qué temas/guías entran en cada parcial o final (buscá frases tipo "Parcial I: Guías 1-3", fechas de examen), armá también la lista de `examenes_programados`, con nombre, fecha (si está) y la sublista de temas correspondiente.
4. Confirmá con el usuario la lista extraída ANTES de escribir nada — mostrala en el chat, no la apliques a ciegas.
5. Una vez confirmada, corré:
```bash
   python3 scripts/update_mapa_estudio.py --materia <slug> \
     --seed-temas-pendientes '[...]' \
     --seed-examenes-programados '[...]'
```
   (el segundo flag es opcional — solo si el programa especificaba la agrupación por examen).
6. Confirmá al usuario cuántos temas y cuántos exámenes quedaron cargados.

## Reglas duras

- Nunca sobrescribas `temas_pendientes` existentes — el script solo agrega los que no estén ya (ver `upsert`), nunca duplica ni pisa lo que ya había.
- Si el cronograma es ambiguo sobre qué temas entran en qué examen, no inventes la agrupación — dejá `examenes_programados` vacío para esos casos y avisá al usuario.

## Notas

Este comando reemplaza el flujo manual que existía antes (correr el script a mano). El script sigue aceptando los mismos flags si en algún momento preferís correrlo directo.
