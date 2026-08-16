# Patrones y técnicas — pedagogia-cognitiva

## Diagnóstico de conocimiento previo antes de redactar
**Cuándo usar**: siempre, antes de generar cualquier síntesis nueva sobre un tema.
**Cómo**: consultar `perfil-academico` (dim. 6, brechas identificadas) en vez de asumir un nivel estándar; si el perfil no tiene ese tema cubierto, tratarlo como conocimiento previo desconocido, no como cero.
**Trade-offs**: sobre-diagnosticar (preguntar de más) cuesta tiempo; sub-diagnosticar (asumir de más) genera contenido mal calibrado — el perfil estructurado existe justamente para evitar tener que elegir entre ambos.

## Descomposición en componentes + práctica de integración
**Cuándo usar**: cualquier habilidad compleja compuesta de sub-habilidades (resolver un problema multi-paso, escribir código, argumentar formalmente).
**Cómo**: enseñar cada componente por separado primero (blocked practice, 2.1.2), después ejercitar específicamente la integración de componentes (no asumir que aparece sola), y por último exponer el conocimiento condicional (cuándo aplicar cada cosa).
**Trade-offs**: saltear el paso de integración es la falla más común — deja al lector "sabe las partes, no puede combinarlas".

## Feedback como discrepancia, no como sanción
**Cuándo usar**: en toda sección de "Errores comunes" o micro-chequeo de la plantilla.
**Cómo**: describir el error como brecha objetiva respecto a un criterio ("esto no coincide con X premisa, por Y motivo"), nunca como juicio ("está mal", "no entendiste").
**Trade-offs**: ninguno real — es una técnica de costo cero que cambia directamente el impacto en aprendizaje (HLW Ch6).

## Motivación vía valor subjetivo + expectativa de éxito
**Cuándo usar**: al redactar la apertura (motivación) de cada tema nuevo.
**Cómo**: anclar el tema en algo relevante para el perfil específico del lector (sube valor subjetivo — dim. 3-10 del perfil) Y construir una primera victoria alcanzable antes de escalar dificultad (sube expectativa de éxito).
**Trade-offs**: un tema genérico "motivador en teoría" pero no anclado al perfil específico no sube el valor subjetivo real.

## Andamiaje decreciente calibrado por tema, no global
**Cuándo usar**: al decidir el nivel de detalle de un ejemplo resuelto (paso 4 de la plantilla).
**Cómo**: usar el nivel de expertise del perfil **por tema/familia específico** (no un nivel único global) para decidir cuántos pasos explicitar — más detalle si es novato en ESE tema puntual, menos si ya tiene base ahí aunque sea novato en otros.
**Trade-offs**: usar un nivel de expertise global en vez de por-tema genera sobre-explicación en temas donde el lector ya es experto (percibido como condescendiente) o sub-explicación en temas nuevos.

## Combatir la ilusión de competencia con testing distribuido
**Cuándo usar**: siempre, dentro de cada bloque teórico, no solo al final del documento.
**Cómo**: intercalar preguntas cortas de autoevaluación (adjunct questions) inmediatamente después de cada fragmento — nunca antes, nunca solo concentradas al cierre.
**Trade-offs**: sin esto, la fluidez de la lectura genera una falsa sensación de dominio que no se corresponde con retención real (HLW Ch7, MIS Ch5 — confirmado por dos fuentes independientes).

## Blocked practice antes de interleaving, nunca al revés
**Cuándo usar**: al diseñar la secuencia de ejercicios de cualquier tema nuevo.
**Cómo**: primera tanda de ejercicios 100% del tema nuevo, sin mezclar (blocked); recién cuando el tema está mínimamente asimilado, empezar a intercalar con temas previos de la MISMA familia.
**Trade-offs**: intercalar antes de tiempo (sin blocked practice previo) genera frustración sin el beneficio de discriminación — el interleaving necesita una base ya asimilada para funcionar (MIS Ch3).

## Generación antes que explicación, después del umbral de expertise
**Cuándo usar**: cuando el perfil indica competencia intermedia o mayor en el tema puntual.
**Cómo**: presentar el problema/pregunta ANTES de la explicación teórica — el intento de generar una respuesta (aunque falle) mejora retención más que ver la solución directo, siempre que haya feedback correctivo inmediato después.
**Trade-offs**: con un lector novato en el tema, invertir el orden sin base previa genera solo frustración sin beneficio — por eso el umbral de expertise (2.1.3) es una condición, no una regla universal (MIS Ch4).

## Calibración honesta vía testing bajo condiciones realistas
**Cuándo usar**: al diseñar el verificador-numérico y cualquier mecanismo de autoevaluación del propio texto generado.
**Cómo**: nunca confiar en el juicio subjetivo de "esto está bien" — verificar con un mecanismo independiente (script, cálculo externo) bajo condiciones lo más parecidas posible a la aplicación real.
**Trade-offs**: sin esto, tanto el lector como el propio sistema generador pueden caer en la misma ilusión de saber (MIS Ch5) — de ahí que la verificación numérica del documento de arquitectura sea un gate duro, no opcional.

## Retirar el andamiaje/mnemotécnico una vez automatizado
**Cuándo usar**: al decidir cuándo dejar de usar una metáfora o analogía de apoyo para un concepto.
**Cómo**: usar el mnemotécnico mientras el concepto se consolida; una vez que el perfil indica dominio en ese tema puntual, dejar de reforzarlo explícitamente — coincide con el fading ya definido para ejemplos resueltos.
**Trade-offs**: un mnemotécnico que se mantiene indefinidamente como muleta impide que el conocimiento se automatice del todo (MIS Ch7).

## Optimizar carga intrínseca sin perder contenido (pre-teaching + segmentación)
**Cuándo usar**: al introducir un tema complejo con muchos elementos interdependientes.
**Cómo**: enseñar por separado, antes, los componentes que después se van a integrar (pre-teaching); dividir el contenido en segmentos manejables presentados secuencialmente (segmentación) en vez de todo junto.
**Trade-offs**: sin esto, la interactividad de elementos puede superar la capacidad de memoria de trabajo del lector, aunque el contenido en sí no sea "demasiado" en abstracto (CLT Parte II).

## Contigüidad texto-diagrama (split-attention effect)
**Cuándo usar**: siempre que texto y diagrama/figura deban integrarse mentalmente para tener sentido.
**Cómo**: colocar la información que debe combinarse junta en espacio Y tiempo — nunca forzar al lector a integrar mentalmente información separada físicamente (páginas distintas) o temporalmente (narración desincronizada).
**Trade-offs**: separar información relacionada, aunque parezca "más prolijo" u organizado, sistemáticamente empeora el aprendizaje frente al formato integrado (CLT Parte III-A).

## Eliminar redundancia real, incluso en notación técnica
**Cuándo usar**: al revisar cualquier fórmula, footnote, o aclaración "por las dudas".
**Cómo**: si la información no aporta nada nuevo (repite en texto lo que ya muestra una fórmula o diagrama), eliminarla — no es inofensiva aunque el lector "pueda ignorarla".
**Trade-offs**: cita directa del propio Sweller citada en CLT in Action — hasta las notas al pie "necesarias" pueden inducir split-attention si no están bien integradas (CLT Parte III-A).

## Autoexplicación incrustada en cada ejemplo resuelto
**Cuándo usar**: en cada ejemplo resuelto de la plantilla (paso 4).
**Cómo**: no dejar el ejemplo como lectura pasiva — pedir explícitamente que el lector explique con sus propias palabras por qué cada paso es correcto antes de avanzar.
**Trade-offs**: la diferencia de aprendizaje entre "leer un ejemplo resuelto" y "leerlo + autoexplicar" es sustancial — es una técnica de costo casi cero (CLT Parte III-B).

## Reformular la meta de un ejercicio como abierta, no siempre fija
**Cuándo usar**: cuando el objetivo pedagógico es que el lector aprenda el patrón subyacente, no solo llegue a un resultado puntual.
**Cómo**: en vez de "encontrá el valor de X", plantear "encontrá tantas variables como puedas" — redirige la atención del lector del análisis medios-fines hacia la estructura del problema.
**Trade-offs**: contraintuitivo — una meta más abierta puede generar MÁS aprendizaje y, sorprendentemente, mayor probabilidad de acertar el resultado específico también (CLT Parte III-B, goal-free effect).

## Auditar el "residuo de pensamiento" antes de aprobar un ejercicio
**Cuándo usar**: al revisar cualquier ejercicio o actividad antes de incluirlo en una síntesis.
**Cómo**: simular explícitamente en qué va a estar pensando el lector momento a momento durante el ejercicio — si el pensamiento activo se dirige a algo periférico (logística, formato) en vez del concepto central, redisñar.
**Trade-offs**: una actividad bien intencionada puede fallar completamente si el pensamiento real que genera no es el que se buscaba (WDSL Ch3).

## Comparar ejemplos de a pares para extraer estructura profunda
**Cuándo usar**: al presentar un concepto abstracto a través de ejemplos concretos.
**Cómo**: presentar al menos dos ejemplos con distinto contexto (superficie) pero la misma estructura de solución (profundidad), señalando explícitamente qué comparten — nunca un solo ejemplo aislado.
**Trade-offs**: un solo ejemplo, por bueno que sea, arriesga que el lector memorice el caso concreto sin extraer el patrón transferible (WDSL Ch4, confirmado por MIS Ch6).

## Frente de flashcard con información mínima
**Cuándo usar**: al generar cualquier card nueva desde `conceptos_ya_cubiertos`.
**Cómo**: el frente es un estímulo único (pregunta o término), sin pistas adicionales que permitan reconocimiento en vez de recuperación. El dorso es la respuesta exacta, sin ambigüedad.
**Trade-offs**: un frente "más fácil" (con pistas) se siente mejor al estudiar pero reduce el esfuerzo de recuperación — y por lo tanto la retención — igual que sucede con el andamiaje excesivo en un ejemplo resuelto.

## No reciclar el texto de un chequeo ya incrustado
**Cuándo usar**: siempre que se genere una card sobre un concepto que ya tuvo un micro-chequeo (3.c) en la síntesis.
**Cómo**: reformular el ángulo de la pregunta — mismo concepto, otro contexto o forma de preguntar.
**Trade-offs**: reciclar el texto exacto convierte la segunda exposición en memorización de la pregunta puntual, no en recuperación del concepto — pierde el efecto que la repetición espaciada busca generar.
