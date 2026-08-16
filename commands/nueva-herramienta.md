---
description: Arma a mano (con skill-creator) una skill de herramienta, con su mapeo-conceptos.md
argument-hint: <nombre-herramienta> --tipo simulador|lenguaje|diagrama-arquitectura
---

# /nueva-herramienta

Armá la skill de una herramienta (simulador, lenguaje de descripción como SystemVerilog, o plataforma de diseño sin ejecución) que vas a usar en síntesis futuras vía `--herramienta`.

## Pasos

1. Creá `skills/herramientas/herramienta-<nombre>/SKILL.md`, con un campo de metadata `tipo` explícito (`simulador` / `lenguaje` / `diagrama-arquitectura`) — este campo determina el esquema de `mapeo-conceptos.md`.
2. A diferencia de `/nueva-fuente`, esto NO se genera con `book-to-skill` — no hay libro fuente. Trabajá directamente con el usuario, preguntando:
   - Qué representa/hace cada pieza relevante de la herramienta (parámetros de un simulador, módulos de un lenguaje, bloques de un diagrama).
   - Qué convenciones sigue el usuario en su flujo de trabajo con esa herramienta.
3. Armá `mapeo-conceptos.md` con el esquema correcto según `tipo`:
   - `simulador` → columnas: concepto teórico | parámetro/control | rango de valores esperado.
   - `lenguaje` → columnas: concepto teórico | construcción de código | snippet mínimo.
   - `diagrama-arquitectura` → columnas: concepto teórico | bloque del diagrama | rol funcional.
4. Empezá con pocas filas (5-10 conceptos centrales) — este archivo se va a ir completando con el tiempo, a medida que generás síntesis y encontrás conceptos sin mapeo.
5. Correr el escaneo de seguridad si se generó contenido ejecutable de ejemplo (snippets de código).

## Notas

- Esta skill es la pieza más importante de mantener actualizada — sin ella, `mapeador-herramienta` no puede vincular teoría con práctica de forma confiable.
- Si en una síntesis futura aparece un concepto sin fila en `mapeo-conceptos.md`, `mapeador-herramienta` lo va a señalar explícitamente — volvé acá para completarlo, no lo dejes para siempre como "sin mapeo".
