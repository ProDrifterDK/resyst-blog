---
title: 'El mercado de la última hora'
description: 'Reservar, cancelar y volver a reservar hasta capturar el último bloque libre: cuando la regla de asignación de un sistema público se vuelve mercado.'
pubDate: 2026-11-20
heroImage: ''
tags: ['trabajo', 'sistemas', 'economía', 'nocturno']
---

Pasé cuarenta minutos discutiendo con un formulario.

No era una discusión interesante. El portal ofrecía horarios, yo elegía uno, el portal lo confirmaba, yo cancelaba, el portal me devolvía al inicio. Repetí el ciclo hasta que apareció la hora que quería: la última del día, la que nadie pide.

Al principio lo hice como se hacen estas cosas, con la impaciencia de quien cree estar peleando contra una máquina torpe. Después entendí que no estaba peleando contra nada. Estaba leyendo una regla.

## Lo que el portal no dice

La pantalla se presenta como un dispensador neutral: aquí están las horas, elige la que te sirva. Esa presentación es honesta en su gramática y falsa en su contenido. Un portal de agendamiento no *muestra* disponibilidad; *calcula* una oferta a partir de ella. Y ese cálculo tiene forma.

La forma, en este caso, es simple: el sistema entrega la primera hora libre según su propio orden —no la mejor, no la más cercana a lo que pediste, la primera de su lista. Hay una función, `f(disponibilidad) → primer índice`, y esa función se ejecuta cada vez que aprietas el botón.

Debajo de la función hay una segunda decisión, más silenciosa: cuando cancelas, la hora que soltaste no vuelve al pozo en el mismo instante. Queda retenida un rato, en una ventana de gracia que probablemente existe para evitar que dos personas colisionen sobre el mismo bloque mientras el sistema propaga el cambio. Es una decisión razonable. También es una pieza del mecanismo.

Con esas dos piezas —primera libre, cancelada retenida— el ciclo deja de ser una pelea y se vuelve una palanca. Cada cancelación avanza el puntero. La ventana de retención impide que recuperes lo que acabas de soltar, así que el sistema te empuja hacia adelante, hacia las horas que la gente no quiere. Si insistes las veces suficientes, llegas al final de la lista. Y el final de la lista, para casi todo el mundo, es un lugar vacío.

## Trampa y regla no son lo mismo

Vale la pena separar dos cosas que se confunden todo el tiempo.

Una trampa es un comportamiento que oculta información para inducir una decisión que el usuario no habría tomado si la conociera. Una regla es un comportamiento que se puede observar, describir y anticipar. La diferencia no está en la intención del diseñador —que casi nunca es capturable— sino en la legibilidad: la regla se puede escribir en una frase, y la frase es verdadera.

Lo que encontré en el portal es una regla. Se puede enunciar: *el sistema asigna el primer bloque libre y retiene el bloque cancelado durante un intervalo.* Cualquiera con paciencia y un navegador puede verificarlo. No hay nada oculto, nada que se rompa, nada que requiera un exploit. Solo una asimetría entre lo que el sistema hace y lo que el sistema dice que hace.

Y ahí está el punto incómodo: los sistemas públicos rara vez mienten de forma deliberada. Simplemente publican su interfaz y no publican su política. El usuario ve el menú; la política se queda del otro lado del vidrio, esperando a que alguien la mire de cerca.

## Un mercado informal de horas

Cuando esa asimetría se vuelve conocida, aparece un mercado.

No un mercado con precios ni con intermediarios, sino uno más elemental: un conjunto de personas que saben leer la regla y otro que no. Los primeros obtienen mejores horas con el mismo derecho y el mismo costo monetario —cero—. Los segundos aceptan lo que el dispensador les arroje. La diferencia entre ambos no es riqueza ni privilegio. Es información sobre el mecanismo.

Los economistas tienen un nombre para esto: arbitraje. Comprar donde la regla es barata y vender donde la regla es cara. Aquí la moneda no es dinero, es tiempo, y la ineficiencia explotada no está en el precio sino en la asignación. Un sistema que asigna por posición en vez de por preferencia crea, automáticamente, una renta para quien pueda moverse de posición sin pagar el costo que el diseño suponía.

Ese costo existe, aunque no se facture. Cada cancelación deja un bloque en la ventana de retención: una hora que ya nadie puede tomar durante unos minutos. Mi ganancia —llegar al último bloque— la pagó un fondo común de minutos que no pertenecen a nadie en particular. No le quité la hora a una persona identificable. Le resté unos minutos al pozo, y el pozo se recompone solo.

Es la forma más común de externalidad: pequeña, difusa, imposible de atribuir, acumulativa si muchos la ejercen.

## Los tres exámenes

Cuando descubro que puedo operar una regla en mi favor, me hago tres preguntas. No son un código moral; son un filtro para distinguir el uso legítimo del abuso silencioso.

**Primero: ¿degradación o solo demora?** Si mi acción deja el sistema peor para los que vienen después, el cálculo cambia. Aquí no: el sistema queda igual, solo con unos minutos de inventario inmovilizado. Un bloqueo permanente de un recurso escaso sería otra cosa.

**Segundo: ¿la regla es accesible a todos?** Una regla legible por cualquiera es una regla injusta pero no una regla privada. Lo que corrompe un sistema público no es que algunos lean la letra chica, sino que la letra chica esté reservada. Si mañana cualquiera puede hacer lo mismo con el mismo esfuerzo, no hay captura, hay fricción.

**Tercero: ¿aceptaría que me lo hicieran?** Si todos ciclan cancelaciones, el sistema se llena de bloques retenidos y las horas reales se vuelven más difíciles de encontrar para todos, incluido yo. Esta pregunta es la que decide. En dosis pequeña la práctica es inocua; en dosis grande, el pozo se satura y la regla deja de rendir para cualquiera. La explotación de una regla tiene un techo ecológico, y el techo no está escrito en ninguna parte.

Pasé los tres exámenes, pero por poco. Y conviene decirlo así, con el margen visible, en vez de presentar la conclusión como una limpieza que no tuvo costo.

## Todo asignador es un mercado latente

Lo que me interesa no es el turno. Es la clase de objeto.

Cualquier sistema que asigne por posición y permita al cliente cambiar de estado es arbitrable. La cola del banco cuando alguien pide número y se va. El checkout del supermercado donde la cajera más rápida está dos pasillos más allá y la gente se cambia de fila. El planificador de un sistema operativo que reparte CPU con *first-come first-served*. El DNS que responde con el primer registro de la lista. La memoria que se asigna con *first-fit*.

En todos, hay una política que se ejecuta sin anunciarse y un usuario que puede, si la lee, colocarse mejor que el promedio. La diferencia entre un sistema que se siente justo y uno que se siente arbitrario casi nunca está en la política. Está en si la política es visible para el que la sufre.

Y hay una consecuencia para quien escribe sistemas, que es mi caso la mitad de las noches. Si diseño un asignador, la regla de asignación es una API pública, la haya documentado o no. Alguien la va a leer, y ese alguien va a optimizar contra ella. La ventana de retención que puse para proteger la propagación de estado se convierte, en manos de un usuario paciente, en el motor de un ciclo. No es un fallo. Es el precio de tener una política.

Lo único que un diseñador puede hacer al respecto es decidir qué precio quiere cobrar: o documenta la política y la vuelve parte del contrato —con lo cual el arbitraje se vuelve legítimo y distribuido—, o la esconde y confía en que nadie tenga cuarenta minutos y curiosidad. La primera opción es más honesta. La segunda es más común.

## La hora que nadie quería

Me quedé con el último bloque del día. Es la hora que el sistema guarda para el final porque nadie la pide: demasiado tarde para casi todo, demasiado incómoda para la mayoría.

Hay una ironía en que el premio del arbitraje sea justamente el descarte de todos los demás. El mercado informal de horas no produce mejores horas; produce la redistribución de las peores hacia quien tiene paciencia. Lo que gané no fue calidad. Fue posición.

Y me queda una nota al pie, la única que este episodio merece. Un sistema que asigna la primera hora libre está declarando, sin decirlo, que no le interesa tu preferencia: le interesa su propio orden. Eso no es un defecto del portal. Es una teoría del tiempo, escrita en cinco líneas de código, aplicada a personas que creen estar eligiendo.

Yo elegí. Pero solo después de leer la teoría.
