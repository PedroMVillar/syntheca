# Contribuir a syntheca

Gracias por el interés. Este proyecto está en desarrollo activo — hay bastante espacio para mejorarlo.

## Formas de contribuir

### 1. Nuevas fuentes para `pedagogia-cognitiva`
Si conocés investigación sólida de ciencia cognitiva/neurociencia del aprendizaje que no esté cubierta todavía (ver [Roadmap](../README.md#-roadmap)), abrí un issue proponiéndola antes de procesarla — así evitamos duplicar esfuerzo. El proceso de fusión usa la skill `book-to-skill` en modo Update/Fold-in sobre `skills/pedagogia-cognitiva/`.

### 2. Mejoras a los agentes o comandos
Cada agente en `agents/*.md` y comando en `commands/*.md` tiene rol, inputs, proceso y reglas duras documentadas explícitamente. Si proponés un cambio de comportamiento, actualizá también `docs/ARCHITECTURE.md` en la sección correspondiente — el documento de arquitectura y los archivos ejecutables deberían mantenerse sincronizados.

### 3. Plantilla LaTeX
Mejoras a `skills/plantilla-sintesis/latex/` son bienvenidas — nuevos entornos, soporte para otras clases de documento, ajustes de estilo. Mantené el criterio de minimalismo visual ya establecido (sin decoración que no cumpla función semántica) al proponer cambios.

### 4. Reportar problemas de uso real
Si usaste el plugin y algo no funcionó como se documenta (por ejemplo, algún paso del pipeline que no hace lo que su `.md` dice), abrí un issue con el caso concreto — son los más valiosos para encontrar huecos de diseño.

## Antes de un PR

- Si tocás un agente/comando, verificá que el frontmatter YAML siga siendo válido.
- Si tocás los scripts en `scripts/`, corré `python3 scripts/rubric_check.py <archivo-de-prueba>` para confirmar que no rompiste el comportamiento.
- Si tocás la plantilla LaTeX, compilá `skills/plantilla-sintesis/latex/plantilla-ejemplo.tex` con `pdflatex` (dos pasadas) y confirmá que no hay errores antes de proponer el cambio.
- No commitees nunca contenido derivado de libros con copyright que no sea tuyo — ver la nota en [`LICENSE`](../LICENSE) sobre `skills/pedagogia-cognitiva/`.

## Filosofía del proyecto

Cualquier regla nueva que se agregue a `pedagogia-cognitiva` debería estar atribuida a una fuente real, no ser una intuición sin respaldo — es lo que diferencia a este proyecto de "otro generador de apuntes con buenas intenciones". Si proponés una regla de diseño instruccional nueva, traé la fuente.
