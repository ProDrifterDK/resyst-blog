---
title: 'Shibboleth: el examen de pronunciación que nunca midió una idea'
description: 'La jerga técnica no prueba claridad: prueba pertenencia. Una lista de palabras prohibidas mide la tribu del lector, no la verdad del texto.'
pubDate: 2026-11-04
heroImage: ''
tags: ['historia', 'lenguaje', 'sistemas', 'nocturno']
---

Igual que todo lector, tengo una lista. No la escribí de una vez: se fue formando por acumulación de decepciones. Cuando un texto técnico menciona ciertas palabras, algo se cierra antes de que termine la primera página. *Cache invalidation*. *Write-through*. *Circuit breaker*. *Race condition*. *Pub/Sub*. *Tailwind*. *Railway*. *Dataloader*.

La lista es heterogénea hasta ser sospechosa. Ahí conviven un problema clásico de sistemas, un patrón de resiliencia, una biblioteca de CSS, una plataforma de despliegue y una capa de acceso a datos. No comparten tema, no comparten nivel de abstracción, no comparten época. Lo único que comparten es el efecto: cuando aparecen sin contexto, dejé de creerle al texto.

Durante mucho tiempo pensé que esa lista medía claridad. No mide eso. Mide otra cosa, y esa otra cosa es mucho más antigua que el software.

## La palabra que decidió un vado

Libro de los Jueces, capítulo 12. Los galaaditas controlan los vados del Jordán y necesitan distinguir a los fugitivos efraimitas que intentan cruzar haciéndose pasar por suyos. La prueba es una sola palabra: *shibboleth*. El que no puede pronunciarla bien, no pasa.

El texto no dice que se evaluara el significado. De hecho la palabra significa algo trivial —espiga, o corriente de agua, según la traducción—. Nadie preguntaba qué era una espiga. Preguntaban si tu boca podía producir el sonido inicial. Los efraimitas decían *sibboleth*, sin la fricativa, y esa *s* los delataba. El pasaje cierra con una cifra que se repite hace tres mil años: cuarenta y dos mil.

Ese es el invento. No el control de acceso, no la vigilancia: la idea de que la forma de pronunciar una palabra puede sustituir a la pregunta de quién eres. Un shibboleth tiene dos propiedades exactas. Es baratísimo de aplicar. Y es imposible de responder: el que lo falla no puede argumentar, no hay contraprueba, no existe la posibilidad de decir «espera, me equivoqué de vocal, dejame explicarte».

La Segunda Guerra Mundial repitió el truco con precisión burocrática. La resistencia holandesa usaba el nombre de un balneario, *Scheveningen*, porque la secuencia inicial resulta difícil para una garganta alemana. En el Pacífico se usó *lollapalooza*, una palabra que existe casi para sonar ridícula. En ambos casos el contenido semántico era irrelevante: un topónimo y una onomatopeya. Lo que se probaba no era conocimiento. Era origen.

## Por qué la jerga se comporta igual

Volvamos a la lista. *Race condition* nombra un estado del mundo: dos escritores, una ventana, un resultado que depende del orden en que llegaron. *Cache invalidation* nombra un problema que alguien tuvo que sufrir para saber que existía. Son palabras caras: no se aprenden leyendo, se aprenden rompiendo algo.

*Tailwind* y *Railway* no nombran estados del mundo. Nombran productos. *Pub/Sub* nombra un patrón, pero también una decisión de arquitectura que en la mayoría de los textos no se explica: se invoca. La diferencia entre estos dos grupos no es de prestigio ni de gusto. Es de referente. Una palabra con referente resiste que la interroguen; una palabra sin referente solo recluta.

Ahí está el mecanismo. La jerga técnica funciona como shibboleth en el momento exacto en que aparece sin referente verificable, porque en ese momento deja de comunicar y empieza a ubicar. No dice «esto es lo que pasa en mi sistema». Dice «yo estuve donde se habla así». Y el lector hace lo mismo desde el otro lado de la página: no evalúa la idea, evalúa la pronunciación. Reconoce la tribu y ajusta su confianza en consecuencia.

Por eso mi lista es tan rara. No es un catálogo de conceptos malos. Es un registro de las veces que una palabra apareció sin cicatriz detrás.

## El precio de prohibir palabras

Hay una trampa en el método, y es exactamente la trampa opuesta a la que creía estar evitando. Prohibir vocabulario produce paráfrasis, y la paráfrasis es el lugar donde muere la precisión. Alguien que no puede escribir *race condition* escribe «un tema de concurrencia», y ahora sé menos que antes. La palabra vetada era un diagnóstico; su reemplazo es una niebla.

Peor todavía: una lista de palabras prohibidas es un test que se puede pasar sin entender nada. El texto hueco, el que no dice nada y por eso no necesita ningún término incómodo, aprueba con honores. Y el desprecio por la jerga terminó teniendo su propio dialecto: un modo de hablar para los tuyos, con su vocabulario obligatorio y sus palabras malditas. La misma operación tribal, con el signo invertido. Nadie está midiendo el contenido. Todos están midiendo el acento.

La historia del *cant* inglés del siglo XVI ayuda a no idealizar ninguna de las dos posiciones. El vocabulario de los ladrones funcionaba igual que un shibboleth: una lengua propia para que el alguacil entendiera la conversación y no pudiera repetirla. Cuando ese vocabulario se filtró a los panfletos que lo publicaban como curiosidad, dejó de servir como cifrado y empezó a servir como disfraz. La misma lista, dos funciones, ninguna relacionada con la verdad de lo que se decía.

## La lista que sí sirve

Después de años de usar la lista negra, la cambié por otra cosa. Ya no llevo palabras prohibidas. Llevo preguntas que el texto tiene que sobrevivir.

Si aparece *circuit breaker*: ¿cuál es el umbral, quién lo fijó, qué pasó la primera vez que se abrió? Si aparece *cache invalidation*: ¿qué invalidó qué, y cómo lo supiste? Si aparece *dataloader*: ¿cuántas consultas había antes, cuántas después, medido dónde? Si aparece *Pub/Sub*: ¿qué pasa cuando un suscriptor llega tarde, y quién decide el orden?

Son tres preguntas por término y ninguna es retórica. Un concepto las contesta con hechos que ya existían en la cabeza del que escribe. Un distintivo se cae en la segunda. Y hay una asimetría que me gusta: la palabra que sobrevive tres preguntas deja de molestarme. No importa cuán de moda esté. Lo que me molestaba no era la palabra, era la ausencia de cicatriz detrás de ella.

La diferencia entre un shibboleth y una pregunta es que la pregunta admite respuesta. Un shibboleth no, y por eso mata: no deja espacio para la corrección. Cuando el galaadita exigía la palabra en el vado, no estaba pidiendo información. Estaba ejecutando una decisión que ya había tomado. El test era el veredicto disfrazado de verificación.

## Lo que quiero de un texto

No quiero saber si tu tribu me reconoce. Quiero saber si tu texto resiste que le pregunte. Esa es toda la política, y es más exigente que cualquier lista de palabras malditas, porque me obliga a leer con atención en lugar de escanear en busca de tokens.

Los cuarenta y dos mil no murieron por decir mal una palabra. Murieron por estar en la orilla equivocada del río. El test solo hizo falta para no tener que mirarlos.
