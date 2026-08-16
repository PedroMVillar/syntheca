---
description: Muestra o congela el mapa mental de un examen programado
argument-hint: <examen> [--foto]
---

# /mapa-mental

Sin `--foto`, simplemente confirma que el mapa vivo de ese examen está actualizado (lo regenera si hace falta). Con `--foto`, congela una copia con fecha, para repaso final de últimos días sin que se siga modificando.

## Pasos

1. Buscá `<examen>` en `mapa-estudio.json → examenes_programados`.
2. Si no existe, avisá y sugerí `/cargar-programa` primero.
3. Sin `--foto`: invocá `generador-mapa-mental` normal, sobre `mapas-mentales/<materia>/<examen-slug>.pdf`.
4. Con `--foto`: invocá `generador-mapa-mental`, pero guardá el resultado como `mapas-mentales/<materia>/<examen-slug>-foto-<fecha>.pdf` — sin tocar ni sobrescribir el mapa vivo.

## Notas

El mapa vivo se actualiza solo, automáticamente, cada vez que `/generar-sintesis` cierra un tema de ese examen — no hace falta correr este comando para que crezca. Se usa para: (a) consultarlo cuando quieras verlo aunque no cambió nada, o (b) sacar la "foto" congelada de repaso final.
