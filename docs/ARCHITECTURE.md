# Arquitectura: Plugin generador de teoría propia personalizada

## -1. Qué es esto realmente (para no perder el eje)

Esto **no** es un generador de "apuntes de curso" genéricos. Es un sistema para que vos construyas **tu propia síntesis teórica**, a partir de:

- **Tus fuentes elegidas** (uno o varios libros + papers específicos sobre un tema — no un libro fijo por tema, sino la combinación que vos decidas para esa síntesis puntual).
- **Tu perfil académico** (qué ya sabés, qué nivel de formalismo manejás, qué te falta) — el mismo tema explicado a alguien que ya cursó álgebra lineal avanzada es un documento distinto al de alguien que no.
- **Tu herramienta de turno, si existe** (un simulador, un lenguaje como SystemVerilog, una plataforma de diseño de SoC) — y si no hay herramienta, el documento es 100% teórico y no fuerza una sección de "software" que no aplica.

Lo que **no cambia** es que sigue siendo un documento *pedagógicamente construido* — con las técnicas reales de cómo el cerebro procesa y retiene información (Capa A). La diferencia con un "apunte de enseñanza" tradicional es el destinatario: es un documento hecho para que aprendas vos, con tus huecos y tu nivel, no para un estudiante genérico.

## 0. Principios de diseño que sostienen esto

Antes de la estructura, los principios reales que la justifican (no son estética, son las razones por las que un framework de agentes bien hecho separa las cosas así):

1. **Separación conocimiento / proceso / interfaz.** El *qué sabe* el sistema (pedagogía, teoría, tu software) vive en `skills/`. El *cómo actúa* (orquestación, pasos, quién hace qué) vive en `agents/`. El *cómo se invoca* (qué escribe el usuario) vive en `commands/`. Mezclar estas capas es la causa #1 de que un framework de agentes se vuelva inmantenible.
2. **Progressive disclosure.** Ninguna skill carga todo su contenido de una. `SKILL.md` trae lo crítico (~unos miles de tokens); los capítulos/detalle se cargan on-demand. Esto ya lo hace `book-to-skill` — lo heredás gratis.
3. **Patrón orquestador-trabajador (orchestrator-worker).** Un agente principal no escribe el apunte de punta a punta solo. Delega en subagentes especializados con un solo trabajo cada uno (extraer teoría, mapear al software, redactar, criticar). Esto reduce alucinación y permite mejorar cada pieza sin tocar las demás.
4. **Quality gates automáticos.** No confiás en que el LLM "se acuerde" de aplicar las reglas pedagógicas. Un hook o script verifica mecánicamente ciertas condiciones (¿hay ejemplo resuelto?, ¿hay pregunta de recuperación activa?, ¿la notación coincide con la fuente?) antes de dar el apunte por terminado.
5. **Estado persistente / curriculum map.** El sistema necesita memoria de qué ya generó, para no repetirse y para poder armar secuencias con espaciado e intercalado (spaced practice, interleaving) — eso requiere un archivo de estado, no solo prompts sueltos.
6. **El perfil del lector es una variable de primera clase, no un detalle de prompt.** Igual que la teoría o la pedagogía, "quién sos vos como estudiante" se guarda como un artefacto propio (un perfil estructurado), porque se reutiliza en *todas* las síntesis que generes, y porque calibra el nivel de formalismo, qué se puede asumir como sabido, y qué analogías van a resonarte.
7. **Multi-fuente por síntesis, no una fuente fija por tema.** Cada documento que generás puede combinar N libros + M papers elegidos por vos para ese tema puntual. La arquitectura no asume "1 libro = 1 tema" — asume que vos armás la mezcla de fuentes cada vez, y el sistema las concilia (incluso si se contradicen o usan notación distinta).
8. **La herramienta es opcional y desacoplada.** Simulador, lenguaje de descripción de hardware, ninguna herramienta — el pipeline no depende de que exista una. Es un módulo que se enchufa si aplica, no un paso obligatorio de la plantilla.

---

## 1. Estructura de carpetas del plugin

```
syntheca/
├── .claude-plugin/
│   └── plugin.json                    # manifiesto único archivo permitido acá
│
├── commands/                          # puntos de entrada (slash commands)
│   ├── nueva-fuente.md                  # /nueva-fuente <libro/paper> → ingesta a skills/fuentes/
│   ├── setup-perfil.md                  # /setup-perfil → crea o edita skills/perfil-academico/
│   ├── nueva-herramienta.md             # /nueva-herramienta <nombre> → arma skill + mapeo-conceptos
│   ├── nuevo-banco-ejercicios.md        # /nuevo-banco-ejercicios <tps/parciales> <materia>
│   ├── generar-sintesis.md              # /generar-sintesis <tema> --materia x --fuentes a,b,c [--herramienta x] [--estilo materia] [--fuente-principal x]
│   ├── revisar-sintesis.md              # /revisar-sintesis <archivo> → re-pasa quality gate
│   └── mapa-estudio.md                  # /mapa-estudio → ver estado global (antes "mapa-curricular")
│
├── agents/                            # subagentes especializados (1 responsabilidad c/u)
│   ├── conciliador-fuentes.md           # lee VARIAS skills de fuentes/ a la vez y las concilia
│   ├── calibrador-perfil.md             # ajusta nivel/formalismo según skills/perfil-academico/
│   ├── mapeador-herramienta.md          # SOLO si hay --herramienta: vincula teoría ↔ herramienta
│   ├── estilista-ejercicios.md          # SOLO si hay --estilo: calibra ejercicios/ejemplos al
│   │                                    # formato real de tus TPs y parciales
│   ├── redactor-pedagogico.md           # escribe la síntesis aplicando reglas de Capa A + perfil
│   ├── verificador-numerico.md          # SOLO si hay ejercicios con resultado calculable:
│   │                                    # resuelve independiente con Python y contrasta
│   └── critico-calidad.md               # GATE DURO: nada se entrega sin verificación completa
│
├── skills/                            # el conocimiento, en 5 capas
│   ├── pedagogia-cognitiva/             # fusión de TODOS tus papers/libros de neurociencia +
│   │   └── SKILL.md                     # aprendizaje (Make It Stick, CLT, papers de memoria, etc.)
│   │                                     # esta capa NO enseña contenido, enseña CÓMO presentarlo
│   ├── perfil-academico/                # quién sos vos como lector — 4 dimensiones, 12 campos (2.2)
│   │   └── SKILL.md
│   ├── fuentes/                         # tus libros y papers, UNO POR FUENTE (no fusionados)
│   │   ├── libro-<autor-tema>/          # vía book-to-skill, modo technical
│   │   │   ├── SKILL.md
│   │   │   ├── chapters/
│   │   │   └── glossary.md
│   │   ├── paper-<autor-anio>/          # vía book-to-skill o extracción liviana (ver 2.3)
│   │   │   └── SKILL.md
│   │   └── ...                          # tantas como fuentes tengas acumuladas
│   ├── herramientas/                    # OPCIONAL — solo si el tema usa alguna
│   │   └── herramienta-<nombre>/        # simulador, SystemVerilog, plataforma de SoC, lo que sea
│   │       ├── SKILL.md
│   │       └── mapeo-conceptos.md       # tabla concepto-teórico → elemento-de-herramienta
│   ├── banco-ejercicios/                # OPCIONAL — Capa E, nueva: TUS TPs y parciales reales
│   │   └── <materia>/                   # ej: comunicaciones-digitales, fisica-2
│   │       ├── SKILL.md                 # patrón de estilo extraído (ver 2.5)
│   │       ├── tps/                     # enunciados de TP, generalmente sin resolver
│   │       │   └── ...
│   │       └── parciales/               # enunciados de parcial, CON solución si la tenés
│   │           └── ...
│   └── plantilla-sintesis/              # el schema de salida (sección 4), variantes según haya o no herramienta
│       └── SKILL.md
│
├── hooks/
│   └── hooks.json                      # quality gate automático (sección 5)
│
├── scripts/
│   ├── rubric_check.py                  # valida estructura de la síntesis generada
│   ├── verificar_ejercicio.py           # resuelve ejercicios numéricos de forma independiente;
│   │                                    # SE ENTREGA TAMBIÉN AL USUARIO como archivo aparte,
│   │                                    # no es solo uso interno (ver sección 5)
│   └── update_mapa_estudio.py           # actualiza estado tras cada generación
│
├── _inbox/                             # carpeta de trabajo: tirás PDFs acá antes de /nueva-fuente
│                                        # (se vacía/archiva después de cada ingesta exitosa)
├── mapa-estudio.json                    # ESTADO PERSISTENTE (no es una skill, es memoria de datos)
└── README.md
```

Nota clave de Claude Code: todas las carpetas de componentes (`commands/`, `agents/`, `skills/`, `hooks/`) van en la **raíz del plugin**, nunca dentro de `.claude-plugin/`. Ese es el error más común al armar plugins — el plugin "aparece" pero no hace nada porque los componentes quedaron mal ubicados.

---

## 2. Las cinco capas de skills, en detalle

### 2.1 `pedagogia-cognitiva` (Capa A — cómo procesa el cerebro, no qué contenido)
Generada corriendo `book-to-skill` sobre **todo** tu corpus de neurociencia/aprendizaje (Make It Stick, Why Don't Students Like School, How Learning Works, Made to Stick, Cognitive Load Theory, y tus papers de neurociencia sobre procesamiento de información) y después usando el **modo Update/Fold-in** de esa misma skill para fusionar todo en una sola skill consolidada. Esto te evita invocar N skills sueltas cada vez — el agente redactor consulta una sola fuente de reglas de estilo/estructura/carga cognitiva.

Contenido esperado: reglas accionables tipo "no introducir más de 4 elementos nuevos sin ejemplo resuelto", "recuperación activa antes que resumen pasivo", "ejemplo concreto antes que definición abstracta", más lo que digan tus papers de neurociencia sobre cómo se codifica/consolida memoria (spacing, elaboración, dual coding, etc.). **No es teoría de tu dominio** — es la capa que decide *cómo se presenta* cualquier contenido, sea circuitos, SystemVerilog o SoC.

#### 2.1.1 Sub-bloque de tono (afecta directo a `redactor-pedagogico`)
Dentro de esta misma skill, pero como sección propia (`tono.md` o una sección dedicada en `SKILL.md`), van las reglas de **cómo debe sonar** el texto — distinto de cómo debe estructurarse. Es la diferencia entre "qué orden llevan las secciones" (ya cubierto por la plantilla) y "qué voz usa cada oración". Con las dos fuentes que pasaste, quedan seis directivas fusionadas ahí:

1. **Feedback neutro, no punitivo.** El error se señala como discrepancia objetiva, nunca como falta. No es solo estética: un tono percibido como amenaza activa una respuesta de estrés que interfiere con la consolidación de memoria en el hipocampo. El `redactor-pedagogico` nunca redacta un error como "mal hecho", sino como "esto no coincide con tal premisa, por tal motivo".
2. **Simetría socrática, cero condescendencia.** El texto invita a razonar junto al lector ("¿qué pasaría si...?"), no lo trata como receptor pasivo de un dato ya masticado. Esto se traduce directo en la sección "Chequeo de comprensión" de la plantilla (sección 4) — esas preguntas no son de repaso, son de exploración conjunta.
3. **Explícito y gradual, pero con dificultades deseables.** Ni constructivismo puro (dejarte descubrir todo solo, frustrante y poco eficiente) ni todo masticado (que genera ilusión de competencia por falsa fluidez de lectura). El texto guía con estructura clara pero intercala preguntas y pausas activas en vez de dejarte deslizar cómodo por la página.
4. **Implicatura conversacional y metáfora, sin sobre-explicar ("pista, no explicación").** Se usan analogías que dejan una pequeña brecha para que el lector la cierre activamente — eso es lo que activa procesamiento profundo — evitando el extremo de explicar de más, que se procesa como condescendencia y apaga el interés.
5. **Oraciones temáticas antes que argumentales.** La apertura de cada concepto nuevo se ancla primero en el *porqué* de fondo de una decisión de diseño (una oración temática, que apela a un propósito), y recién después llegan las afirmaciones técnicas duras. Abrir directo con la afirmación argumental ("esto es superior porque...") despierta resistencia; abrir con el propósito de la decisión no.
6. **Narrativa en primera persona — con o sin herramienta.** El texto no se redacta como manual de instrucciones frío — se redacta como si "vos" (el futuro lector, vos mismo repasando) fueras el protagonista que se topó con un obstáculo concreto. Cuando hay herramienta, ese obstáculo es de implementación (un límite de ancho de banda, un bug de simulación, una restricción de área en el chip). **Cuando no hay herramienta** (tema puramente teórico), el obstáculo pasa a ser una tensión conceptual sin resolver o un límite de diseño que la teoría misma enfrenta ("por qué no alcanza con el enfoque simple, y qué fuerza a este otro") — anclado siempre en el Obstáculo de Relevancia del perfil (dim.3-10, sección 2.2), nunca en un obstáculo genérico inventado sin conexión con vos. Párrafos cortos, concisos, fáciles de escanear.

#### 2.1.2 Sub-bloque estructural-generativo (afecta a `redactor-pedagogico` Y a la plantilla misma)
Estas directivas no son de "voz", son de **qué mecanismos generativos hay que incrustar en el propio texto** para forzar procesamiento activo. Se guardan también en `pedagogia-cognitiva`, pero impactan directamente el diseño de la plantilla (sección 4), no solo el estilo de redacción:

- **Minimalismo visual — sin excepción para fórmulas.** Nada de ilustraciones o decoración que no cumpla una función semántica directa: cada imagen/diagrama compite por los mismos recursos de atención que el contenido, y el exceso de adorno visual debilita el procesamiento en la corteza prefrontal. Esto **incluye a las fórmulas** — no están exceptuadas por ser "el contenido en sí": el procesamiento de notación matemática densa es intensamente demandante en recursos visuales/atencionales, así que una fórmula tampoco debe rodearse de adorno adicional; se muestra limpia, sin decoración alrededor. El `redactor-pedagogico` solo genera un diagrama/figura cuando reemplaza texto (nunca como acompañamiento decorativo), y cuando hay texto + diagrama juntos, deben quedar coordinados/próximos — el cerebro integra imagen y texto por vías separadas, y si quedan disociados en el documento fuerza un cambio de atención costoso que interrumpe el procesamiento consciente.
- **Diagramas: generados por el lector o entregados ya resueltos, según el perfil.** No hay una única respuesta correcta — depende de `perfil-academico`: si ya hay conocimiento previo del área, conviene *pedirle al lector que arme su propio diagrama* (esto es en sí mismo un prompt generativo más, ver el punto de GLT); si el tema es nuevo sin base previa, conviene entregar el diagrama ya armado, porque el lector todavía no tiene el esquema mental para poder construirlo por su cuenta sin sobrecargarse.
- **Diagrama progresivo vs. estático — según el tipo de contenido, no según el perfil.** Progresivo (armado paso a paso) cuando el contenido es secuencial/procedimental — un pipeline, una máquina de estados, un algoritmo — por el mismo motivo que ya fundamenta la micro-estructura 3.a→3.b→3.c de la plantilla: construir por etapas evita saturar de golpe la memoria de trabajo. Estático (una sola vista completa) cuando el contenido es estructural/relacional simultáneo — topología de un circuito, bloques de un SoC — porque ahí las relaciones necesitan verse todas juntas para tener sentido; partirlo en pasos rompe la comprensión de conjunto en vez de ayudarla.
- **Intercalado real de ejercicios (interleaving), con tres condiciones precisas — no aplica siempre igual.**
  - **Fase previa obligatoria: práctica en bloque.** Si el tema es nuevo y complejo, el primer bloque de ejercicios debe ser 100% del tema nuevo, sin intercalar nada todavía — recién cuando el `perfil-academico` (o el propio desarrollo del documento) indica que el procedimiento básico ya está asimilado, se pasa a la fase de intercalación. Intercalar antes de tiempo, sobre un concepto aún no asimilado, no genera el efecto buscado.
  - **Criterio de similitud (Goldstone).** Solo se intercalan conceptos que compiten por la misma familia de solución — esto es lo que fuerza discriminación real (¿qué fórmula/estrategia corresponde acá?). Mezclar conceptos de familias completamente distintas no aporta nada porque es obvio cuál usar en cada caso; en ese caso el sistema no debe forzar la mezcla, solo el espaciado natural del documento alcanza. Si los ejemplos dentro de una misma familia son muy heterogéneos entre sí, puede convenir más bloquearlos que intercalarlos.
  - **Progresión de dificultad en cada reaparición.** Cada vez que un concepto ya visto reaparece intercalado, no debe presentarse con el mismo formato/dificultad — hay que subir la complejidad o el contexto de aplicación (transferencia). Presentar lo idéntico reduce la novedad y genera ilusión de saber; el objetivo, además de espaciar, es exigir composición de conocimientos (recombinar una destreza ya automatizada en un contexto nuevo).
- **Prompts de Teoría del Aprendizaje Generativo (GLT), incrustados en el cuerpo, no al final.** El texto debe forzar, en el medio de cada bloque teórico (no solo al cierre): reformulación con tus propias palabras, una pregunta elaborativa tipo "¿por qué esta regla aplica acá y no en el otro caso?", una imagen mental/analogía propia, y una conexión explícita con lo que ya sabías antes de este tema.
- **Testing effect distribuido, no concentrado en una sola sección final — con posición y cantidad precisas.** El texto debe forzar, en el medio de cada bloque teórico (no solo al cierre): reformulación con tus propias palabras, una pregunta elaborativa tipo "¿por qué esta regla aplica acá y no en el otro caso?", una imagen mental/analogía propia, y una conexión explícita con lo que ya sabías antes de este tema. La investigación sobre *adjunct questions* agrega un detalle operativo concreto: estas preguntas rinden más colocadas **inmediatamente después** del fragmento de texto que antes, y el número óptimo es de **2 a 3 preguntas cortas de desarrollo (short-answer) por subsección** — ni una sola pregunta genérica al final del bloque, ni un cuestionario largo que sature.

Estas seis reglas de tono son las que `critico-calidad` (agente, sección 3) también chequea de forma cualitativa antes de aprobar: no solo "¿están las secciones?" sino "¿el tono es neutro ante el error, socrático, y deja espacio a la metáfora sin sobre-explicar?".

#### 2.1.3 Sub-bloque de andamiaje decreciente / fading (afecta al paso "Ejemplo resuelto" de la plantilla)
Responde directo al Eje 3 que quedaba abierto — cierra cómo dosificar ejemplos resueltos según nivel de expertise, con cuatro reglas encadenadas:

1. **No hay proporción fija ("1 cada N conceptos").** La dosis depende de la dificultad del material y del conocimiento previo indicado en `perfil-academico`, no de un contador de conceptos. Para temas complejos o donde el perfil indica poca base: priorizar ejemplo resuelto completo + práctica en bloque antes de pedir resolución autónoma — la memoria de trabajo de un novato se desborda si lo exponés a variedad antes de tiempo.
2. **Fading: menos pasos explicitados a medida que el perfil indica más experiencia en ESE tema puntual.** Al principio el procesamiento es consciente y lento (cuesta caro en corteza prefrontal) y ahí el detalle paso a paso es andamiaje necesario. Una vez que el perfil (o el propio avance dentro del documento) indica que la operación ya se consolidó, seguir detallando pasos obvios pasa a ser contraproducente — se vuelve el mismo problema que "sobre-explicar" del punto 4 de tono (2.1.1).
3. **Alternar ejemplo 100%-resuelto con ejemplo-parcial (a completar), no un solo formato fijo.** Un documento que solo muestra resoluciones completas invita a lectura pasiva (asentís, no procesás). Intercalar ejemplos donde el lector tiene que completar el último paso o deducir una variable fuerza retrieval practice + autoexplicación — es una dificultad deseable más, en la misma familia que los micro-chequeos (2.1.2).
4. **Umbral de expertise que invierte el orden completo del bloque.** Antes del umbral (novato en ese tema): Instrucción explícita → Ejemplo resuelto en detalle → Ejercicios guiados. Después del umbral (competencia intermedia ya alcanzada en ese tema, según `perfil-academico` o según lo que el propio documento ya cubrió): se invierte a Problema/autoevaluación primero → Feedback teórico después — enfrentar el problema sin la respuesta genera una señal de error de predicción que abre la plasticidad neuronal para absorber mejor la explicación que viene después.

El umbral del punto 4 es el mismo mecanismo, a nivel de un bloque completo, que el criterio de "blocked practice → interleaving" del punto 2.1.2: primero anclar la base, después exigir esfuerzo activo — nunca al revés.

### 2.2 `perfil-academico` (Capa nueva — quién sos vos)
Una skill chica pero crítica, que vos escribís/actualizás (no sale de un libro). Se estructura en **4 dimensiones**, cada una con un rol operativo concreto — no es una lista de datos sueltos, cada campo alimenta a un agente o a un paso específico de la plantilla:

**Dimensión 1 — Capa exterior (competencias explícitas):**
1. Formación de base e identidad académica (qué carrera/materias ya dominás) → determina qué se puede asumir sabido.
2. Nivel de formalismo matemático cómodo → decide si el `redactor-pedagogico` usa demostración rigurosa o aproximación intuitiva.
3. Idiomas de decodificación y manejo de jerga → evita que la traducción mental compita con la atención ejecutiva.

**Dimensión 2 — Capa interior (estructura cognitiva y motivación):**
4. Anclajes y analogías preferidas (física, código, cotidiano) → alimenta directo el tipo de metáfora que usa el sub-bloque de tono (2.1.1-4).
5. Mindset ante el error (autoexigencia, resiliencia) → calibra cuánta guía socrática hace falta para no disparar ansiedad — conecta directo con 2.1.1-1 (feedback neutro).
6. Brechas de conocimiento identificadas por vos mismo (metacognición activa) → la síntesis apunta específicamente a esa brecha, no a repetir lo que ya sabés.
7. Valores/creencias rectoras de la disciplina (qué te parece "elegante" o valioso) → define qué oración temática (2.1.1-5) usar para encuadrar cada concepto nuevo.

**Dimensión 3 — Mapa de obstáculos (resistencias que el documento debe demoler):**
8. Obstáculo de Cognición Funcional — ¿entendés qué problema real resuelve el concepto? → el `redactor-pedagogico` abre cada tema con el problema/necesidad física antes de la fórmula (esto ya estaba en la plantilla como paso 1, ahora tiene fundamento explícito por perfil).
9. Obstáculo de Ventaja — ¿entendés por qué esta solución y no otra? → obliga a que el marco teórico compare trade-offs y alternativas descartadas, no solo presente la solución elegida como única.
10. Obstáculo de Relevancia — ¿ves la conexión con tu carrera/proyectos? → alimenta la narrativa en primera persona (2.1.1-6): el "obstáculo concreto" de la narrativa debe anclarse en algo relevante para VOS puntualmente, no genérico.

**Dimensión 4 — Directivas de secuenciación (por tema/familia, no un valor único global):**
11. Nivel de andamiaje/fading actual → alimenta directo el umbral de inversión de 2.1.3.
12. Estrategia de intercalado/spacing preferida → alimenta directo el criterio de familia de 2.1.2.

Los campos 11 y 12 confirman algo que ya habíamos definido por necesidad de diseño: el perfil **no es un valor único global** — se completa **por tema o familia de conocimiento**, porque podés ser experto en circuitos digitales y novato en FEC, y el `calibrador-perfil` necesita saber cuál aplica en cada síntesis puntual.

### 2.3 `fuentes/` (Capa B — tus libros y papers, sin fusionar)
Una skill **por fuente individual**, vía `book-to-skill`:
- Libros → modo **Technical** (preserva fórmulas, tablas, notación exacta).
- Papers → mismo flujo; si son cortos, `book-to-skill` igual funciona pero podés pedir un extraction más liviano (menos capítulos, un solo resumen denso).

Clave: **no fusiones fuentes entre sí**. Cada una mantiene su propia notación y precisión terminológica — dos autores pueden nombrar lo mismo distinto, y necesitás que el sistema sepa que son fuentes separadas para poder conciliarlas explícitamente en vez de mezclarlas a ciegas. El `conciliador-fuentes` (agente, sección 3) es quien decide qué tomar de cada una cuando generás una síntesis puntual con `--fuentes libro-x,paper-y,paper-z`.

### 2.4 `herramientas/` (Capa C — OPCIONAL)
Solo existe si el tema la necesita. Se arma a mano con `skill-creator` (no `book-to-skill`, no hay libro fuente) porque es conocimiento que **no existe en ningún lado más que en tu cabeza**: cómo se usa tu simulador, cómo se estructura un módulo en SystemVerilog para tu flujo de trabajo, qué convenciones seguís en un diseño de SoC. Estructura mínima:
- `SKILL.md`: qué representa/hace cada pieza de la herramienta, con un campo `tipo` (`simulador` / `lenguaje` / `diagrama-arquitectura`) que determina el esquema de la tabla siguiente.
- `mapeo-conceptos.md`: la tabla **no tiene un formato único** — el esquema de columnas depende del `tipo`, porque lo "accionable" es distinto en cada caso:
  - **`simulador`** → `concepto teórico → parámetro/control + rango de valores esperado` (ej: "polinomio generador" → "GENERATOR_POLY, rango 0x00-0xFF").
  - **`lenguaje`** (SystemVerilog y similares) → `concepto teórico → construcción de código + snippet mínimo` (ej: "registro de desplazamiento" → `shift register`, con 3-4 líneas de ejemplo).
  - **`diagrama-arquitectura`** (SoC sin plataforma ejecutable) → `concepto teórico → bloque del diagrama + rol funcional` (ej: "árbitro de bus" → bloque "Arbiter", rol "resuelve contención entre masters").

Sin esta tabla el agente no puede vincular teoría con práctica de forma confiable — solo puede alucinar la conexión.

Si el tema es puramente teórico (ej. "arquitecturas de decodificadores FEC en general, sin implementación todavía"), esta capa simplemente no se invoca — el pipeline lo detecta por la ausencia del flag `--herramienta`.

### 2.5 `banco-ejercicios/<materia>` (Capa E — OPCIONAL, tus TPs y parciales reales)

Esta es la capa que resuelve algo que ninguna de las anteriores cubre: que los ejercicios que el sistema genera **suenen y se estructuren como los que realmente te toman**, no como ejercicios genéricos de manual. Se arma vía `book-to-skill` o extracción liviana sobre los PDFs de tus TPs y parciales, con una diferencia clave respecto a `fuentes/`: acá lo que importa extraer no es contenido teórico, es **patrón de forma** — cómo se fraseán los enunciados, cuántas partes suele tener un problema, qué notación usan tus profesores, y (cuando el parcial viene con solución) cómo se estructura una resolución "tipo" de esa cátedra.

Contenido de `SKILL.md` para cada materia:
- **Patrón de enunciado**: estructura típica (dato→pedido, multi-inciso, con/sin gráfico de partida), longitud habitual, convenciones de notación de esa cátedra específica.
- **Curva de dificultad TP vs. parcial**: los TPs suelen ser guiados y de una sola familia de concepto por ejercicio; los parciales suelen combinar 2-3 familias en un mismo problema y tienen menos andamiaje. Esta distinción es la que conecta directo con la plantilla (ver abajo).
- **Ejercicios resueltos de parcial, cuando los tenés**: se guardan como ejemplos de referencia de "cómo se ve una resolución completa esperada por esa cátedra" — el `estilista-ejercicios` los usa para calibrar el paso 4 (ejemplo resuelto) de la plantilla, imitando estructura y nivel de detalle, nunca copiando el enunciado o la resolución palabra por palabra (se parafrasea y se generan variantes nuevas con la misma forma, para que sirvan como práctica real y no como plagio de tu propio parcial).

**Por qué esto encaja natural con lo que ya teníamos, sin inventar mecanismos nuevos:**
- El paso **6.a (práctica en bloque)** de la plantilla ya pedía ejercicios "solo del tema nuevo, sin intercalar" — ese es exactamente el perfil de un ejercicio de TP. Cuando existe `--estilo <materia>`, 6.a se genera imitando el patrón de TP de esa materia en vez de un formato genérico.
- El paso **6.b (práctica intercalada, mayor dificultad, mezcla de familias)** ya pedía justo lo que un parcial real hace: combinar familias de conceptos con menos andamiaje. Cuando existe `--estilo <materia>`, 6.b se calibra contra el patrón de parcial de esa materia.
- El paso **4 (ejemplo resuelto)** — si hay un parcial resuelto de una familia de concepto compatible con el tema actual, se usa como referencia de formato para ese ejemplo, respetando el nivel de detalle que indican las reglas de fading (2.1.3) según tu expertise en ese tema puntual.

Si no pasás `--estilo`, el pipeline simplemente genera ejercicios con el formato por default de la plantilla — esta capa es aditiva, no reemplaza nada de lo ya definido, solo lo calibra mejor cuando existe el material real.

### 2.6 `plantilla-sintesis` (schema de salida)
No es conocimiento de dominio, es la **forma** del output, con una variante "con herramienta" y otra "solo teórica". Ver sección 4.

---

## 3. Los subagentes (patrón orquestador-trabajador)

En vez de que un solo prompt gigante intente "conciliar N fuentes + saber pedagogía + calibrar tu nivel + vincular herramienta + escribir bien + revisarse a sí mismo" (que es como se generan alucinaciones y síntesis inconsistentes), cada responsabilidad es un subagente separado que el comando principal invoca en secuencia:

```
/generar-sintesis "Decodificadores FEC" --fuentes libro-fec-lin-costello,paper-viterbi-1967 [--herramienta systemverilog] [--estilo comunicaciones-digitales] [--fuente-principal libro-fec-lin-costello]
        │
        ▼
┌─────────────────────────┐
│ conciliador-fuentes       │  lee TODAS las skills en --fuentes en paralelo
│                            │  detecta solapes, notación distinta, Y contradicciones de fondo
│                            │  entre autores. Ante notación distinta: unifica citando origen.
│                            │  Ante contradicción real de fondo: NUNCA elige en silencio —
│                            │  si vino --fuente-principal, esa se presenta como marco primario
│                            │  y las demás como contraste explícito; si no vino el flag,
│                            │  presenta ambas posturas atribuidas a su autor, sin fusionarlas
│                            │  en una sola voz
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ calibrador-perfil          │  lee skill perfil-academico
│                            │  decide qué se puede asumir sabido, qué nivel de formalismo usar
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ mapeador-herramienta        │  SOLO si vino --herramienta: lee esa skill + mapeo-conceptos.md
│  (condicional)              │  si no vino flag, este paso se salta entero
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ estilista-ejercicios        │  SOLO si vino --estilo: lee banco-ejercicios/<materia>
│  (condicional)              │  saca patrón de TP (→ 6.a) y de parcial (→ 6.b y 4, si aplica)
│                            │  si no vino flag, este paso se salta entero
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ redactor-pedagogico         │  lee skill pedagogia-cognitiva (estructura + sub-bloque de tono)
│                            │  y plantilla-sintesis; combina todo aplicando TODAS las reglas:
│                            │  cómo se ordena, cómo suena cada oración, y (si aplica) qué forma
│                            │  tienen tus ejercicios reales
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ verificador-numerico        │  SOLO si el tema tiene ejercicios con resultado calculable
│  (condicional)              │  (física, señales, cualquier cosa con número/resultado
│                            │  verificable): corre un script Python que resuelve
│                            │  independientemente cada ejercicio y contrasta contra
│                            │  lo que escribió el redactor. Si no coincide, vuelve al
│                            │  redactor. El script queda además como archivo entregable
│                            │  (ver sección 5) para que VOS también puedas correrlo.
└──────────┬─────────────────┘
           ▼
┌─────────────────────────┐
│ critico-calidad             │  GATE DURO: no entrega nada hasta que TODO esté verificado
│                            │  — corre rubric_check.py + revisión cualitativa de tono/
│                            │  estructura + confirma que verificador-numerico (si aplicó)
│                            │  dio OK. Si cualquiera falla: vuelve al redactor con
│                            │  feedback puntual, nunca entrega un borrador a medio validar
└──────────┬─────────────────┘
           ▼
   síntesis final (100% verificada) + actualización de mapa-estudio.json
```

Cada agente tiene su propio archivo en `agents/` con su propósito acotado. Esto es exactamente el patrón que usa Anthropic internamente para tareas de investigación complejas: subagentes con contexto limpio y una sola responsabilidad superan a un solo agente tratando de hacer todo, porque cada uno puede ser evaluado y mejorado de forma aislada. `mapeador-herramienta`, `estilista-ejercicios` y `verificador-numerico` siendo condicionales es importante: la arquitectura no fuerza una herramienta, un banco de ejercicios, ni una verificación numérica donde no aplican.

---

## 4. La plantilla de síntesis (el schema fijo, con dos variantes)

Vive como skill (`plantilla-sintesis/SKILL.md`) para que el redactor la consulte, no como texto suelto en un prompt — así es versionable y auditable. Con la segunda fuente que pasaste, la plantilla deja de ser puramente lineal: el "testing" y los prompts generativos ya no van solo al final, van **incrustados dentro** del marco teórico, en cada bloque/subtema.

**Núcleo (siempre presente, con o sin herramienta):**
```
1. Motivación (oración temática) — demuele explícitamente el Obstáculo de Cognición
                                    Funcional (perfil-academico, dim.3-8): plantea el
                                    problema/necesidad física real ANTES de cualquier
                                    fórmula, en primera persona narrativa, anclado en
                                    algo relevante para VOS (dim.3-10, no genérico)
2. Mapa de fuentes                — qué trae cada fuente, dónde coinciden, dónde
                                    divergen o usan notación distinta

3. Marco teórico, por BLOQUES (se repite esta micro-estructura por cada subtema, no una
   sola vez para todo el tema):
   3.a  Definición/fórmula del bloque — notación explícita de qué autor la usa así.
        Si existe una alternativa de diseño descartada o un método competidor,
        se compara explícitamente el trade-off (demuele el Obstáculo de Ventaja,
        dim.3-9) — nunca se presenta la solución elegida como si fuera la única
   3.b  Prompt generativo incrustado  — UNA de: reformular con tus palabras / pregunta
                                        elaborativa "¿por qué aplica acá y no en el otro
                                        caso?" / conexión con lo que ya sabías
   3.c  Micro-chequeo (adjunct questions) — 2 a 3 preguntas cortas de desarrollo,
                                             colocadas INMEDIATAMENTE DESPUÉS del
                                             fragmento (nunca antes), sobre ESE
                                             bloque puntual

4. Ejemplo resuelto — según nivel de expertise en ESE tema (perfil-academico):
   4 (antes del umbral, novato en el tema) — Instrucción explícita → Ejemplo
        100%-resuelto en detalle, con TODOS los pasos → Ejercicio guiado.
        Formato narrado como resolución de un obstáculo concreto, no como
        procedimiento frío.
   4 (después del umbral, competencia intermedia ya alcanzada) — orden
        INVERTIDO: Problema/autoevaluación primero → feedback teórico después.
        Además, el detalle de pasos se reduce (fading): no explicitar pasos
        ya consolidados.
   En ambos casos, alternar entre ejemplo 100%-resuelto y ejemplo-parcial
   (el lector completa el último paso o deduce una variable) — nunca un
   solo formato fijo repetido en todo el documento.
   SI vino --estilo <materia> y hay un parcial resuelto de familia compatible
   en banco-ejercicios/<materia>/parciales/: el formato y nivel de detalle de
   ESTE ejemplo se calibra contra esa resolución real (parafraseada, nunca
   copiada literal — ver nota de estilo más abajo).
5. Errores comunes       — anti-patrones, en tono neutro no punitivo (Capa A, 2.1.1-1)
6. Ejercicios, en dos sub-fases:
   6.a  Práctica en bloque — SOLO del tema nuevo, sin intercalar (obligatoria si el
                              tema es nuevo/complejo; se puede omitir si el perfil
                              indica que el procedimiento base ya está asimilado).
                              SI vino --estilo: formato imita el patrón de TP de
                              banco-ejercicios/<materia>/tps/
   6.b  Práctica intercalada — mezcla con conceptos previos de la MISMA familia
                                Y MISMA materia (mapa-estudio.json →
                                conceptos_ya_cubiertos, filtrado por familia Y
                                por materia — nunca cruza conceptos de Física
                                con los de Comunicaciones solo porque una
                                familia se llama parecido), cada reaparición con
                                dificultad o contexto de aplicación mayor al de su
                                última vez; nunca mezcla con conceptos de familia no
                                relacionada — ahí no hay beneficio de discriminación.
                                SI vino --estilo: formato imita el patrón de parcial
                                (multi-familia, menos andamiaje) de esa materia
```

**Nota de estilo — parafraseo, no copia.** Cuando `estilista-ejercicios` calibra contra un parcial real tuyo, extrae la *forma* (estructura del enunciado, cuántos incisos, qué tipo de dato de partida, nivel de detalle de la resolución) pero genera un ejercicio **nuevo**, con datos/contexto distintos — nunca reproduce tu parcial palabra por palabra. Esto no es solo prolijidad: si reutilizás el enunciado idéntico como "ejercicio nuevo para resolver vos mismo", ya sabés la respuesta de memoria (la viste en el parcial real) y se pierde el efecto de recuperación activa que buscamos en toda la Capa A.

**Cola condicional (solo si vino `--herramienta`):**
```
7. Traducción a la herramienta — tabla concepto→elemento (sale de mapeo-conceptos.md)
8. Ejercicio guiado en la herramienta — predicción ANTES de ejecutar/simular/compilar (clave
                                        pedagógicamente: forzar predicción antes de ver el resultado
                                        es lo que genera el efecto de aprendizaje, no solo mirarlo)
```

Dos cambios importantes respecto a la versión anterior de esta plantilla:
- **El "Chequeo de comprensión" dejó de ser una sección única al final** — se distribuyó como micro-chequeo (3.c) dentro de cada bloque teórico, porque el testing effect es más fuerte distribuido que concentrado.
- **El paso 6 ahora exige explícitamente mirar `mapa-estudio.json`** para traer ejercicios de temas previos — esto es lo que vuelve operativo el interleaving, en vez de dejarlo como una intención declarada nada más.

El orden general sigue fuentes→teoría(con testing incrustado)→ejemplo narrado→errores→intercalado→(herramienta), que es el que minimiza carga cognitiva y maximiza retención según la Capa A. El paso 2 (mapa de fuentes) sigue siendo necesario cuando combinás, por ejemplo, FEC de Lin & Costello con un paper de Viterbi: el documento deja explícito qué formalismo estás usando y por qué, no diluye las dos voces en una sola sin atribución.

---

## 5. Quality gate automático (hooks)

`hooks/hooks.json` puede disparar `scripts/rubric_check.py` automáticamente cada vez que se escribe un archivo de apunte (evento `PostToolUse` sobre `Write`), verificando mecánicamente cosas que un LLM se puede saltear por descuido:

```json
{
  "PostToolUse": [{
    "matcher": "Write",
    "hooks": [{
      "type": "command",
      "command": "python3 ${CLAUDE_PLUGIN_ROOT}/scripts/rubric_check.py \"$FILE_PATH\"",
      "timeout": 30
    }]
  }]
}
```

`rubric_check.py` valida cosas simples y objetivas (no reemplaza al `critico-calidad`, lo complementa): que existan las 6 secciones del núcleo (+2 más si vino `--herramienta`), que cada bloque teórico (3.a) tenga sus micro-chequeos asociados (3.c, 2-3 preguntas, posicionadas después del fragmento), que "Ejercicios" (6) tenga la sub-fase 6.a antes que 6.b cuando el tema es nuevo, que los conceptos traídos en 6.b pertenezcan a la misma `familia` que algún concepto del tema actual (no cualquier concepto de `conceptos_ya_cubiertos` al azar), que el "mapa de fuentes" mencione explícitamente cada fuente pasada por `--fuentes`, y que no haya texto copiado literal de más de N palabras de ninguna fuente.

### 5.1 Verificación numérica — doble propósito (control interno + herramienta para VOS)

Esto responde directo a un requisito tuyo: **nada se entrega hasta que esté verificado**, y en materias con resultado calculable (física, señales, cualquier ejercicio con número de respuesta), la verificación no puede ser "el LLM revisa su propia cuenta" — necesita un chequeo independiente.

`verificar_ejercicio.py` (invocado por el agente `verificador-numerico`) resuelve cada ejercicio generado usando el motor de cálculo correspondiente (sympy/numpy según el tipo de problema) de forma completamente independiente del texto que escribió `redactor-pedagogico`, y compara resultados. Si no coinciden, `critico-calidad` rechaza el borrador y vuelve al redactor — nunca se entrega una síntesis con un ejercicio sin verificar cuando el ejercicio es de tipo numérico.

**La parte que agregaste vos y que vale la pena resaltar como principio de diseño:** el script no queda enterrado como herramienta interna del pipeline — se entrega también como archivo aparte al usuario (`verificar_ejercicio.py`, copiado junto a la síntesis en `/mnt/user-data/outputs/`), para que vos mismo puedas correrlo sobre tus propias resoluciones y aprender a chequear resultados sin depender de que alguien (o algo) te confirme si estás bien. Esto es coherente con toda la Capa A: un chequeo automático que se queda oculto solo te ahorra trabajo; uno que te entregan como herramienta te enseña una habilidad de verificación que te sirve más allá de este documento puntual.

---

## 6. Estado persistente: `mapa-estudio.json`

Esto es lo que le falta a un enfoque "prompt suelto" y es imprescindible si vas a generar muchas síntesis con el tiempo:

```json
{
  "sintesis_generadas": [
    {
      "tema": "Decodificadores FEC",
      "materia": "comunicaciones-digitales",
      "fecha": "2026-08-04",
      "fuentes": ["libro-fec-lin-costello", "paper-viterbi-1967"],
      "herramienta": "systemverilog",
      "estado": "aprobado"
    }
  ],
  "temas_pendientes": ["Códigos LDPC", "Turbo codes"],
  "secuencia_sugerida": ["...", "..."],
  "conceptos_ya_cubiertos": [
    {
      "concepto": "distancia de hamming",
      "materia": "comunicaciones-digitales",
      "familia": "métricas de codificación",
      "ultima_dificultad": "básica",
      "veces_reaparecido": 0
    },
    {
      "concepto": "algoritmo de viterbi",
      "materia": "comunicaciones-digitales",
      "familia": "decodificación de secuencias",
      "ultima_dificultad": "básica",
      "veces_reaparecido": 0
    }
  ],
  "version_perfil_usada": "2026-07-20"
}
```

Cada concepto ahora guarda su `familia` (para que el redactor solo intercale contra conceptos de la misma familia, criterio de Goldstone) y su `ultima_dificultad` + `veces_reaparecido` (para que cada reaparición suba el nivel en vez de repetir el mismo ejercicio). Sin estos dos campos, "intercalar" quedaría reducido a mezclar al azar — que la fuente aportada indica explícitamente que no funciona si los conceptos no compiten por la misma familia de solución.

Además de esto, sirve para tres cosas más: **espaciado** (saber cuándo retomar un tema ya visto), evitar que el agente redacte dos síntesis que se pisan, y **detectar cuándo tu perfil cambió** (`version_perfil_usada`) para saber si una síntesis vieja quedó desactualizada en calibración y conviene regenerarla.

---

## 7. Flujo completo, con los dos casos de uso que mencionaste

**Caso con herramienta (FEC → SystemVerilog):**
```
1. Vos: /setup-perfil
   → una sola vez (o cuando cambie tu formación): crea skills/perfil-academico/

2. Vos: /nueva-fuente "lin_costello_error_control_coding.pdf"
        /nueva-fuente "viterbi_1967.pdf"
   → corre book-to-skill en modo technical sobre cada una → crea
     skills/fuentes/libro-fec-lin-costello/ y skills/fuentes/paper-viterbi-1967/

3. Vos (una sola vez, a mano con skill-creator): armás
   skills/herramientas/herramienta-systemverilog/ con mapeo-conceptos.md
   (ej: "polinomio generador" → "parámetro GENERATOR_POLY del módulo decoder.sv")

4. Vos: /generar-sintesis "Decodificadores convolucionales" \
        --fuentes libro-fec-lin-costello,paper-viterbi-1967 \
        --herramienta systemverilog
   → dispara la cadena completa de subagentes de la sección 3
   → hook valida automáticamente al escribir
   → se actualiza mapa-estudio.json
```

**Caso sin herramienta (SoC, puramente teórico):**
```
1. Vos: /nueva-fuente "soc_design_paper_A.pdf"
        /nueva-fuente "soc_design_book_B.pdf"

2. Vos: /generar-sintesis "Arquitecturas de interconexión en SoC" \
        --fuentes soc-design-paper-A,soc-design-book-B
   (sin --herramienta: el pipeline salta mapeador-herramienta y la plantilla
    usa solo el núcleo de 6 secciones, sin la cola de traducción/ejercicio)
```

**Caso con banco de ejercicios (Física, ciencia dura con TPs y parciales reales):**
```
1. Vos: /nueva-fuente "resnick_fisica_2.pdf"

2. Vos: /nuevo-banco-ejercicios "tp3_ondas.pdf,tp4_ondas.pdf" fisica-2 --tipo tp
        /nuevo-banco-ejercicios "parcial1_2025.pdf,parcial2_2025.pdf" fisica-2 --tipo parcial
   → extrae patrón de forma (no contenido teórico) → crea/actualiza
     skills/banco-ejercicios/fisica-2/

3. Vos: /generar-sintesis "Ondas estacionarias" \
        --fuentes resnick-fisica-2 \
        --estilo fisica-2
   → estilista-ejercicios calibra 6.a contra tus TPs reales y 6.b (+ el
     ejemplo resuelto del paso 4, si hay parcial de familia compatible)
     contra tus parciales reales — parafraseado, con datos nuevos
```

**Revisión posterior:**
```
Vos: /revisar-sintesis sintesis/decodificadores-convolucionales.md
   → vuelve a correr solo critico-calidad, útil si editaste la síntesis a mano después
```

---

## 8. Roadmap de implementación sugerido (de menor a mayor complejidad)

| Fase | Qué armar | Por qué primero |
|---|---|---|
| 1 | `pedagogia-cognitiva` (fusión de tus libros/papers de aprendizaje) + `perfil-academico` a mano | Base que se reutiliza en TODAS las síntesis futuras, cero riesgo |
| 2 | 2-3 skills de `fuentes/` sobre un tema que te interese ya (vía book-to-skill) | Validás que la extracción preserva bien fórmulas/notación antes de escalar |
| 3 | `plantilla-sintesis` como skill + generar UNA síntesis a mano combinando 2 fuentes | Validás que la conciliación entre fuentes y la calibración por perfil funcionan antes de automatizar nada |
| 4 | (si aplica) `herramienta-<nombre>/mapeo-conceptos.md` a mano | Es la pieza sin la cual la cola condicional de la plantilla no tiene sentido |
| 5 | (si aplica) `banco-ejercicios/<materia>/` con 1-2 TPs y 1-2 parciales tuyos | Validás que el patrón de estilo se puede extraer bien antes de automatizarlo |
| 6 | Subagentes separados (conciliador, calibrador, mapeador, estilista, redactor, crítico) | Recién acá conviene dividir, cuando ya sabés qué necesita cada paso |
| 7 | `hooks/rubric_check.py` | Automatizás el control de calidad una vez que sabés qué reglas importan de verdad |
| 8 | `mapa-estudio.json` + comando de secuenciación | Última capa, solo tiene sentido cuando ya tenés varias síntesis generadas |

Empezar por la Fase 5-6 sin haber hecho 1-3 a mano es el error típico de sobre-ingeniería en frameworks de agentes: armás la orquestación antes de saber qué reglas de calidad realmente necesitás, y terminás iterando la arquitectura en vez del contenido.
