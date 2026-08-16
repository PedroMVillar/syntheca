---
description: Genera un examen de prueba (parcial o final) — enunciado y resolución por separado, con contenido nuevo pero mismo formato que los reales
argument-hint: --materia <slug> --tipo parcial|final [--examen <nombre-programado>] [--temas "a,b,c"]
---

# /generar-examen-prueba

Dispará la generación de un examen de prueba completo, distinto del pipeline de `/generar-sintesis` — no produce un capítulo del libro, produce un documento de examen aparte.

## Validación de argumentos

- `--materia`, `--tipo`: obligatorios.
- Necesitás UNO de estos dos:
  - `--examen <nombre>`: busca esa entrada en `mapa-estudio.json → examenes_programados` (cargada por `/cargar-programa`) para saber qué temas cubre.
  - `--temas "tema1,tema2,..."`: lista manual, si no tenés el programa cargado con agrupación por examen.
- Si `skills/banco-ejercicios/<materia>/` no tiene material del `--tipo` pedido, avisá y preguntá si continuar con formato default o cancelar.

## Pipeline

1. **`conciliador-fuentes`** — sobre las fuentes de los temas involucrados (mismo agente que ya existe, reutilizado).
2. **`generador-examen-prueba`** — arma enunciado + resolución.
3. **`verificador-numerico`** — sobre la resolución, gate duro igual que en `/generar-sintesis`.
4. Compilar ambos `.tex` con `pdflatex` (dos pasadas cada uno) y confirmar 0 errores.

## Al aprobar

1. Guardá ambos archivos en `examenes-prueba/<materia>/<slug>-enunciado.{tex,pdf}` y `.../<slug>-resolucion.{tex,pdf}`.
2. Copiá también el script de verificación numérica como archivo entregable aparte.
3. Presentá al usuario **primero el enunciado únicamente** — no adjuntes la resolución en el mismo mensaje sin que la pida, para no arruinar el valor de rendirlo como simulacro real.

## Notas

Este comando es independiente de `/generar-sintesis` — no agrega un capítulo al libro de la materia, ni actualiza `conceptos_ya_cubiertos` de la misma forma (un examen de prueba no es "contenido nuevo aprendido", es práctica sobre contenido ya sintetizado).
