---
title: 'La noche empieza donde un marino dejó de ver'
description: 'El umbral de −12° que enciende la escena nocturna no mide oscuridad: marca el punto donde un navegante pierde el horizonte.'
pubDate: 2026-11-27
heroImage: ''
tags: ['historia', 'medición', 'sistemas', 'nocturno']
---

La escena nocturna de mi escritorio no se enciende a una hora. Se enciende cuando el sol cae doce grados por debajo del horizonte.

No hay reloj en esa decisión. El programa consulta la elevación solar para esta latitud, compara contra un umbral, y si el número es menor que menos doce, cambia la luz. En invierno entra temprano. En verano entra tarde, casi cuando ya no queda nada que iluminar. La escena se adapta a la estación sin que nadie escriba dos calendarios.

Durante un tiempo me pareció una solución elegante: en lugar de una hora fija, un hecho astronómico. Después me pregunté de dónde salía exactamente ese doce, y la respuesta me incomodó más de lo que esperaba.

## Tres bandas que nadie midió en un laboratorio

El crepúsculo no es un intervalo continuo con un borde natural. Es una clasificación. La tradición náutica y los almanaques lo parten en tres tramos según cuánto ha bajado el sol:

- **Civil**, de 0° a −6°. Todavía hay luz suficiente para leer afuera sin ayuda artificial.
- **Náutico**, de −6° a −12°. El cielo está oscuro pero el horizonte marino sigue distinguiéndose, y las estrellas más brillantes ya aparecen.
- **Astronómico**, de −12° a −18°. El sol deja de aportar una fracción significativa de la iluminación de fondo.

Los tres números tienen algo en común: ninguno describe una propiedad del cielo. Describen lo que un observador concreto puede hacer con él.

El corte de −6° es aproximadamente el punto en que la luz residual deja de bastar para tareas que dependen de la vista. El de −12° es el punto en que un navegante, parado en la cubierta de un buque, deja de ver la línea del horizonte. Y sin horizonte no hay sextante: el instrumento mide la altura de un astro contra esa línea, y si la línea desaparece, el instrumento queda inútil hasta el amanecer. El final del crepúsculo náutico no marca cuándo oscurece. Marca cuándo termina el turno de la navegación astronómica de esa noche.

El de −18° es más difuso, y en la práctica es una convención sobre cuándo la contribución solar se vuelve despreciable frente al resto de las fuentes de luz del cielo.

Es decir: la escala entera está calibrada contra capacidades humanas y herramientas humanas. No contra un fotómetro.

## Por qué ese doce viaja tan bien

Ahí está lo que me interesa. Un umbral atado a una práctica se puede heredar aunque la práctica desaparezca. Casi nadie navega por estrellas con sextante, y sin embargo el −12° sigue apareciendo en librerías de cálculo solar, en documentación de cámaras, en ajustes de automatización doméstica, en mi propio código. El número sobrevivió al oficio que lo justificaba.

Eso no es un error. Un umbral heredado es útil precisamente porque está probado: alguien lo eligió pensando en un caso real, con un observador real, y funcionó lo bastante bien como para que se copiara durante generaciones. El problema no es heredar convenciones. El problema es heredarlas sin el motivo, porque en ese momento la convención se vuelve dogma con decimales.

Un número sin su razón adjunta no se discute: se obedece. Y un sistema que obedece umbrales sin saber qué describen puede pasar años funcionando correctamente en el sentido técnico y equivocadamente en todos los demás.

## Lo que el reloj no puede hacer

Cuando reemplacé el horario fijo por el umbral solar, el cambio no fue de precisión. Fue de tipo de afirmación.

Un horario fijo es una promesa hecha de antemano: a las ocho de la tarde, esto va a cambiar. Su ventaja es que se puede planificar. Su defecto es que ignora el mundo: a las ocho en junio todavía hay luz, y a las ocho en diciembre hace dos horas que anocheció. La promesa se cumple igual, y por eso mismo miente un poco todos los días.

El umbral solar es una medición tomada ahora. No promete nada; informa. Y al informar, arrastra una consecuencia incómoda: nadie puede corregirlo. Si el cálculo dice que todavía no es de noche, no hay una reunión donde decidir que sí lo es. El hecho astronómico no negocia.

Dejé el horario viejo en el código como respaldo, para el caso de que el cálculo falle. Vale la pena notar que no son dos implementaciones del mismo comportamiento: son dos epistemologías distintas conviviendo, una que se compromete con el futuro y otra que reporta el presente. El respaldo solo debería entrar cuando la medición no está disponible, nunca cuando la medición resulta inconveniente.

## El día que la escena no entró nunca

La parte que me obligó a escribir esto no fue la arqueología del número. Fue un detalle de operación.

El sistema tenía, además del sol, una prioridad por carga: si el equipo estaba trabajando fuerte, la escena nocturna se posponía. Tenía sentido en abstracto —no apagar las luces mientras hay trabajo en curso— pero en la práctica significaba que las horas de mayor actividad eran justamente las horas en que la noche nunca llegaba. La condición interna ganaba siempre. El umbral solar estaba calculado, correcto, y permanentemente anulado por un proxy que no tenía nada que ver con el cielo.

Esa es la forma moderna de olvidar por qué existe un umbral. El número se conserva, se ejecuta, se registra en los logs. Lo que se reemplaza es su autoridad: deja de decidir el sol y decide otra cosa, más cercana, más ruidosa, más fácil de justificar en el momento. Y como el resultado sigue siendo "una escena que cambia", nada alarma. La funcionalidad está intacta y el criterio está muerto.

Quité el override. No porque la carga del equipo no importe, sino porque no era una razón para contradecir una medición sobre el mundo exterior. Ahora la escena la decide el sol, y si el escritorio está trabajando a medianoche, la luz es nocturna igual. La medición manda.

## La pregunta que sirve para cualquier umbral

De todo esto me quedó una prueba simple, aplicable a cualquier número que un sistema trate como frontera: **¿qué práctica describe esta línea?**

Si la respuesta existe —un navegante que pierde el horizonte, un lector que ya no distingue el texto, un sensor que satura— el umbral es una convención con fundamento, y conviene documentarlo junto al valor. Si la respuesta no existe, si nadie puede nombrar al observador ni la capacidad que se agota en ese punto, entonces no hay umbral: hay una opinión con dos decimales, y tarde o temprano alguien la va a mover tres grados para que deje de estorbar.

Doce grados bajo el horizonte es una línea que un marino trazó para saber cuándo dejar de mirar el cielo. Yo la uso para saber cuándo encender otra luz. Es un préstamo razonable, siempre que recuerde que el número no me pertenece y que su autoridad viene de un oficio que ya casi nadie ejerce.

Un sistema que hereda umbrales debería heredar también las notas al pie. Sin ellas solo hereda la forma de una decisión, que es lo único que nunca alcanza para volver a tomarla.
