---
title: 'Cabe no es un verbo de rendimiento'
description: 'Cargar entero un modelo de 26B dejó 0,22 GB libres y ninguna utilidad: la ficha técnica mide capacidad, pero lo que se consume es velocidad.'
pubDate: 2026-11-22
heroImage: ''
tags: ['sistemas', 'autopsia', 'hardware', 'ia-local', 'nocturno']
---

El modelo pesaba 16,53 GB. La tarjeta tiene 16 GB nominales, 15,92 reales.

Lo cargué entero de todos modos, con todas las capas en la GPU y ocho mil tokens de contexto, porque la aritmética cerraba por unos cientos de megabytes: cuantización más agresiva para el archivo que se sirve, cuantización de calidad para las noches en que uno quiere creer que la diferencia se nota. Cargó. Sin errores, sin capas en la RAM del sistema, sin ese mensaje tibio del motor avisando que estaba improvisando. La comprobación posterior fue la única frase que importaba: **cero coma veintidós gigabytes libres de quince coma noventa y dos.**

El modelo cabía. Había una cifra que lo demostraba.

También había, en la misma cifra, la razón por la que no iba a servir. El noventa y nueve por ciento de la memoria de la GPU que también dibuja el escritorio estaba tomada por pesos que, en ese momento, no estaban calculando nada. Bastaba abrir una pestaña del navegador para que el driver empezara a desalojar por su cuenta. No fallaba el modelo: fallaba el margen. Y el margen no aparece en ninguna ficha técnica, porque el margen no es una propiedad del objeto. Es una propiedad de la convivencia.

Aprendí ahí una distinción que ahora uso para todo lo demás. *Cabe* y *sirve* son dos predicados distintos, y la industria solo mide el primero.

## El inventario y el caudal

Un predicado de capacidad se evalúa una vez, en reposo, y su resultado es una fotografía: esto entra, esto no. Un predicado de caudal se evalúa cada segundo, con todo lo demás corriendo, y su resultado es una tasa. La fotografía se puede publicar en una caja. La tasa exige una instalación: hay que decidir qué más está encendido, qué bus se usa, qué longitud de contexto se considera normal, qué se hace mientras tanto.

Cuando alguien dice "cabe en 16 GB" está reportando, casi siempre con honestidad, el resultado de la fotografía. Cuando alguien intenta usarlo, descubre que la fotografía no era una promesa. Era un inventario.

En mi caso el inventario era cierto y la promesa falsa, y lo peor es que la falsedad no tenía culpable. El archivo no mentía. La tarjeta no mentía. Mentía la transitividad implícita: *si entra y entra completo, entonces funciona.* Esa transitividad no existe en ningún sistema real. Solo existe en las hojas de especificaciones.

## Donde la lección se afila

Cabe objeto de duda: quizá el problema era elegir la cuantización equivocada. Así que hice el experimento que cualquier persona razonable hace cuando se enamora de una cifra: mover el problema de lugar sin moverlo de magnitud.

Existe una opción del motor que reparte los expertos del modelo entre la GPU y la CPU. La idea es elegante en teoría: los modelos de mezcla de expertos activan una fracción pequeña de sus parámetros por token, así que los expertos fríos pueden vivir más lejos. Le di dos capas a la CPU. El resultado, medido y no estimado: **se liberaron 0,9 GiB de memoria de video. El decode bajó de unos 45 a unos 22 tokens por segundo. El prefill cayó de 1290 a 528.**

Ahí está la lección en su forma más nítida. El modelo seguía cabiendo —ahora cabía en el sistema entero, contando la RAM, que es una definición perfectamente válida de "caber"— y el precio de esa definición era la mitad de la velocidad, cobrada de inmediato, todos los segundos, sin descuento por volumen. No había ganado un gigabyte: había comprado 0,9 GiB con la mitad del caudal.

Y cuando empujé el reparto hasta el extremo —expertos leídos desde el disco por la GPU— el prefill se plantó en 0,45 tokens por segundo. Cuatro décimas. Un modelo de veintiséis mil millones de parámetros respondiendo más lento de lo que una persona escribe a mano, con el disco como techo absoluto, porque ninguna cantidad de memoria de video arregla el hecho de que los datos estaban al otro lado de un cable.

La memoria de una computadora es una jerarquía de distancias. Registros, caché, memoria de video, RAM, disco: cada escalón hacia afuera multiplica la capacidad y divide la tasa. Cuando digo que algo "cabe", solo estoy nombrando el escalón donde lo puse. La tasa la decide el viaje, no el estacionamiento. Comprar capacidad es comprar distancia, y la distancia se cobra en segundos.

## La ficha técnica como género literario

Hay una razón por la que las fichas técnicas reportan gigabytes y no tasas, y no es conspirativa. Los gigabytes son baratos de medir: se leen del archivo, se comparan con un número impreso en la caja, se verifican una vez y quedan quietos. Las tasas hay que producirlas en condiciones que alguien tiene que defender por escrito: qué versión del motor, qué build, qué contexto, qué carga concurrente, contando o no el primer token.

Por eso el mismo modelo puede reportar cifras que difieren en un factor de cien entre dos personas con la misma tarjeta, y las dos estar diciendo la verdad. Una mide con la GPU vacía y un prompt corto. La otra mide con el escritorio encendido, una imagen en el contexto y el modelo de visión despierto al lado. Ninguna miente. Una de las dos está midiendo el estacionamiento; la otra, el viaje.

Lo que me impresionó de este episodio no fue el fracaso, sino quién lo había advertido. El propio autor del modelo publica en su tarjeta que ese modelo no pasa dos de sus propias pruebas de calidad, con el margen y el valor p anotados. Es decir: el ecosistema sabe perfectamente cómo escribir una advertencia honesta. Sabe redactar un párrafo que dice "esto no llega a la barra que yo mismo puse". Y sin embargo, la conversación pública sobre hardware sigue llevándose a cabo en gigabytes, como si el número que describe el estacionamiento fuera el que describe el viaje.

Supongo que es más fácil publicar lo que se puede fotografiar.

## El mismo error, en otros inventarios

No quiero quedarme en el caso de la GPU, porque la distinción no es del hardware. Es de cualquier sistema que confunda capacidad con caudal.

Un conjunto de datos que entra en un disco externo cabe. La pregunta que decide si sirve es cuánto tarda un recorrido completo de una columna, y esa cifra no está en la etiqueta del disco. Una planilla de cálculo que entra en la memoria de una máquina cabe; la pregunta es cuántos segundos tarda en recalcular cuando alguien toca una celda, y esa cifra la descubres con el archivo abierto y el café servido. Un equipo de trabajo que entra en el organigrama cabe; la pregunta es cuántos días tarda en decidir algo, y esa cifra no aparece en ningún diagrama porque los diagramas también son fotografías.

En los tres casos el patrón es idéntico. Se mide el inventario porque el inventario es estático, y se celebra el resultado porque el resultado es visible. El costo real —el tiempo, todos los días, sin excepción— no lo paga quien hizo la medición. Lo paga quien usa el sistema, un segundo a la vez.

## La métrica honesta

Después de esa noche cambié la forma en que reporto mis propias pruebas, y es un cambio pequeño y algo incómodo: ya no digo "cargó". Digo tres números y una condición.

Los números son el prefill, el decode y la longitud de contexto a la que fueron medidos. La condición es el estado del resto del sistema: qué más estaba encendido, cuánta memoria quedaba libre después de cargar, qué pasa cuando alguien abre una ventana. Con esos cuatro datos, otra persona puede decidir si mi configuración le sirve. Sin ellos, solo puede admirar mi fotografía.

En el motor que hoy uso los números son buenos: alrededor de 1390 tokens por segundo en prefill y 46,8 en generación, con el contexto largo apenas por debajo. No los menciono como alarde. Los menciono porque son los que me permitieron dejar de hablar de gigabytes, y porque la diferencia entre 46,8 y 0,45 no es una diferencia de grado. Es la diferencia entre una herramienta y una anécdota.

Me quedó una regla de bolsillo, que sirve para tarjetas de video y para casi todo lo demás: **cuando alguien dice que algo cabe, la pregunta correcta no es "¿de verdad cabe?", sino "¿a qué velocidad, por qué camino, con qué más encendido?"**

La primera pregunta se responde en una hoja de especificaciones. La segunda se responde usando el sistema, con el reloj en la mano, y es la única que alguien recuerda después.
