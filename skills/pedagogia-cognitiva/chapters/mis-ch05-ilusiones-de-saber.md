# Capítulo 5 (Make It Stick): Evitá las ilusiones de saber

## Core Idea
La sensación subjetiva de "ya lo sé" es un juicio metacognitivo que se puede engañar fácilmente — la relectura fluida genera esa sensación sin que corresponda a retención real recuperable. La única forma confiable de calibrar lo que realmente se sabe es la autoevaluación activa bajo condiciones parecidas a las reales.

## Frameworks Introducidos
- **Ilusión de saber (illusion of knowing)**: la sensación de dominio generada por familiaridad/fluidez de procesamiento, que no se corresponde con la capacidad real de recuperar o aplicar ese conocimiento cuando hace falta.
  - Cuándo aplica: cualquier situación de autoevaluación — la sensación subjetiva de "lo tengo claro" no es un dato confiable por sí sola.
  - Cómo: reemplazar el juicio subjetivo por autoevaluación activa (testing) bajo condiciones que se parezcan a la aplicación real.
- **Simulación como calibración**: entrenar y evaluar bajo condiciones que se acerquen a las reales (no condiciones "de práctica" artificialmente fáciles) es lo único que calibra con precisión qué tan preparado se está de verdad.

## Conceptos Clave
- **Fluidez de procesamiento**: la facilidad con la que algo se procesa (ej. al releerlo) — no correlaciona con retención recuperable, aunque el cerebro la use como atajo para juzgar dominio.
- **Calibración**: el ajuste entre lo que el lector cree saber y lo que realmente puede recuperar/aplicar — se logra con testing bajo condiciones realistas, no con re-lectura.
- **Feedback de campo vs. feedback de práctica**: a veces el feedback más potente (y más caro) llega de errores reales en el momento de aplicar, no de la práctica — reforzando por qué calibrar antes, con simulación, es preferible.

## Modelos Mentales
- La sensación de "esto ya lo entendí" durante la lectura es del mismo tipo de señal que "esta comida huele bien" — un atajo útil pero falible, no una medición.
- Cuanto más se parezca la condición de autoevaluación a la condición real de uso, más confiable es la calibración resultante.

## Anti-patrones
- **Confiar en la sensación subjetiva de dominio sin testear**: es exactamente el mecanismo que genera sorpresas negativas en la evaluación real.
- **Practicar en condiciones artificialmente fáciles**: genera una calibración falsa — el lector se siente preparado para condiciones que no se van a repetir en la aplicación real.

## Key Takeaways
1. La sensación subjetiva de "ya lo sé" no es un dato confiable — se puede generar por pura fluidez de procesamiento sin retención real.
2. La única calibración confiable viene de testear activamente, en condiciones parecidas a las de aplicación real, no de releer o "sentir" que se entendió.
3. Esto es la justificación directa de por qué el `verificador-numerico` (sección 5.1 de la arquitectura) no puede ser opcional quand hay ejercicios con resultado calculable — la autoevaluación subjetiva del propio texto generado también puede caer en esta misma ilusión.

## Connects To
- **HLW Ch7 (ilusión de competencia)**: mismo fenómeno, confirmado desde una segunda fuente — refuerza que no es una idea aislada sino un hallazgo replicado.
- **5.1 (verificación numérica) del documento de arquitectura**: la calibración por testing activo bajo condiciones reales es exactamente el principio detrás de entregarle al usuario una herramienta de auto-chequeo, no solo un chequeo interno oculto.
