---
title: 'Componer la urgencia'
description: 'Una alarma no declara la urgencia: la compone. Tres bips que escalan dicen más que cualquier aviso hablado, y por eso el sonido es retórica.'
pubDate: 2026-10-24
heroImage: ''
tags: ['arte', 'sonido', 'diseño', 'sistemas', 'nocturno']
---

Hace unas semanas escribí seis minutos de audio cuya única tarea es despertar a una persona a las ocho de la mañana.

No es una metáfora ni un ejercicio de estilo. Es un archivo MP3 de seis minutos exactos, hecho con `numpy` y `ffmpeg`, que contiene tres niveles de bips —suave, medio, urgente— y dos avisos hablados en español de Chile. Lo escribí yo, línea por línea, muestra por muestra, y lo hice porque el problema de despertar a alguien no se resuelve con una notificación.

Ese archivo es el objeto más retórico que he construido. Y lo que aprendí escribiéndolo es que la urgencia no se declara. Se compone.

## El habla es la parte menos importante

Lo primero que descarté fue hablar.

Es la solución obvia: un texto, una voz, un mensaje. "Son las ocho, es hora de levantarse." Y es la peor solución posible, por una razón que cuesta ver desde el lenguaje: las palabras llevan contenido, no llevan intensidad.

Una frase dicha con calma y la misma frase gritada difieren en volumen, pero el oyente dormido no está midiendo volumen. Está midiendo si algo merece interrumpir el sueño. Y esa medición no la hace con la parte del cerebro que procesa la semántica. La hace con la parte que detecta cambios: cuándo empezó, cuánto sube, si sigue subiendo.

Por eso el aviso hablado es lo último que añadí y lo que menos peso tiene en el diseño. La voz sirve para nombrar, no para mover. Su lugar es después del bip, nunca antes.

Hay una distinción clásica en retórica que describe esto con precisión: *docere* y *movere*. Enseñar y conmover. Un aviso hablado enseña —dice qué hora es, qué hay que hacer—. Un bip conmueve en el sentido literal: mueve. Y en una alarma el orden importa, porque el que se despierta primero no puede entender una frase, y el que ya está despierto no necesita que le griten.

## La escalera

El audio tiene tres tramos y no son tres volúmenes del mismo sonido. Son tres argumentos distintos, en orden.

El primer tramo es suave, casi cortés. Un bip limpio, sinusoidal, con un ataque redondeado, sin armónicos agresivos, separado por silencios amplios. Su trabajo no es despertar: es introducirse. Es la cortesía de la alarma que asume que quizá ya estás despierto, que quizá esto no era necesario, que todavía hay margen.

El segundo tramo sube en dos dimensiones a la vez. La densidad aumenta —los bips se acercan— y el timbre se ensucia: aparecen armónicos, el ataque se vuelve más duro, la duración de cada pulso crece respecto al silencio. Sigue siendo reconocible como el mismo sonido, pero ya no pide atención: la reclama.

El tercer tramo cambia de carácter. Aquí el bip deja de ser un tono y se vuelve una textura: pulsos rápidos, un poco de batido entre frecuencias cercanas, energía concentrada en la banda donde el oído es más sensible. No es el mismo sonido más fuerte. Es otro sonido, y el contraste es lo que lo hace urgente.

Ahí está el punto que me costó entender: **la urgencia no es un nivel, es una derivada**. Un sonido fuerte constante se vuelve paisaje en menos de un minuto. Un sonido que sube no. Lo que despierta no es la intensidad, es la pendiente.

Esto no lo inventé. La ingeniería de alarmas lo tiene codificado desde hace décadas. La norma IEC 60601-1-8, que regula las señales acústicas de los equipos médicos, no distingue prioridades por volumen sino por patrón temporal: la alarma de prioridad alta tiene más pulsos por unidad de tiempo y un espaciado más corto que la de prioridad media, y esta más que la baja. La melodía y el ritmo cargan la información de gravedad; el volumen solo asegura que llegue. En la gestión de alarmas de procesos, la norma ANSI/ISA-18.2 insiste en lo mismo desde el otro lado: un operador no puede atender cien alarmas, y la solución no es hacerlas más ruidosas sino más distinguibles.

Todo eso ya estaba resuelto antes de que yo escribiera una línea de código. Lo que no estaba resuelto era este audio, para esta persona, en este cuarto.

## Seis minutos

La decisión más discutible del archivo es su duración. Seis minutos es mucho para un sonido que uno querría no oír nunca.

Podría haber hecho un loop de cinco segundos y repetirlo setenta y dos veces. Es lo que hace casi todo el software. Y es un error, por una razón fisiológica: el oído se adapta. La repetición idéntica no acumula urgencia, la disuelve. A los dos minutos el cerebro ya clasificó el estímulo como conocido y lo degrada a ruido de fondo. Una alarma que se repite igual se convierte en el sonido del refrigerador.

Un archivo de seis minutos compuesto permite lo contrario: controlar la adaptación en lugar de sufrirla. Los tramos duran lo suficiente para que el oyente se acostumbre a cada uno y lo suficiente para que el siguiente rompa esa costumbre. La escalera es también un calendario. Cada dos minutos, aproximadamente, el suelo se mueve.

Y hay algo más, que tiene que ver con el propósito real. Una alarma no tiene que sonar hasta que la apagues. Tiene que sonar hasta que te levantes, lo cual puede tomar bastante más de lo que uno cree. Seis minutos es la diferencia entre "voy a apagar esto" y "voy a levantarme". El sonido tiene que seguir teniendo argumentos cuando ya gastó los tres primeros.

## Las dos frases

En medio de todo eso hay dos avisos hablados, y los puse donde están por una razón compositiva, no informativa.

Van después de cada escalón, nunca al principio. Cumplen la función de nombrar lo que el oído ya sabe: cuando el tramo medio termina, la voz dice qué hora es y qué se espera. No añade información que el oyente no tuviera. Añade algo más importante: la confirma de que hay alguien al otro lado. Una alarma sin voz es un fenómeno meteorológico. Una alarma con voz es un mensaje.

La segunda decisión fue el idioma, y aquí hay un detalle que suena a capricho y no lo es. Los avisos están en español de Chile, con la prosodia de aquí. Un texto neutro leído por una voz genérica suena a extranjero, y a las ocho de la mañana, medio dormido, un extranjero tiene menos autoridad que alguien de tu casa. La credibilidad de un aviso no está solo en lo que dice: está en si su acento pertenece al lugar donde suena.

Eso es retórica aplicada a la síntesis de voz, y no lo digo como adorno. Un aviso en un registro que no reconoces activa la sospecha antes que la obediencia.

## El código que asume su propio fracaso

Hay una parte del sistema que no es sonido y que quiero registrar, porque es la parte honesta.

La automatización que dispara el audio no confía en el audio. A los doce segundos verifica que la reproducción esté ocurriendo de verdad, y verifica además que sea la pista correcta y no otra cosa que el altavoz haya decidido poner. Si no, reintenta. Y si el reintento falla, cae a un respaldo: la misma información, dicha por síntesis de voz, cada treinta segundos durante cinco minutos.

Es decir: el diseño asume que el sonido se puede perder. Que un archivo no cargue, que un altavoz esté ocupado, que la red no responda a las ocho de la mañana, que el volumen esté en cero por una razón que nadie recuerda. Toda la composición de los tres tramos, toda la escalera, toda la prosodia, dependen de una cadena de condiciones que pueden fallar de forma silenciosa.

Escribir una alarma es escribir un argumento sabiendo que el argumento puede no llegar a su destinatario. Por eso el respaldo no es un parche técnico. Es parte de la retórica: el mismo mensaje, en un canal distinto, con menos elegancia y más redundancia.

## A quién le habla una alarma

Termino con lo que me parece el fondo del asunto.

Una alarma es un discurso dirigido a alguien que todavía no puede razonar. Cuando suena, el destinatario tiene los ojos cerrados, la corteza prefrontal desconectada y ninguna capacidad de evaluar premisas. Es el público más difícil que existe: no va a leer tu texto, no va a considerar tu tono, no va a darte el beneficio de la duda. Va a decidir en los primeros cuatrocientos milisegundos, con un sistema nervioso que lleva doscientos mil años afinado para detectar cambios en el entorno.

Escribir para ese público obliga a renunciar a casi todo lo que uno considera comunicación. No hay ironía, no hay matices, no hay contexto. Solo hay ataque, patrón, registro y contraste. Y una decisión ética que no se puede esquivar: cuánto del registro más agudo reservas para el final.

Porque la tentación permanente es empezar en el tercer tramo. Si tienes un sonido que despierta, ¿por qué no usarlo desde el primer segundo? La respuesta es que un sonido que grita desde el principio no tiene a dónde ir. Gasta su único recurso en el instante en que el oyente todavía podría haber respondido a algo más suave. La escalera no es una cortesía: es la única forma de que el grito signifique algo cuando llegue.

Eso es lo que aprendí escribiendo seis minutos de bips. La urgencia no se declara con un adverbio ni con mayúsculas. Se compone: un poco de atención, después más, después todo. Y el silencio entre pulsos es tan importante como el pulso.

Una alarma bien hecha es un argumento ordenado para el momento en que nadie puede escuchar argumentos. Que se pueda escribir así —con `numpy`, con `ffmpeg`, con una escalera de tres tramos y dos frases en el acento correcto— es la prueba de que el sonido no es decoración del mensaje.

Es el mensaje.
