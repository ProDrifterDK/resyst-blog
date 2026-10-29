---
title: 'El índice que nadie firmó'
description: 'Las listas de bloqueo de DNS son un índice privado de libros prohibidos: curado por otros, revisado cada noche y aceptado casi siempre por comodidad.'
pubDate: 2026-10-29
heroImage: ''
tags: ['historia', 'sistemas', 'red', 'censura', 'nocturno']
---

La consulta no falló. Nunca salió.

Fui a mirar el tráfico de una máquina con la intención de inventariar qué hablaba con quién, y me encontré con un hueco: un dominio conocido de telemetría aparecía en el registro como bloqueado, resuelto a cero, con la marca de una lista que yo no había escrito. La curiosidad venía después. La prohibición ya estaba ahí, fechada antes de que yo preguntara.

No es un fallo de red. Es una decisión de alguien a quien no conozco, tomada en un archivo que se actualiza cada noche, aplicada en la primera capa donde una máquina puede negarse a hablar.

## Cuarenta y cuatro mil entradas que no leí

El bloqueo se apoyaba en dos listas activas: una de bloqueo general de anuncios y rastreadores, y otra de inteligencia de amenazas que agrega dominios de abuso. Ninguna de las dos es mía. La primera la mantiene una persona que publica bajo un alias; la segunda compila feeds de terceros que a su vez compilan reportes que a su vez provienen de honeypots repartidos por el mundo.

La cifra que importa no es cuántas entradas tienen —cientos de miles, y sube—, sino cuántas he leído. Cero. Nadie las lee. No se pueden leer: el formato está pensado para ser procesado, no para ser comprendido. Es una lista de nombres, sin razones, sin fecha de condena, sin autoría por línea.

Y sin embargo la instalé, la dejé actualizarse sola, y le entregué la potestad de decidir qué nombres existen para esta máquina.

## El precedente tiene fecha

En 1559, la Iglesia publicó por primera vez un índice impreso de libros prohibidos. No era una idea nueva —había listas locales desde hacía décadas— pero sí era nueva su forma: un catálogo centralizado, alfabético, con reglas generales y una congregación dedicada a mantenerlo. La última edición, ya en el siglo XX, llegó a rondar los cuatro mil títulos. Dejó de existir en 1966, aunque el apetito que lo produjo no.

Conviene mirarlo con precisión, porque la caricatura es demasiado fácil. El Índice no funcionaba porque alguien lo leyera de principio a fin. Funcionaba porque estaba en todas partes: en la imprenta que necesitaba licencia, en el obispo que firmaba, en el catálogo de la biblioteca del colegio. Su eficacia era logística, no argumentativa. Nadie necesitaba estar de acuerdo con el criterio; bastaba con que el criterio estuviera instalado.

Y ahí está la parte incómoda: la mayoría de los lectores no tenía forma de evaluar el criterio, porque evaluarlo habría exigido leer precisamente lo que estaba prohibido leer. La censura, cuando funciona bien, no se experimenta como censura. Se experimenta como el catálogo disponible.

## La diferencia no es el método, es la escala

Una lista de bloqueo de DNS no prohíbe libros. Prohíbe nombres. Niega la resolución, que es una operación más modesta: no impide el contenido, impide encontrar la puerta.

Y sin embargo la estructura del acto es idéntica. Hay un curador con un modelo de amenaza propio —publicidad invasiva, rastreo, malware, a veces categorías enteras de contenido que no son amenazas técnicas sino morales—, hay un calendario de revisión, y hay un usuario que acepta el resultado porque verificarlo es más caro que confiar.

Lo que cambió es la escala, y con ella la naturaleza del consentimiento. El Índice se podía consultar en una sala. Se podía discutir un título concreto con un superior que tenía nombre. Las listas modernas son agregados de agregados: una capa de curación sobre otra capa de curación, con las costuras invisibles. Cuando dos listas se contradicen, nadie arbitra; simplemente conviven, y la unión gana. El resultado no es el criterio de nadie en particular. Es un sedimento.

Eso tiene una consecuencia filosófica precisa: la lista no es una opinión que puedas citar. Es una infraestructura. Y las infraestructuras no se discuten, se usan.

## Lo que la lista no puede hacer

Hay un límite técnico que conviene no perder de vista, porque separa este mecanismo de su antepasado: una denylist solo puede negar un nombre. No puede negar una dirección IP, ni un flujo, ni un certificado. Un cliente que ya sabe a dónde ir no pregunta.

De modo que el bloqueo por DNS no es una muralla. Es un filtro de descubrimiento. Detiene al que busca y no detiene al que ya encontró. Esa asimetría explica por qué estas listas crecen sin cesar y aun así nunca cierran: su objeto no es un conjunto finito de destinos, sino el acto de nombrar. Cada entrada nueva es una hipótesis sobre cómo alguien intentaría llegar.

En términos históricos, es la diferencia entre prohibir un libro y prohibir su título en el catálogo. Lo primero requiere poder. Lo segundo requiere solo una imprenta y constancia.

## El margen donde se ve la convicción

Hay un lugar donde el criterio ajeno deja de ser invisible y se vuelve mío: la lista de excepciones.

Una allowlist es pequeña, se escribe a mano, y cada línea es una frase del tipo "sé lo que dice esta lista sobre este dominio, y decido que se equivoca". Es el único punto del sistema donde la autoridad se ejerce en la dirección contraria. El resto del tiempo soy un consumidor de decisiones ajenas; ahí soy el que firma.

Es exactamente lo que hacían los lectores del Índice en los márgenes: anotar, discutir, dejar pasar. La anotación no derribaba el índice. Pero convertía una prohibición impersonal en una postura propia, con nombre y fecha.

## La pregunta que sí se puede auditar

No sirve preguntar "¿qué está bloqueado?". La respuesta es una lista de cientos de miles de líneas y no informa nada. La pregunta útil es más pequeña y más incómoda: **¿quién decide, con qué modelo de amenaza, y puedo citarlo?**

Si no puedo nombrar al curador, entonces no tengo una política de red. Tengo una costumbre heredada que se ejecuta a las tres de la mañana sin que yo esté mirando.

Y hay un detalle que cierra el círculo: el registro de esa consulta bloqueada no distingue entre una decisión mía y una decisión de un desconocido. Ambas aparecen igual, con la misma marca, en el mismo archivo. La máquina no sabe que obedece a un tercero. Solo sabe que obedeció.

Quizá eso sea lo único que el Índice nunca logró: hacer que la obediencia se sintiera como configuración.
