---
description: Genera una síntesis teórica completa, disparando el pipeline completo de agentes
argument-hint: "<tema>" --materia <slug> --fuentes <a,b,c> [--herramienta <nombre>] [--estilo <materia>] [--fuente-principal <slug>]
---

# /generar-sintesis

Este es el comando central del plugin. Dispara el pipeline completo de subagentes para producir una síntesis teórica personalizada.

## Validación de argumentos

- `<tema>`: obligatorio, string libre.
- `--materia`: obligatorio — namespace para `mapa-estudio.json`, evita que el interleaving cruce conceptos de materias distintas.
- `--fuentes`: obligatorio — al menos un slug de `skills/fuentes/`. Si alguno no existe, avisá y sugerí `/nueva-fuente` antes de continuar.
- `--herramienta`: opcional — slug de `skills/herramientas/`. Si no existe, avisá y sugerí `/nueva-herramienta`.
- `--estilo`: opcional — nombre de materia en `skills/banco-ejercicios/`. Si no existe, avisá y sugerí `/nuevo-banco-ejercicios`, o continuá sin estilo si el usuario prefiere.
- `--fuente-principal`: opcional — debe ser uno de los slugs pasados en `--fuentes`.

## Pipeline (invocar los agentes EN ESTE ORDEN, cada uno recibe el output del anterior)

1. **`conciliador-fuentes`** — siempre. Lee todas las fuentes de `--fuentes`, produce contenido conciliado con atribución.
2. **`calibrador-perfil`** — siempre. Lee `skills/perfil-academico/`, produce ficha de calibración para este tema/familia específico.
3. **`mapeador-herramienta`** — CONDICIONAL, solo si vino `--herramienta`. Produce tabla concepto→elemento.
4. **`estilista-ejercicios`** — CONDICIONAL, solo si vino `--estilo`. Produce ejercicios 6.a/6.b calibrados + referencia de formato para el ejemplo resuelto.
5. **`redactor-pedagogico`** — siempre. Combina todo lo anterior siguiendo `skills/plantilla-sintesis/` y aplicando `skills/pedagogia-cognitiva/`.
6. **`verificador-numerico`** — CONDICIONAL, solo si el documento generado tiene ejercicios con resultado calculable. Verifica independientemente, produce reporte + script(s) entregables.
7. **`critico-calidad`** — siempre, GATE DURO. Si falla cualquier chequeo (mecánico o numérico), vuelve al paso 5 con feedback puntual — repetir hasta aprobar, nunca entregar un borrador sin aprobar.

## Al aprobar

1. Guardá el documento final como un `\chapter` dentro de `sintesis/<materia>/<materia>.tex` (un archivo LaTeX por materia, acumulando capítulos — ver `skills/plantilla-sintesis/latex/`). Si es la primera síntesis de esa materia, copiá `plantilla-syntheca.tex` + `plantilla-syntheca-preamble.tex` como base y agregá el capítulo antes de `\end{document}`; si ya existe, insertá el nuevo `\chapter` antes del `\end{document}` existente.
2. Compilá con `pdflatex` (dos pasadas, para resolver referencias de TOC e índices) y verificá que no haya errores antes de dar por terminado — no entregues un `.tex` que no compila.
3. Si hubo `verificador-numerico`, copiá también el/los script(s) de verificación como archivos entregables aparte.
4. Corré `scripts/update_mapa_estudio.py` para registrar el nuevo tema, familia(s), dificultad inicial y fecha en `mapa-estudio.json`.
5. Presentá el PDF final (y opcionalmente el `.tex`) al usuario.

## Notas

- Nunca saltees `critico-calidad` "para ir más rápido" — es el punto de la arquitectura que garantiza que nada llegue sin verificar.
- Si el usuario interrumpe el pipeline a mitad de camino, no guardes un output parcial en `sintesis/` — solo el output final aprobado se persiste ahí.
