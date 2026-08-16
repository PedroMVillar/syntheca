# CLT in Action — Parte II: Optimizar la Carga Intrínseca

## Core Idea
La carga intrínseca no se "reduce" arbitrariamente (eso perdería contenido necesario) — se **optimiza**: se organiza y secuencia de forma que la interactividad de elementos que enfrenta el lector en un momento dado sea manejable, sin sacrificar el contenido en sí. Y crucialmente: qué tanto soporte hace falta depende del nivel de expertise del lector EN ESE DOMINIO PUNTUAL — no es un valor fijo.

## Frameworks Introducidos
- **Pre-teaching**: enseñar por separado, antes, los elementos que van a tener que integrarse simultáneamente después — reduce la interactividad de elementos en el momento de la integración porque cada pieza ya está consolidada.
- **Segmentación (segmentation)**: dividir contenido complejo en partes más pequeñas y manejables, presentadas secuencialmente en vez de todas juntas — reduce cuántos elementos hay que sostener en memoria de trabajo en un momento dado.
- **Secuenciación y combinación (sequencing and combination)**: el orden en que se presentan los segmentos, y cuándo se vuelven a combinar en el todo, importa tanto como la segmentación en sí.
- **Efecto de reversión de la experiencia (expertise-reversal effect)**: "los estudiantes necesitan cantidades distintas de soporte según su nivel de expertise" — y, crucialmente, las recomendaciones instruccionales para novatos y para expertos suelen estar **invertidas**. Novatos se benefician de ejemplos resueltos (alta guía estructurada); expertos se benefician más de resolución de problemas directa, porque el ejemplo resuelto se vuelve **redundante** para ellos (ya conocen el procedimiento) — la práctica es lo que necesitan para automatizar.

## Conceptos Clave
- **Condiciones de frontera (boundary conditions)**: toda recomendación instruccional de la CLT viene con condiciones sobre cuándo aplica y cuándo no — nunca hay una técnica "la mejor" en abstracto, siempre depende del contexto y del lector.
- **Expertise específico de (sub)dominio**: cuando el efecto de reversión de la experiencia habla de "más experto/más novato", se refiere específicamente a un dominio o incluso sub-dominio puntual (ej. "balancear ecuaciones químicas" o "escribir una oración temática"), NO a un nivel general de inteligencia o preparación. La misma persona puede ser experta en un sub-dominio y novata en otro.

## Modelos Mentales
- Ninguna técnica instruccional es universalmente "la mejor" — siempre hay que preguntar "¿la mejor para quién, en qué dominio específico, en qué momento de su desarrollo de expertise ahí?"
- Un ejemplo resuelto que ayuda a un novato puede activamente perjudicar a un experto en ese mismo sub-dominio (redundancia que consume carga extraña sin aportar).

## Anti-patrones
- **Aplicar el mismo nivel de andamiaje sin considerar expertise específico de dominio**: es la violación central del efecto de reversión de la experiencia.
- **Usar "el lector es experto" como juicio general**: el efecto es específico de sub-dominio — alguien puede ser experto en un tema y novato en el de al lado, dentro de la misma materia.

## Key Takeaways
1. Optimizar carga intrínseca (pre-teaching, segmentación, secuenciación) no es lo mismo que simplificar el contenido — es organizarlo para que la interactividad de elementos sea manejable sin perder profundidad.
2. El efecto de reversión de la experiencia es una **confirmación directa, con nombre académico formal**, de la regla ya definida en la arquitectura (2.1.3): antes del umbral, ejemplo resuelto; después del umbral, problema-primero — y el umbral se mide por sub-dominio específico, nunca de forma global.
3. Ninguna recomendación instruccional es universal — siempre viene con condiciones de frontera que dependen del lector y del contexto.

## Connects To
- **2.1.3 (umbral de fading e inversión) del documento de arquitectura**: esta es la fuente académica formal y con nombre propio ("expertise-reversal effect") de la regla ya integrada — confirma explícitamente que el umbral debe evaluarse por sub-dominio específico, tal como ya estaba diseñado.
- **`perfil-academico` dim. 4 (nivel de expertise por tema/familia)**: la justificación teórica formal de por qué ese campo no puede ser un valor único global.
