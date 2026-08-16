---
description: Re-corre solo critico-calidad sobre una síntesis ya generada (útil tras editarla a mano)
argument-hint: <ruta-al-archivo-de-sintesis>
---

# /revisar-sintesis

Volvé a pasar el gate de calidad sobre una síntesis existente, sin correr todo el pipeline de nuevo — útil si editaste el documento a mano después de generarlo.

## Pasos

1. Leé el archivo indicado.
2. Invocá directamente `critico-calidad` (saltando los pasos 1-6 de `/generar-sintesis`) sobre el contenido actual del archivo.
3. Si el archivo tiene ejercicios con resultado calculable que fueron editados a mano, invocá también `verificador-numerico` antes de `critico-calidad`, para no perder esa verificación en la edición manual.
4. Si `critico-calidad` rechaza: mostrá el feedback puntual al usuario (no invoques automáticamente a `redactor-pedagogico` para corregir — la edición manual implica que el usuario probablemente quiere decidir él mismo cómo ajustar).
5. Si aprueba: confirmá y, si corresponde, actualizá `mapa-estudio.json` con la fecha de revisión.

## Notas

Este comando es más liviano que `/generar-sintesis` a propósito — no vuelve a conciliar fuentes ni a calibrar perfil, solo valida el documento tal como está ahora.
