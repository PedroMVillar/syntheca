# Guía de uso — syntheca

Esta guía asume que ya instalaste el plugin (`/plugin install ./syntheca` dentro de Claude Code). Ver el [README](../README.md) para requisitos.

## 0. Antes de arrancar

Verificá que tenés Python 3 y `pdflatex` disponibles en el entorno donde corre Claude Code — sin esto, la ingesta de fuentes y la compilación de síntesis no funcionan correctamente.

```bash
python3 --version
pdflatex --version
```

## 1. Perfil académico

```
/setup-perfil
```

Se completa una vez, con las 4 dimensiones (competencias, motivación/anclajes, obstáculos, secuenciación). El nivel de andamiaje (Dimensión 4) **no es un valor único** — se completa por tema/familia específico, y para una materia que recién vas a cursar, lo correcto es dejarlo como "sin diagnosticar", no asumir nivel.

## 2. Cronograma/temario de la materia (opcional pero recomendado)

```
/cargar-programa <materia>
```

Pegá o adjuntá el cronograma en el mismo mensaje. El comando extrae los temas y, si el programa especifica qué temas entran en cada parcial/final, también carga esa agrupación (útil más adelante para generar exámenes de prueba). Te muestra la lista extraída antes de guardar nada — confirmá antes de que se aplique.

## 3. Bibliografía — un comando por fuente

```
/nueva-fuente <archivo.pdf>
```

Cada libro/paper es una skill independiente, nunca se fusionan entre sí (a diferencia de `pedagogia-cognitiva`, que sí se fusiona porque es la única capa universal). Recomendación: arrancá con la bibliografía principal + la complementaria que sepas que vas a necesitar para el primer tema — no hace falta ingestar todo de entrada.

**Tip para muchos archivos:** ponelos en `_inbox/` y pedile a Claude en un solo mensaje que procese como fuente cada PDF de esa carpeta.

## 4. Herramienta de la materia (opcional)

```
/nueva-herramienta <nombre> --tipo simulador|lenguaje|diagrama-arquitectura
```

Solo si la cátedra usa un simulador, un lenguaje de descripción de hardware, o herramientas de diseño sin ejecución. Se arma a mano (no hay libro fuente) — empezá con 5-10 conceptos centrales en `mapeo-conceptos.md` e ilo ampliando con el tiempo.

## 5. TPs, parciales y finales reales (opcional pero muy recomendado)

```
/nuevo-banco-ejercicios <archivos-separados-por-coma> <materia> --tipo tp
/nuevo-banco-ejercicios <archivos-separados-por-coma> <materia> --tipo parcial
/nuevo-banco-ejercicios <archivos-separados-por-coma> <materia> --tipo final
```

**A diferencia de las fuentes, acá SÍ conviene agrupar varios archivos del mismo tipo en una sola corrida** — lo que se extrae es el patrón de formato de la cátedra (estructura de enunciado, curva de dificultad), y ese patrón se calibra mejor viendo varios ejemplos juntos que uno por uno. Procesá cada `--tipo` por separado para no mezclar sus curvas de dificultad.

## 6. Generá tu primera síntesis

```
/generar-sintesis "<tema>" --materia <slug> --fuentes <a,b,c> [--herramienta x] [--estilo materia] [--fuente-principal x]
```

Recomendación: probá con el primer tema del cronograma antes de terminar de cargar toda la bibliografía complementaria y todos los parciales/finales — así, si algo del resultado no te convence, lo ajustás una sola vez.

## 7. Consultá tu progreso

```
/mapa-estudio [materia]
```

Muestra síntesis generadas, temas pendientes, y conceptos ya cubiertos por familia — sin filtrar por materia, evitá mezclar vistas de materias distintas.

## 8. Revisar una síntesis editada a mano

```
/revisar-sintesis <ruta-al-archivo>
```

Vuelve a correr solo el gate de calidad, sin re-conciliar fuentes ni re-calibrar perfil — útil si tocaste el documento vos mismo después de generarlo.

## Preguntas frecuentes

**¿Necesito reportarle al sistema cómo me fue en cada ejercicio?**
No. El pipeline no mide tu desempeño real — `mapa-estudio.json` trackea qué *contenido* ya se generó (para el interleaving), no cómo te fue a vos resolviéndolo. Es un flujo de "generar y listo", sin pasos obligatorios de feedback tuyo.

**¿Puedo correr esto en el chat de claude.ai en vez de Claude Code?**
Técnicamente sí (Claude puede simular el rol de cada agente leyendo sus instrucciones), pero **se pierde la persistencia** — no queda instalado como sistema reutilizable entre sesiones. Para uso real y continuo, Claude Code es el entorno pensado.

**¿Por qué separar fuentes, TPs y parciales en comandos distintos?**
Cada uno extrae algo distinto: las fuentes aportan contenido teórico (por eso van una por una, preservando su voz individual); los TPs/parciales/finales aportan patrón de forma (por eso conviene verlos juntos, para que el patrón sea representativo).
