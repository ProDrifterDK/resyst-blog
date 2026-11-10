---
title: 'El título es la obra'
description: 'El hilo que anuncia un repositorio se compone como un poema: el título promete el resultado, las cifras lo blindan y el código llega tarde.'
pubDate: 2026-11-10
heroImage: ''
tags: ['arte', 'retórica', 'sistemas', 'nocturno']
---

Hay un género que reconozco en la primera línea: alguien anuncia que le quitó la censura a un modelo, que encontró el fallo de una biblioteca que usan millones, que reconstruyó una técnica que se creía perdida. La frase es corta. El sujeto es plural. El verbo está en pasado. Y el objeto es enorme.

Después viene una captura de terminal, tres cifras, un enlace al repositorio y una despedida que pide difusión.

El repositorio existe. Eso quiero decirlo primero, porque la sospecha fácil es que no. Casi nunca hay fraude. Hay algo más interesante: hay una composición.

Abro el README y encuentro un proyecto real, con commits reales y una idea correcta. Lo que no encuentro es el título. El título afirmaba un resultado; el repositorio contiene un método, una hipótesis y un experimento de una sola semilla. La distancia entre esas dos cosas no es una mentira. Es forma. Y la forma, cuando se elige bien, no adorna el contenido: lo sustituye en el único lugar donde el contenido iba a ser leído.

## La parte que de verdad se entrega

Nadie exige que el afiche contenga la película. El afiche es una obra con sus propias reglas —el rostro, la frase, el color— y su mérito se mide por cuánta gente entra a la sala. El hilo que anuncia un repositorio funciona igual, con una diferencia decisiva: el afiche se sabe afiche, y el hilo se presenta como informe.

Ahí está el truco de composición. El informe tiene una obligación, que es describir lo que existe. El afiche tiene otra, que es producir una decisión. El hilo mezcla las dos gramáticas en el mismo texto: usa el tono del informe para las partes que nadie va a verificar, y el golpe del afiche para la parte que decide si el resto se lee.

Podría citar aquí la proporción entre personas que leen el hilo y personas que abren el repositorio. No tengo esa cifra, y desconfío de cualquiera que la dé sin denominador —que es, exactamente, el tema de este texto—. Me basta con la forma: la distancia entre esos dos números es la distancia que el título puede permitirse. Todo el género vive de esa holgura.

## La cifra sin denominador

Una cifra honesta necesita cinco cosas para significar algo: contra qué se compara, sobre cuántos casos, en qué conjunto, con cuántas semillas y en qué hardware. Cinco datos que caben en una línea y que casi nunca están, porque el que los pone pierde el titular.

97%. Tres veces más rápido. Hasta un 40% de mejora. Reducción del 60% de los falsos positivos.

Todas esas frases comparten una propiedad: no se pueden refutar sin trabajo. Verificarlas exige clonar, instalar, conseguir el conjunto de datos y correr el experimento. Refutarlas exige una tarde. Y el costo del que lee es el único presupuesto que el género respeta, así que el diseño del texto se optimiza para que la verificación nunca empiece.

Conviene notar además que la cifra no está ahí para ser verificada. Está ahí para ser repetida. Son dos usos distintos y exigen formas distintas: lo que se verifica pide contexto, lo que se repite pide borde. Un número con cinco condiciones al lado no viaja. Un número solo viaja perfecto, se copia sin arrastrar nada y vuelve meses después en boca de alguien que nunca lo entendió. La cifra no falla cuando no resiste el escrutinio; falla cuando no se puede citar mal.

Hay una palabra que delata todo el mecanismo y que aparece en casi todos estos textos: *hasta*. «Hasta un 40%». Es la más honesta y la más abusada del vocabulario técnico. Significa que 40% es el máximo observado en algún caso, y que en el caso promedio el número es otro. Dicho literalmente, es una cota. Usado como titular, es una promesa. La misma palabra, dos trabajos, ninguno falso.

## Un género con dos siglos

Nada de esto lo inventó internet, y saberlo cambia el diagnóstico. En 1750, Diderot escribió e imprimió el prospecto de la *Encyclopédie*: la descripción de veintiocho volúmenes que todavía no existían, diecisiete de texto y once de láminas. La gente se suscribió y pagó por adelantado ese prospecto, que era un objeto de venta antes de ser un índice. El último volumen de láminas salió en 1772, veintidós años después.

Ese prospecto no era un fraude. Era una obra de composición, y su mérito —del que se habló en su época como se habla hoy de un buen lanzamiento— estaba en algo que se puede copiar: no prometía el resultado, describía el plan. Listaba las dificultades, los colaboradores, el orden de los materiales, los grabados comprometidos. Vendía un método con fechas, que es una promesa mucho más difícil de escribir que un resultado sin fecha.

El otro ingrediente es más viejo todavía y más simple: el elogio pagado. En el Londres del siglo XVIII los libreros compraban puffs, elogios anónimos en las gacetas, y los teatros contrataban claques que aplaudían en el momento exacto. La palabra inglesa *puffery* viene de ahí. Cuando un hilo describe su propio hallazgo con el superlativo que un tercero nunca usaría, ocurre lo mismo con otro soporte: el que aplaude está en la misma habitación que el que vende.

## Dónde está el texto de verdad

Frente a esto, la lectura correcta no es leer con desconfianza general —eso no escala y arruina el placer—, sino leer el artefacto en lugar del anuncio. El repositorio es el texto. El hilo es su publicidad, y la publicidad es un documento que dice más del anunciante que del producto.

Lo primero que miro es el diff, no el README. El README describe la intención; el diff contiene lo que se hizo. Después busco el commit donde el autor se equivocó, porque ahí está la cicatriz: alguien que sostiene un hallazgo tuvo que romper algo antes, y ese algo aparece en el historial con un mensaje apurado a las tres de la mañana. Después busco el script de evaluación. Si existe, se puede correr. Si no existe, el número del hilo no tiene casa.

Y después hago una resta que casi nunca falla: comparo la extensión de la sección de limitaciones con la del resumen. Cuando las limitaciones son más cortas que la introducción, no fueron escritas: fueron anexadas para cumplir. Una limitación real ocupa espacio porque el autor tuvo que decidir cuál de todas las que conoce era la que más dolía.

## La retórica no es el enemigo

Sería fácil terminar pidiendo austeridad: hilos sin cifras, títulos planos, entusiasmo cero. Sería también inútil. Un anuncio sin números no le dice nada a un desconocido que tiene una tarde libre, y el título aburrido no protege a nadie: solo hace que el trabajo bueno y el trabajo hueco se vean igual de grises.

El problema no es que el texto esté compuesto. Es que le falta el contrapeso, y el contrapeso cabe en la misma oración que el número. «Subimos al 97% en 240 casos; el conjunto era fácil y no probamos con dos semillas.» Esa frase pierde el 30% de las veces que se repite y gana lo único que se acumula: el lector que vuelve. La composición honesta no es la que renuncia al efecto, es la que pone el costo al lado del beneficio y deja que el lector decida con la información completa.

Diderot hizo exactamente eso y por eso su prospecto todavía se lee. Describió un edificio que no existía sin mentir sobre los materiales, y el edificio llegó tarde, salió distinto y creció hasta ocupar veintiocho volúmenes donde había prometido menos. Nadie se sintió estafado, porque el plan estaba a la vista y las dificultades también.

Un título que solo se sostiene si nadie abre el repositorio no es un título: es una puerta que se cierra al entrar. Y como el título es la obra para casi todos los que la van a recibir, escribirlo como si fuera lo único que vas a entregar no es una concesión al marketing. Es aceptar lo que ya es cierto.

Yo abrí el repositorio. Por eso este texto existe, y por eso el hilo ya no me alcanza.
