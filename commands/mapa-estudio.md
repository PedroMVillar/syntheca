---
description: Muestra el estado global de mapa-estudio.json (temas generados, pendientes, conceptos cubiertos)
argument-hint: "[materia opcional para filtrar]"
---

# /mapa-estudio

Mostrale al usuario un resumen legible del estado de `mapa-estudio.json` — qué se generó, qué falta, qué conceptos ya están cubiertos por familia y materia.

## Pasos

1. Leé `mapa-estudio.json`.
2. Si se pasó un argumento de materia, filtrá todo por esa materia — no mezcles el resumen de distintas materias salvo que el usuario pida explícitamente una vista global.
3. Presentá:
   - Síntesis generadas (tema, fecha, fuentes usadas, estado).
   - Temas pendientes.
   - Conceptos ya cubiertos, agrupados por familia, con su última dificultad y cuántas veces reapareció.
   - Si `version_perfil_usada` es más vieja que la fecha actual de `skills/perfil-academico/SKILL.md`, avisá explícitamente que puede haber síntesis desactualizadas en calibración.
4. Si el usuario lo pide, sugerí una secuencia razonable de próximos temas basada en `temas_pendientes` y el criterio de interleaving (temas de la misma familia que todavía no se intercalaron entre sí).

## Notas

Este comando es de solo lectura para consultar — nunca modifica `mapa-estudio.json` directamente vos mismo. Las modificaciones normales las hace `scripts/update_mapa_estudio.py`, invocado por `critico-calidad` al aprobar una síntesis.

**Excepción — carga inicial desde el programa de la materia**: si el usuario te pasa el programa/temario de una materia nueva, podés poblar `temas_pendientes` de una sola vez con:
```
python3 scripts/update_mapa_estudio.py --materia <slug> --seed-temas-pendientes '["Tema 1", "Tema 2", ...]'
```
Esto no registra ninguna síntesis como generada — solo deja la lista de temas pendientes lista para que `/generar-sintesis` y `/mapa-estudio` la usen como referencia de secuenciación.
