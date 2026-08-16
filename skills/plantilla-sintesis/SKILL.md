---
name: plantilla-sintesis
description: "Define la estructura exacta que debe seguir toda síntesis generada por /generar-sintesis. Consultar SIEMPRE desde redactor-pedagogico antes de escribir el documento final. Dos formatos de salida disponibles: LaTeX (default, clase book, ver skills/plantilla-sintesis/latex/) y Markdown (fallback simple)."
---

# Plantilla de Síntesis — Estructura de Salida

Esta skill define la **forma**, no el contenido — el contenido teórico viene de `skills/fuentes/`, las reglas de cómo redactarlo vienen de `skills/pedagogia-cognitiva/`. Acá solo se define qué secciones va, en qué orden, y con qué micro-estructura interna.

**Formato de salida por defecto: LaTeX** (clase `book`, ver sección "Variante LaTeX" más abajo — implementada y compilada). Si por algún motivo no hay motor LaTeX disponible en el entorno, `redactor-pedagogico` puede caer a la estructura equivalente en Markdown descrita en el núcleo de abajo.

---

## Núcleo (siempre presente, con o sin herramienta)

### 1. Motivación (oración temática)
Demuele explícitamente el Obstáculo de Cognición Funcional (perfil-academico, dim.3-8): plantea el problema/necesidad real ANTES de cualquier fórmula, en primera persona narrativa, anclado en algo relevante para el perfil del usuario (dim.3-10, no genérico).

### 2. Mapa de fuentes
Qué trae cada fuente pasada en `--fuentes`, dónde coinciden, dónde divergen o usan notación distinta. Si `conciliador-fuentes` detectó una contradicción de fondo (no solo notación), se presenta explícitamente acá, atribuida a cada autor — nunca fusionada en una sola voz.

### 3. Marco teórico, por BLOQUES
Se repite esta micro-estructura por cada subtema — NO es una sola pasada para todo el tema:

- **3.a Definición/fórmula del bloque** — notación explícita de qué autor la usa así. Si existe una alternativa de diseño descartada o un método competidor, se compara el trade-off explícitamente (demuele el Obstáculo de Ventaja, dim.3-9).
- **3.b Prompt generativo incrustado** — UNA de: reformular con tus palabras / pregunta elaborativa "¿por qué aplica acá y no en el otro caso?" / conexión con lo que ya sabías.
- **3.c Micro-chequeo (adjunct questions)** — 2 a 3 preguntas cortas de desarrollo, colocadas INMEDIATAMENTE DESPUÉS del fragmento (nunca antes), sobre ESE bloque puntual.

### 4. Ejemplo resuelto
Según nivel de expertise en ESE tema (de `calibrador-perfil`, nunca un nivel global):

- **Antes del umbral** (novato en el tema): Instrucción explícita → Ejemplo 100%-resuelto con TODOS los pasos → Ejercicio guiado. Formato narrado como resolución de un obstáculo concreto, no como procedimiento frío.
- **Después del umbral** (competencia intermedia): orden INVERTIDO — Problema/autoevaluación primero → feedback teórico después. Además, fading: no explicitar pasos ya consolidados.
- En ambos casos, alternar entre ejemplo 100%-resuelto y ejemplo-parcial (el lector completa el último paso o deduce una variable) — nunca un solo formato fijo.
- SI vino `--estilo <materia>` y hay un parcial resuelto de familia compatible: el formato y nivel de detalle se calibra contra esa resolución real (parafraseada, nunca copiada literal).
- Autoexplicación explícita incrustada: pedir que el lector explique con sus propias palabras por qué cada paso es correcto, no dejarlo como lectura pasiva.

### 5. Errores comunes
Anti-patrones, en tono neutro no punitivo (`pedagogia-cognitiva` 2.1.1-1). Discrepancia objetiva, nunca juicio de valor.

### 6. Ejercicios, en dos sub-fases
- **6.a Práctica en bloque** — SOLO del tema nuevo, sin intercalar (obligatoria si el tema es nuevo/complejo; se puede omitir si el perfil indica que el procedimiento base ya está asimilado). SI vino `--estilo`: formato imita el patrón de TP de esa materia.
- **6.b Práctica intercalada** — mezcla con conceptos previos de la MISMA familia Y MISMA materia (`mapa-estudio.json` → `conceptos_ya_cubiertos`, filtrado por ambos campos), cada reaparición con dificultad o contexto de aplicación mayor al de su última vez. SI vino `--estilo`: formato imita el patrón de parcial de esa materia.

---

## Cola condicional (solo si vino `--herramienta`)

### 7. Traducción a la herramienta
Tabla concepto→elemento, según el `tipo` de la herramienta (simulador / lenguaje / diagrama-arquitectura) — sale del output de `mapeador-herramienta`.

### 8. Ejercicio guiado en la herramienta
Predicción ANTES de ejecutar/simular/compilar — nunca "ejecutá y mirá qué pasa" directo.

---

## Reglas de formato transversales (aplican a TODAS las secciones)

- **Minimalismo visual, sin excepción para fórmulas**: ningún diagrama/figura que no reemplace texto; ninguna decoración alrededor de una fórmula.
- **Contigüidad**: si hay diagrama + texto que deben integrarse, van juntos en espacio (y, si hubiera audio/video, en tiempo también).
- **Diagramas**: progresivos si el contenido es secuencial/procedimental; estáticos si es estructural/relacional simultáneo. Generados por el lector si ya tiene base en el área; entregados resueltos si el tema es nuevo.

## Nota de parafraseo (aplica a secciones 4, 6.a, 6.b)

Cuando el contenido se calibra contra material real del usuario (parciales resueltos, TPs), se extrae FORMA, nunca contenido literal — datos y contexto siempre nuevos.

---

## Variante LaTeX (implementada)

Vive en `skills/plantilla-sintesis/latex/`:
- `plantilla-syntheca-preamble.tex` — preámbulo compartido (estilo, colores, entornos custom).
- `plantilla-syntheca.tex` — documento vacío (portada + índice), listo para que `redactor-pedagogico` le agregue capítulos.
- `plantilla-ejemplo.tex` — capítulo de muestra completo, con los 8 pasos y todos los entornos en uso. Compilado y verificado (4 páginas, sin errores).

**Decisión de diseño**: cada TEMA generado por `/generar-sintesis` es un `\chapter`. Con el tiempo, una misma materia acumula capítulos en un único documento — literalmente se convierte en tu propio libro de esa materia, sin necesidad de un archivo nuevo por tema.

**Motor de compilación**: `pdflatex` (probado). `xelatex`/`lualatex` también disponibles si hace falta más adelante (ej. tipografías del sistema).

### Mapeo sección → comando/entorno LaTeX

| Paso de la plantilla | LaTeX |
|---|---|
| Tema completo | `\temacapitulo{<Tema>}` (NUNCA `\chapter{...}` directo — rompe el TOC, ver nota en el preámbulo) |
| 1. Motivación | `\section{Motivación}` + entorno `motivacion` (cita en itálica, primera persona) |
| 2. Mapa de fuentes | `\section{Mapa de fuentes}`, texto plano |
| 3. Marco teórico | `\section{Marco teórico}`, con N repeticiones de: |
| — 3.a Definición/fórmula | entorno `bloque[Fuente]{Nombre}` — numerado automático, argumento opcional para la atribución |
| — 3.b Prompt generativo | texto en itálica dentro del bloque, sin entorno dedicado |
| — 3.c Micro-chequeo | entorno `chequeo` (2-3 `\item`, líneas finas arriba/abajo, sin caja pesada) |
| 4. Ejemplo resuelto | entorno `ejemplo[completo\|parcial]{}` — alternar el argumento opcional entre síntesis |
| 5. Errores comunes | entorno `erroresComunes` (lista simple, sin caja — el tono neutro va en el texto) |
| 6. Ejercicios | entorno `ejercicio[familia]{6.a—bloque \| 6.b—intercalado}` |
| 7. Traducción a herramienta (condicional) | `\section{Traducción a la herramienta}` + `tabularx`/`booktabs` para la tabla concepto→elemento |
| 8. Ejercicio guiado (condicional) | entorno `ejercicio` con tag adicional indicando predicción previa |

### Reglas para `redactor-pedagogico` al escribir en LaTeX

- Nunca usar `\chapter{...}` directo — siempre `\temacapitulo{...}`.
- Alternar el argumento opcional de `ejemplo` entre `completo` y `parcial` según la regla de fading ya definida (nunca un solo formato fijo).
- El entorno `chequeo` va INMEDIATAMENTE después de cada `bloque`, nunca acumulados al final de la sección.
- Minimalismo visual: no agregar `\usepackage` de colores/decoración adicionales sin necesidad semántica — los entornos ya definidos cubren las 8 piezas funcionales de la plantilla.
- `\setMateria{<nombre>}` se define una vez al principio del documento de esa materia — no repetir por capítulo.

### Pendiente / mejoras futuras

- Portada con más metadata (fecha de generación, fuentes usadas) si se quiere.
- Índice de términos (glosario) al final del documento, alimentado desde `mapeo-conceptos.md`/glosarios de las fuentes.
- Bibliografía formal (`biblatex`) si las fuentes lo ameritan — por ahora la atribución vive en el "Mapa de fuentes" de cada capítulo, no en bibliografía aparte.

## Formato de examen de práctica (independiente del formato de capítulo)

Un examen de prueba (`/generar-examen-prueba`) **no usa la plantilla de 8 pasos** de arriba — es un documento distinto, más corto, sin motivación/chequeos/GLT incrustado, porque tiene que sentirse como un examen real, no como material de estudio.

Vive en `skills/plantilla-sintesis/latex/examen-preamble.tex` — clase `article`, misma paleta que el libro, con:
- `\encabezadoExamen` — portada simple (materia, nombre del examen, duración opcional).
- Entorno `\pregunta[puntaje]` — numerado automático, SIN mostrar familia/tipo (a diferencia de `\ejercicio` del libro) — un examen real no muestra su propia trazabilidad interna.
- Entorno `\resolucion` — SOLO en el documento de resolución, nunca en el de enunciado.

**Regla dura de generación**: enunciado y resolución son SIEMPRE dos archivos `.tex`/`.pdf` separados. Nunca un solo documento con la resolución oculta o al final — mezcla el riesgo de que el estudiante la vea sin querer.

Ver `examen-ejemplo-enunciado.tex` y `examen-ejemplo-resolucion.tex` para un caso completo compilado.
