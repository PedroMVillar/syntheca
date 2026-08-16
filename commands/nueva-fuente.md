---
description: Ingesta un libro o paper nuevo a skills/fuentes/, vía book-to-skill
argument-hint: <ruta-al-pdf-o-archivo> [materia]
---

# /nueva-fuente

Ingestá una fuente teórica nueva (libro o paper) a `skills/fuentes/`, para que quede disponible para futuras síntesis vía `/generar-sintesis --fuentes`.

## Pasos

1. Si el archivo no está ya en `_inbox/`, decile al usuario que lo coloque ahí (o aceptá una ruta absoluta directa si la da).
2. Invocá la skill `book-to-skill` (Modo 1, Full Conversion) sobre el archivo:
   - Preguntá el tipo de contenido (Technical vs. Text-heavy) — para libros/papers con fórmulas, tablas o notación técnica, siempre `Technical`.
   - Skill destino: `skills/fuentes/<slug>/`, donde `<slug>` sigue el patrón `libro-<autor-tema>` o `paper-<autor-año>`.
   - Presentá la estimación de costo/tiempo (Step 2.5 de book-to-skill) antes de generar, y esperá confirmación.
3. Una vez generada la skill, corré el escaneo de seguridad obligatorio (`scan_generated_skill.py`) antes de dar por terminada la ingesta.
4. Si se pasó `[materia]` como segundo argumento, registrá esa asociación (no hace falta un campo especial en la skill — simplemente usá ese slug al momento de pasar `--fuentes` en síntesis de esa materia).
5. Archivá o eliminá el archivo de `_inbox/` una vez completada la ingesta exitosa.
6. Confirmá al usuario: nombre de la skill creada, cuántos capítulos, tokens aproximados del `SKILL.md`.

## Notas

- Cada fuente es una skill separada — NUNCA fusiones automáticamente con otra fuente existente. Solo `pedagogia-cognitiva` se fusiona entre sí (vía Update/Fold-in), porque es la única capa "universal". Las fuentes de dominio se mantienen independientes para poder conciliarlas explícitamente después.
- Si el usuario pide actualizar una fuente ya existente con más material del mismo libro/autor, ahí sí corresponde Modo 4 (Update/Fold-in) sobre esa misma skill puntual.
