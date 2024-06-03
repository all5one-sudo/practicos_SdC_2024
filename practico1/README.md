# Trabajo Práctico 1: rendimiento

## Introducción

En el siguiente informe se desarrolla el trabajo práctico 1, correspondiente a la asignatura Sistemas de Computación. El objetivo principal es analizar el rendimiento de los computadores, de forma de poder cuantificar el mismo. Para ello, se utilizan benchmarks. Para medir las performances de los computadores de los integrantes del grupo, se correrán algunos de ellos, en este caso serán:

- Benchmarks de terceros para tomar decisiones de hardware
- Herramientas (GPROF y perf) para medir performance de código

Los resultados de time profiling realizados serán analizados y explicados. 

Finalmente, para cerrar el concepto de rendimiento y su cuantificación, se analizará qué pasa al overclockear un microcontrolador Raspberry Pi Pico que ejecuta un simple programa de sumas de números.

## Marco teórico

### Benchmarking

Al evaluar la eficacia de un ordenador, surge la cuestión de cómo medir su rendimiento. Esto implica la evaluación de cada uno de sus componentes para identificar áreas de mejora, pero especialmente se enfoca en optimizar el rendimiento global del sistema. En consecuencia, el indicador más confiable suele ser el tiempo de ejecución.

Sin embargo, surge la interrogante sobre qué estándar utilizar para medir este tiempo de ejecución. Para garantizar un rendimiento óptimo del sistema, las pruebas deben realizarse con programas reales o similares a los que se ejecutarán en condiciones de operación normales. Posteriormente, se comparan los tiempos resultantes con los de computadoras similares para determinar si se está alcanzando un rendimiento competitivo en el mercado actual. Para comparar el rendimiento entre distintas máquinas, se emplea un benchmark como referencia.

Un benchmark es un conjunto de programas de prueba o programas reales que sirven para medir el rendimiento de un componente concreto o de una computadora en su conjunto, mediante la comparación de los tiempos de ejecución obtenidos de esos programas de prueba con respecto a otras máquinas similares.

#### Tipos de benchmarks

Existen diferentes tipos de benchmarks, dependiendo de las características de la computadora a evaluar y de la sofisticación del mecanismo utilizado.

- Programas de juguete o microbenchmark: consisten en pequeños fragmentos de código con entre 10 y 100 líneas de código que se utilizan para medir una determinada característica de la computadora. Ejemplos de esto son: Java Micro Benchmark, Puzzle, Quicksort, criba de Erastótenes.
- Benchmarks sintéticos: se trata de programas de prueba que simulan programas reales en carga de trabajo y reparto de instrucciones, sirven más que nada para medir el rendimiento de componentes concretos o del PC en general. Ejemplos son: Whetstone, Dhrystone
- Benchmarks de kernel: consisten en un fragmento de código extraído de un programa real. La parte escogida es la más representativa, y por tanto, la que más influye en el rendimiento del sistema para ese determinado software (como puede ser por ejemplo el kernel de Linux).
- Programas reales: son los más utilizados hoy en día. Son programas reales que son ejecutados con un conjunto de datos reducido para no alargar su ejecución. Se tienen como ejemplos los de la familia SPEC (clasificados en SPECint y SPECfp, según operen con números enteros o reales).
- Otros: existen numerosos tipos de benchmarks para probar características y componentes específicos de un ordenador, como pueden ser benchmarks de entrada/salida, de bases de datos, paralelos. Ejemplos son: Linpack, Livermoore, NAS y PARSEC.

##### Famila SPEC

SPEC (Standard Performance Evaluation Corporation, por sus siglas en inglés) es una asociación que fue creada por los mayores fabricantes de computadoras del mundo (IBM, HP, INTEL, SUN, etc.) Se creó con el objetivo de definir unos benchmarks que consistieran en programas reales y que pudieran ser utilizados como referentes o estándares para todas las marcas. Los benchmarks SPEC sirven para medir el rendimiento de componentes concretos o de microprocesadores en general.

### Rendimiento

#### Definición

El rendimiento de una computadora se refiere a la cantidad de trabajo que puede realizar un sistema informático en un período de tiempo dado. Este rendimiento puede variar según el contexto y puede incluir uno o más de los siguientes aspectos:

- Tiempo de respuesta reducido para una tarea específica.
- Alto throughput, es decir, una alta tasa de procesamiento de trabajo.
- Utilización baja de recursos computacionales.
- Alta disponibilidad del sistema informático o de la aplicación.
- Capacidad rápida (o altamente eficiente) de compresión y descompresión de datos.
- Amplio ancho de banda para la transferencia de datos.
- Tiempos cortos de transmisión de datos.

