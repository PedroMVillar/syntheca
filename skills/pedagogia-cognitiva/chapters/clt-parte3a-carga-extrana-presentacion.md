# CLT in Action — Parte III-A: Reducir la Carga Extraña (presentación)

## Core Idea
La carga extraña es la que un mal diseño de presentación agrega innecesariamente, sin aportar nada al aprendizaje. Los cuatro efectos de esta sección (redundancia, split-attention, información transitoria, modalidad) son las formas más documentadas en que un material bien intencionado termina saturando memoria de trabajo sin necesidad.

## Frameworks Introducidos
- **Efecto de redundancia (redundancy effect)**: información adicional que no aporta nada nuevo (repetir en texto lo que ya muestra un diagrama, notas al pie no esenciales) consume memoria de trabajo sin necesidad — el lector no puede "ignorarla gratis", procesarla ya cuesta recursos aunque sea prescindible. Cita directa del propio Sweller sobre por qué evitar notas al pie: consumen memoria de trabajo en algo distinto de lo que se quiere enseñar.
- **Efecto de atención dividida (split-attention effect)**: "información que debe combinarse debe colocarse junta en espacio y tiempo." Cuando dos fuentes de información (ej. diagrama y su descripción) deben integrarse mentalmente para entenderse, separarlas físicamente (en el espacio, ej. página distinta) o temporalmente (una después de la otra) fuerza al lector a gastar memoria de trabajo en la integración en sí, en vez de en el contenido.
  - Aplica también a paginación: si hace falta pasar de página para integrar información de una misma idea, eso induce split-attention.
- **Información transitoria (transient information effect)**: información que desaparece (audio, animación) es más difícil de procesar que información persistente (texto, imagen fija), porque no se puede "releer" — genera carga extra si el contenido es complejo y no hay forma de volver a consultarlo.
- **Efecto de modalidad (modality effect)**: cuando hay que integrar dos fuentes de información, presentar una en modalidad visual y otra en auditiva (en vez de las dos en visual) puede aliviar la carga, porque usa dos "canales" de memoria de trabajo en paralelo en vez de saturar uno solo — pero está en tensión con el efecto de información transitoria (el canal auditivo es inherentemente transitorio).

## Conceptos Clave
- **Espacio Y tiempo, no solo espacio**: el split-attention no es solo sobre layout físico — también aplica a la sincronización temporal (ej. narración de audio que no coincide con lo que se muestra en pantalla en ese momento).
- **Redundancia ≠ inofensiva**: la intuición dice que información extra "no hace daño" — la CLT muestra que sí, porque procesar algo (aunque sea prescindible) consume el mismo recurso limitado.
- **Formato integrado vs. formato dividido**: la comparación empírica estándar de la investigación de split-attention — el formato integrado (texto y diagrama fusionados en una sola vista) sistemáticamente supera al formato dividido.

## Modelos Mentales
- Antes de agregar cualquier elemento (nota al pie, aclaración adicional, capa visual extra), preguntar: "¿esto es necesario para entender, o es redundante?" — si es redundante, sacarlo, no "por las dudas dejarlo".
- Si dos piezas de información necesitan combinarse mentalmente para tener sentido, la respuesta de diseño casi siempre es acercarlas físicamente, no dejarlas separadas "por prolijidad".

## Anti-patrones
- **Footnotes o aclaraciones "por las dudas"**: cita textual del propio Sweller — son redundancia que consume memoria de trabajo en algo distinto de lo que se enseña.
- **Diagrama en un lugar, descripción/leyenda en otro**: el caso clásico de split-attention en geometría — casi siempre perjudica el aprendizaje frente al formato integrado.
- **Requerir cambio de página para integrar información de un mismo concepto**: split-attention por paginación, evitable con buen diseño de layout.

## Key Takeaways
1. La redundancia no es neutral — cuesta recursos de memoria de trabajo aunque el lector "podría ignorarla".
2. Información que debe combinarse mentalmente debe colocarse junta en espacio Y tiempo — este es el fundamento académico formal, con nombre propio, de la regla de "contigüidad" que ya estaba integrada en la arquitectura sin ese nombre.
3. El efecto de modalidad y el de información transitoria están en tensión — no hay una solución universal, depende de la complejidad del contenido y si el lector puede "pausar/releer".

## Connects To
- **2.1.2 (minimalismo visual, contigüidad texto-diagrama) del documento de arquitectura**: esta sección es la fuente académica formal exacta de esas dos reglas — "split-attention effect" es el nombre técnico preciso que la arquitectura no tenía todavía, y "redundancy effect" confirma por qué las fórmulas tampoco están exceptuadas del minimalismo.
