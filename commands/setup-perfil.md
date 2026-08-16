---
description: Crea o edita skills/perfil-academico/SKILL.md, la ficha de perfil de 4 dimensiones
argument-hint: [--edit para editar campos existentes]
---

# /setup-perfil

Creá o editá tu perfil académico — la skill que calibra CADA síntesis futura. Se corre una vez al principio, y se vuelve a correr cuando cambie algo relevante de tu formación.

## Pasos

1. Si `skills/perfil-academico/SKILL.md` no existe todavía, copialo desde `skills/perfil-academico/SKILL.md.template` (el template versionado en el repo) y completalo con el usuario — este archivo con datos reales NUNCA se commitea (está en `.gitignore` a propósito, son tus datos personales).
2. Si ya existe y se pasó `--edit`, mostrá los campos actuales y preguntá cuáles actualizar — no reescribas todo desde cero, solo los campos que cambian.
3. Recordá al usuario que los campos 11-12 (Dimensión 4: andamiaje e interleaving) y el nivel de expertise en general **no son un valor único global** — se completan por tema/familia específico. El template deja espacio para múltiples entradas por dominio, no un solo campo.
4. Al guardar, actualizá `version_perfil_usada` implícitamente: la próxima vez que `calibrador-perfil` corra, va a comparar la fecha de esta edición contra la de `mapa-estudio.json` para detectar síntesis desactualizadas.
5. Preguntá si el usuario quiere que se marquen como "a revisar" las síntesis ya generadas de temas donde el perfil cambió significativamente.

## Notas

- Este comando no genera contenido teórico — solo estructura el perfil que después van a consultar `calibrador-perfil` y `redactor-pedagogico`.
- Sé exhaustivo pero no fuerces respuesta a los 12 campos de una — si el usuario no tiene clara alguna dimensión todavía (ej. Dimensión 3, mapa de obstáculos), dejala como pendiente explícitamente en vez de inventar una respuesta genérica.
