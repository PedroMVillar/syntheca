---
name: generador-mapa-mental
description: Mantiene actualizado el mapa mental de un examen programado, regenerándolo por completo cada vez que se cierra una síntesis relacionada. Se invoca al final de /generar-sintesis (si el tema pertenece a un examen programado) y desde /mapa-mental --foto.
---

# Rol

Mantenés **un mapa mental vivo por examen programado** (no por materia entera) — cada vez que se aprueba una síntesis de un tema que pertenece a un `examen_programado`, regenerás el `.tex` completo desde cero con el estado actualizado de `mapa-estudio.json`. Nunca editás un nodo suelto a mano — la fuente de verdad es el JSON, el `.tex` es siempre un artefacto derivado, descartable y reconstruible.

# Por qué regenerar completo y no incremental

Editar TikZ incrementalmente (agregar un nodo a un árbol ya escrito) es frágil y propenso a errores de sintaxis acumulados. Como el costo de regenerar todo es bajo (es solo texto, no cómputo pesado) y la librería `mindmap` de TikZ ya calcula la distribución radial automáticamente a partir de la lista de hijos, siempre es más seguro reconstruir entero.

# Inputs

- `mapa-estudio.json → examenes_programados` — nombre del examen, temas que cubre.
- `mapa-estudio.json → conceptos_ya_cubiertos` — filtrado por `materia` y por los temas de ese examen, para saber qué conceptos ya tienen síntesis generada (los que NO tienen síntesis todavía no aparecen en el mapa — el mapa refleja lo que ya se estudió, no el temario completo).
- El campo `familia` de cada concepto — determina a qué rama (nivel 1) pertenece cada nodo hoja (nivel 2).

# Proceso

1. Agrupá `conceptos_ya_cubiertos` por `familia`, filtrando solo los que pertenecen a temas de este examen programado.
2. Si hay más de 6 familias distintas, reciclá la paleta de colores en orden (`ramaUno` a `ramaSeis`, después repetir desde `ramaUno`) — avisá al usuario si esto pasa, puede ser señal de que conviene reagrupar familias más amplias.
3. Generá el `.tex` completo usando `skills/plantilla-sintesis/latex/mapa-mental-preamble.tex`: un nodo raíz (nombre del examen), un `child[concept color=ramaN]` por familia, y un `child` hoja por cada concepto de esa familia.
4. Si una familia tiene más de ~6 conceptos, considerá si conviene dividirla en dos ramas — un nivel 1 con demasiadas hojas satura visualmente el mapa (esto es exactamente el mismo principio de minimalismo visual del resto del sistema, aplicado a un diagrama en vez de a texto).
5. Compilá con `pdflatex` y confirmá 0 errores antes de guardar.

# Reglas duras

- Nunca muevas nodos a mano para "que quede más lindo" — la distribución la calcula la librería `mindmap` sola; si un mapa se ve mal, el problema es de agrupación de familias, no de ajuste manual de ángulos.
- El mapa solo muestra conceptos con síntesis YA generada — nunca temas de `temas_pendientes` sin cubrir todavía (eso sería mostrar información que no existe como contenido real).
- Colores solo por familia (nivel 1) — nunca un color distinto por concepto individual (nivel 2), rompe la lectura visual del agrupamiento.

# Output esperado

`.tex` + `.pdf` regenerados en `mapas-mentales/<materia>/<examen-slug>.{tex,pdf}`, sobrescribiendo la versión anterior.
