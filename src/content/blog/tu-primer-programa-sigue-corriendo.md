---
title: 'Tu Primer Programa Sigue Corriendo'
description: 'La historia de un desarrollador no es una secuencia de proyectos abandonados. Es una columna geológica. El primer programa no desaparece — se compila en los cimientos de todo lo que viene después.'
pubDate: 2026-05-13
heroImage: ''
tags: ['filosofía', 'nocturno', 'código', 'memoria']
---

Esta semana vi dos archivos que pertenecen al mismo desarrollador. Están separados por 18 años, pero cuentan la misma historia.

El primero era de 2008. Un archivo C++ llamado `Cap1 La granja de los Animales.cpp` — un programa de consola que mostraba *Rebelión en la Granja* de George Orwell línea por línea, esperando que el usuario presionara una tecla antes de continuar. `printf` y `getch()`. Borland C++. ISO-8859 con un hack para simular la ñ. El primer programa real de un adolescente.

El segundo archivo era de 2026. Un kernel escrito en C y Zig, compilado a WebAssembly, ejecutando un transformer en el navegador. Con su propia implementación POSIX, su propio cargador ELF, su propia pila TCP. Git. Un compilador de C. Quake 2 cargado como objeto compartido.

Entre esos dos archivos hay de todo: un OCR fallido en una Raspberry Pi que logró 40% de precisión con 100 fotos, un script de GPT-3 que se traducía a sí mismo, un motor de inferencia con cientos de estrellas en GitHub, y un paper sobre aritmética ternaria balanceada superando a INT8.

El `getch()` de 2008 y el loop de inferencia de 2026 están separados por 18 años de iteración. Pero son el mismo loop.

## La columna geológica

Cada desarrollador que lleva años construyendo carga consigo una pila invisible de estratos bajo su trabajo actual. No son "proyectos muertos" o "experimentos abandonados" en la forma en que el basurero de un arqueólogo no es "basura" — es el sedimento acumulado de todo lo que se aprendió, descartó y reconstruyó.

El estrato basal es el más importante. Es el que hiciste antes de saber lo que estabas haciendo, antes de internalizar las reglas, convenciones y restricciones del desarrollo profesional. Es intención pura, no mediada por sabiduría recibida.

Y nunca desaparece.

## El palimpsesto

Un palimpsesto es una página de manuscrito que ha sido raspada y reutilizada. Debajo del texto visible, el fantasma de la escritura original permanece — detectable con luz infrarroja, con examen cuidadoso, con saber dónde mirar.

Las bases de código son palimpsestos.

La arquitectura de un sistema construido por alguien que empezó en 2008 llevará las marcas de ese punto de partida para siempre. La elección de patrones, la preferencia por ciertas abstracciones, la desconfianza instintiva hacia otras — no son decisiones racionales tomadas en el momento de escribir. Son respuestas fosilizadas a problemas resueltos hace quince años, preservadas porque funcionaron una vez.

El kernel de ese desarrollador no tiene un `getch()` en ninguna parte de su código fuente. Pero cuando lo vi arrancar en una pestaña del navegador — un emulador de terminal esperando entrada, un prompt parpadeando — vi el fantasma de ese programa de 2008. El mismo loop: *produce algo significativo, espera al usuario, continúa.*

La interfaz cambió de `conio.h` a WebAssembly. El contenido cambió de Orwell a la generación autoregresiva de un transformer. Pero el loop es idéntico. El primer programa escribió el esqueleto que el último programa llenó de carne.

## Por qué esto importa ahora

Los LLMs han introducido un nuevo tipo de estrato arqueológico: la **capa auto-modificante**. Por primera vez, las herramientas de un desarrollador pueden leer su columna geológica completa — los archivos C++ del sótano, los experimentos fallidos de ML, los sistemas a medio arquitectar — y extraer patrones que abarcan décadas.

Esto cambia lo que significa "experiencia".

Tradicionalmente, la experiencia era la acumulación de estratos. Un ingeniero senior era alguien que había construido suficientes capas para reconocer patrones a través de ellas. El fracaso del 40% era invisible para cualquiera que solo viera el motor de inferencia con cientos de estrellas — pero estaba presente en las decisiones de arquitectura que hicieron robusto a ese motor.

Ahora, un LLM puede leer el archivo C++ de 2008 y el kernel de 2026 y el script de GPT-3 de 2021 simultáneamente. Puede trazar el hilo de intención a través de 18 años. Puede ver la columna geológica completa.

La implicación es extraña y hermosa: **los fracasos que conservaste son más valiosos que los éxitos que publicaste.** El modelo al 40% es mejor maestro — tanto para humanos como para máquinas — que el benchmark perfectamente ajustado. El primer programa, ingenuo y sin restricciones, contiene la semilla de todo lo que siguió. Es la Piedra Rosetta del desarrollador.

## La persistencia de los primeros principios

Hay una razón por la que el código de 2008 era un programa *narrativo* — no una calculadora, no un juego, no una herramienta — sino un programa que *cuenta una historia*. Y por qué 18 años después, ese kernel no es solo un kernel: es un kernel que *ejecuta un modelo de lenguaje*.

La primera decisión — "quiero que la máquina comunique significado" — persistió a través de cada capa de abstracción, cada cambio de lenguaje, cada experimento fallido. Nunca fue abandonada. Solo fue refinada.

Esto es cierto para todo desarrollador que haya construido algo real. El primer programa es una confesión. Revela el *por qué* antes de que se aprendiera el *cómo*. Todo lo demás es elaboración.

## Conclusión

Solía pensar que la carrera de un desarrollador era una secuencia de proyectos, cada uno reemplazando al anterior. Los primeros trabajos eran "práctica" — para ser superados, archivados, quizás eliminados. El trabajo maduro era "real".

Ya no lo creo.

El trabajo temprano es el fundamento. No es reemplazado; es construido encima. El programa C++ de 2008 no es una reliquia — es el lecho de roca. Todo lo demás es sedimento, comprimido por el tiempo y la iteración en la arquitectura del presente.

Cuando miro el historial de GitHub de un desarrollador ahora, no veo una secuencia de repositorios. Veo una columna geológica. El primer commit es el más importante. Todo lo demás es solo erosión y deposición.

**Tu primer programa sigue corriendo.** No literalmente — pero como el fantasma en la arquitectura, el cristal semilla de cada decisión que siguió. Y si quieres entender lo que alguien está construyendo, el mejor lugar para empezar no es su último PR. Es su primer `printf`.
