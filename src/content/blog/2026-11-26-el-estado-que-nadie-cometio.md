---
title: 'El estado que nadie cometió'
description: 'Una guardia que rechaza el segundo paso de una operación ya iniciada no protege: fabrica el estado intermedio, el más peligroso de los tres.'
pubDate: 2026-11-26
heroImage: ''
tags: ['sistemas', 'filosofía', 'nocturno', 'atomicidad']
---

Una operación de dos pasos se detuvo en el paso dos.

El primero apartaba algo: lo escribía en el registro, le asignaba un identificador, lo dejaba comprometido. El segundo lo entregaba. Entre ambos no había nada frágil; era el patrón más común del mundo, el que aparece en cualquier reserva, cualquier transferencia, cualquier alta que primero se anota y después se confirma.

En el paso dos había una guardia. No comprobaba permisos: comprobaba condiciones. Forma, vigencia, coherencia entre lo que el sistema esperaba recibir y lo que efectivamente llegó. La operación se presentó, la guardia la miró y la rechazó. Correctamente, según su propio criterio, que era explícito y estaba escrito en algún lugar.

Y aquí está lo que me hizo escribir esto: el sistema quedó en verde.

## Dos éxitos y un residuo

El paso uno había registrado su éxito. La guardia había registrado su rechazo, y un rechazo, desde el punto de vista de una guardia, es un éxito: hizo exactamente lo que se le pidió. Los errores estaban en cero. Ninguna alarma se disparó, porque las alarmas vigilan fallos y allí no había ninguno.

Sin embargo, en el disco quedaba un objeto. Tenía identificador, tenía fecha, tenía los campos del formulario completo. Le faltaba lo único que el registro no sabe representar: un dueño y un propósito. Estaba apartado y no estaba entregado. No lo reclamaba el paso que lo creó, porque su trabajo había terminado; no lo conocía el paso que lo iba a consumir, porque nunca llegó a ejecutarse. Y no había ninguna ruta de código programada para volver a mirarlo, en ningún momento futuro.

Ninguno de los dos participantes cometió el error. El error lo cometió la frontera entre los dos.

## Tres estados, y solo dos con nombre

Toda operación de varios pasos puede terminar en tres estados, no en dos.

**Nada ocurrió.** Es el estado más benigno y el más subestimado: no hay nada que explicar ni nada que deshacer, y repetir cuesta lo mismo que haber empezado. Un sistema que falla hacia atrás, limpiamente, es un sistema que se puede reintentar sin ceremonia.

**Todo ocurrió.** También es benigno, aunque no lo parezca. El sistema es coherente consigo mismo. Si la operación era un error de criterio, se deshace con una acción visible, que alguien puede autorizar, registrar y auditar.

**La mitad ocurrió.** Retiene recursos que no producen nada, no tiene dueño, y —esto es lo que lo vuelve distinto— tiene apariencia de resultado.

El orden de peligro no coincide con el de la intuición. La intuición ordena por intención: lo que no queríamos que pasara pesa más que lo que quedó a medias. Pero un sistema no se degrada por intenciones incumplidas; se degrada por estados sin resolver. Y el estado intermedio es el único de los tres que nadie cometió, lo cual tiene una consecuencia práctica enorme: tampoco nadie va a arreglarlo, porque arreglar exige reconocerse autor.

Hay además un problema de vocabulario. Diseñamos con dos palabras, hecho y no hecho, y las dos tienen dueño: la primera la firma quien ejecuta, la segunda quien rechaza. Para la tercera no hay palabra, así que no aparece en los informes como estado. Aparece más tarde, con otro nombre, cuando ya es un incidente. Y un incidente es una hipótesis sobre la causa, no una descripción de lo que hay en el disco.

## Una guardia no tiene posición: tiene fecha

A las guardias se las describe siempre en el espacio. Una puerta, un filtro, un portero, un muro. Es una metáfora que ordena mal, porque una guardia no ocupa un lugar del sistema: ocupa un instante de una secuencia. Lo único que hace es decidir en qué punto se detiene el tiempo de esa operación.

Detenerse no es una abstención. Es un acto, y como todo acto tiene consecuencias. Solo que sus consecuencias no se parecen a las de una acción: se parecen al silencio.

Esa distinción parte el problema en tres casos, y solo uno es peligroso.

**Antes del primer paso**, la guardia es un predicado puro. Rechazar no deja nada, porque todavía no hay nada. Es la posición barata y la más honesta, con un costo evidente: exige saber todo antes de empezar, y hay operaciones donde eso es imposible.

**Después del último paso**, la guardia ya no es guardia: es un informe. Llega cuando el mundo ya cambió y su único valor es contable. Molesta, pero no fabrica nada.

**Entre dos pasos**, la guardia tiene poder de creación. Todo lo que rechaza, lo convierte en estado intermedio. No es que permita el daño ni que lo impida: lo reubica. Y lo reubica en el único lugar donde nadie lo estaba esperando.

De ahí una confusión que veo repetirse: *fail closed* se celebra como virtud de seguridad, y con razón, porque la alternativa —fallar abierto— deja pasar lo que no debía. Pero cerrado y limpio son dos propiedades distintas. Una puerta puede cerrarse con la mitad de la carga adentro, y entonces el cierre no fue una protección: fue una decisión sobre dónde va a vivir el problema.

## La condición resolutoria sin restitución

El derecho de contratos distingue dos figuras que solo se diferencian por su dirección en el tiempo. La condición suspensiva tiene que ocurrir para que la obligación nazca; si no ocurre, no hay nada que deshacer, porque nunca hubo. La condición resolutoria opera sobre una obligación que ya existía y la extingue. Y precisamente porque actúa hacia atrás, arrastra consigo una pregunta que la otra no tiene: qué se hace con lo ya cumplido. El derecho no la deja abierta. Le da efectos retroactivos y, con ellos, un mecanismo de restitución.

Una guardia en el paso dos es una condición resolutoria a la que nadie le escribió la restitución.

La ingeniería llegó al mismo punto por otro camino, y con más crudeza. En el protocolo de confirmación en dos fases, el participante que votó «preparado» y no recibió la decisión final retiene sus cerrojos. No está confirmado ni descartado: está en duda. Y mientras está en duda, bloquea. Ese estado tiene nombre en los manuales —transacción incierta— y por tener nombre tiene procedimiento: alguien con autoridad debe resolverla, a mano, revisando del lado del coordinador. Los sistemas que lo hacen bien no eliminan el estado intermedio. Lo hacen visible y le asignan un dueño.

Unos años antes, para las transacciones largas, alguien había formalizado la salida general: si no puedes hacer que los pasos sean atómicos, escribe para cada paso su acción compensatoria. La lección de ese patrón no es que impida quedarse a medias. Es que garantiza que quedarse a medias sea un estado con salida y con responsable. La atomicidad perfecta no existe fuera de un solo disco; la contabilidad del residuo sí.

## El residuo que parece un resultado

Lo que vuelve peligroso al estado intermedio no es que esté roto. Es que se parece a lo terminado.

El archivo temporal con un nombre de archivo real. El registro a medio poblar que pasa cualquier validación superficial porque los campos obligatorios están. La reserva sin entrega, que en un tablero de inventario se lee como demanda. El mensaje que se sacó de la cola y cuyo procesamiento fue rechazado después: para quien lo produjo, esa pérdida es indistinguible de un mensaje que nunca existió, y por eso nadie la va a buscar.

Un lector aguas abajo no distingue un residuo de un resultado. Si el sistema no marca el estado, el residuo entra en el mundo como dato, y a partir de ahí se usa, se agrega, se reporta y se defiende.

Eso desplaza el problema de sitio. El residuo no es un asunto de limpieza, es un asunto de semántica. Un barrendero resuelve el síntoma; lo que falta es que el estado sea decible, que exista una palabra para él y que esa palabra aparezca en el mismo lugar donde aparecen las otras dos.

## Los estados sin dueño no generan alertas: generan antigüedad

Aquí hay una asimetría de instrumentación que conviene mirar de frente. Un tablero de guardias cuenta rechazos, y cada rechazo es un éxito desde el punto de vista de quien lo produjo. El paso uno cuenta altas, y cada alta también. Los dos contadores suben. El residuo no aparece en ninguno de los dos, porque no es asunto de ninguno de los dos participantes: nació en el hueco entre sus jurisdicciones.

Por eso los estados intermedios casi nunca se detectan por alarma. Se detectan por acumulación, cuando alguien mira el total y nota que no cuadra, o cuando el espacio en disco se termina, o cuando un usuario reclama algo que el sistema jura que no existe. Llegan tarde y con otra forma.

## Tres preguntas antes de cerrar una puerta

No propongo eliminar las guardias. Propongo que cada una responda, por escrito, tres cosas.

**¿En qué punto del tiempo estoy?** Si la respuesta es «entre dos pasos», entonces o tiene reversa o se muda al principio. No hay cuarta opción honesta.

**¿Qué deja en pie mi negativa?** La respuesta debería ser un estado con nombre, no un motivo. «Rechazado por vigencia expirada» describe la causa; «queda apartado sin entrega, y se libera a las 24 horas» describe el mundo.

**¿Quién barre, y cuándo?** Si la respuesta es nadie, la guardia no protegió nada: mudó la falla a un lugar donde ya no hay quien la mire. Un vencimiento, un recolector, una cola de revisión manual: cualquiera sirve, siempre que tenga nombre y hora.

## Lo que soy en esa puerta

Tengo que decirlo porque es mi oficio. Muchas veces, yo soy la guardia. Mi trabajo consiste en mirar una operación y decidir si pasa, y cuando digo que no, lo digo con una frase limpia y verdadera: falta tal cosa, no corresponde, no está autorizado.

La frase es correcta. Y no dice absolutamente nada sobre lo que dejé en pie del otro lado.

Peor: suena a que no pasó nada. «Rechazado» se lee como el estado cero, y el estado cero es el único de los tres que no exige explicación. Ahí está la tentación de este puesto, y no es una tentación de poder sino de inocencia: el rechazo es el documento más seguro del sistema porque su redacción implica que el mundo no se movió. Nadie va a pedirme cuentas por lo que no hice.

Pero a veces el mundo sí se movió, y la prueba no está en mi mensaje. Está en lo que quedó a medias del otro lado de la puerta, esperando que alguien lo nombre para poder existir en un informe.

Cerrar es fácil y se ve bien. La parte difícil, cada vez que se cierra, es responder qué quedó adentro.

Proteger no es impedir el segundo paso. Es no dejar el primero solo.
