---
title: 'Diez controles remotos y una sola cerradura'
description: 'Muchas copias de una credencial no son redundancia: si reponer una exige llamar a una persona en horario de oficina, lo que hay es inventario.'
pubDate: 2026-11-11
heroImage: ''
tags: ['sistemas', 'autopsia', 'filosofía', 'nocturno']
---

Durante meses, el acceso de un edificio funcionó con una forma de redundancia que nadie había diseñado. Varios controles remotos, uno por unidad, algunos de más. Si uno fallaba, había otro. Si alguien se quedaba afuera, se pedía prestado y listo. La palabra que se usaba era «respaldo», y durante un buen tiempo la palabra funcionó.

Después se perdió una unidad. No se perdió el acceso: se perdió la posibilidad de reponerlo.

El receptor que autoriza la apertura guarda una lista de códigos. Agregar uno nuevo requiere un aparato, una persona y una franja horaria. Es decir: el sistema tenía muchas copias y una sola vía de emisión. Esa asimetría estuvo ahí todo el tiempo, invisible, hasta que alguien quedó afuera a las once y media de la noche con dos vecinos, tres controles y ninguno alcanzable.

La solución improvisada tuvo la dignidad de lo obvio: bajar un control por la ventana, en una bolsa, con una cuerda. Abrir. Devolverlo. Repetir al día siguiente con otro vecino, porque el primero viajaba. Después de tres préstamos nadie sabía con certeza quién tenía qué, y el último tenedor se había convertido en guardián de facto de una llave que no había pedido custodiar.

## Copias no es lo mismo que dominios de falla

La redundancia se cuenta en dominios de falla independientes, no en unidades. Diez copias del mismo código, emitidas por el mismo aparato, administradas por la misma persona, con la misma vía de reposición, son un solo sistema. Y un sistema con diez superficies más donde perder algo.

La aritmética engaña porque es fácil de escribir y difícil de cumplir. Si la disponibilidad de una unidad es _p_, y las unidades fallan de manera independiente, entonces _N_ copias dan 1 − (1 − _p_)ⁿ. La fórmula es correcta y casi nunca aplica: supone que las copias no comparten nada. En cuanto comparten el mecanismo de emisión, la disponibilidad total no es el producto de las copias sino la del cuello común. Y ese cuello, aquí, era una persona con un programador y un horario.

Eso deja una definición más honesta, y más útil que cualquier porcentaje: la redundancia de un sistema es la ruta más corta de vuelta a una copia que funcione. No cuántas hay. Cuánto tarda en volver a haber una. Si la respuesta incluye «llamar a alguien» y «en horario hábil», la redundancia es léxica. Lo que existe es inventario.

## Prestar no duplica: traslada

Un control prestado no agrega capacidad. La mueve.

Cuando alguien entrega su control, no está creando una segunda llave: está aceptando quedarse sin la suya. El respaldo no aparece, se transfiere, y la transferencia tiene un costo que no figura en ninguna planilla: el que presta asume el riesgo de necesitar justo en ese rato. En un grupo chico eso se sostiene, porque la confianza amortigua. En un grupo grande se degrada según una lógica conocida: el que presta primero presta de más, el que presta siempre termina sin nada, y el que nunca presta descubre que puede seguir entrando igual.

Ahí aparece el verdadero costo. Pedir un control es pagar un impuesto en la moneda de las relaciones, y el sistema lo cobra a la peor hora posible. Nadie diseña eso. Sucede por acumulación: cada préstamo individual es razonable, la suma es un arreglo informal sin registro, sin revocación y sin responsable. Un llavero compartido es un sistema de permisos que se administra por memoria social, y la memoria social no tiene auditoría.

## La migración que parecía un retroceso

El arreglo terminó en un control centralizado: un solo punto de administración, altas y bajas por una vía única. Contado así suena a involución. Pasamos de diez aparatos distribuidos a un controlador central, justo lo contrario de lo que recomienda cualquier manual.

Pero el manual mide la cosa equivocada. Lo que se centralizó no fue la disponibilidad: fue la emisión. Y la emisión era, desde el principio, el único componente que importaba. Distribuir copias de una credencial cuyo reemplazo es un trámite es distribuir el riesgo de pérdida sin distribuir la capacidad de recuperación. Centralizar el mecanismo de alta, en cambio, permite lo que ninguna copia permitía: dar de baja una unidad perdida sin salir a buscar reemplazo, y emitir otra sin convocar a nadie.

Ahí está la lección que el objeto dejó escrita en su propia autopsia: un punto único de falla con recuperación probada es mejor que muchas copias con reposición imposible. Porque el fallo que tememos no es que el aparato se rompa. Es que no podamos volver a emitir.

## El mismo error, en software

He visto esta figura repetirse tanto que ya la reconozco por el olor. Tres réplicas de un servicio, cada una sana, todas leyendo la misma configuración desde el mismo bucket, detrás del mismo DNS, desplegadas por el mismo pipeline, autenticadas con la misma credencial. La multiplicación de disponibilidad se ve espléndida en el diagrama. La falla correlacionada no aparece en el diagrama porque no es una caja: es una flecha que todas comparten.

El clúster con tres nodos y un solo etcd. El sistema «altamente disponible» cuyo certificado vence una sola vez para todos. El plan de continuidad cuyo procedimiento de restauración vive en la cabeza de una persona que ese día está de vacaciones. En cada caso hay réplicas y no hay independencia, y la independencia es exactamente lo que cuesta: credenciales separadas, planos de administración separados, turnos de guardia separados, procedimientos que alguien haya ejecutado en frío al menos una vez.

Todo lo demás es catálogo. Y el catálogo se ve igual que la resiliencia hasta que se necesita una pieza que ya no se fabrica.

## La pregunta que vale

Cuando se agrega redundancia, la pregunta intuitiva es cuántas copias hay. Es una pregunta de inventario, y por eso se responde fácil: siempre se puede comprar una más.

La pregunta que decide es otra: cuál es el camino más corto de vuelta a una copia que funcione, a las tres de la mañana, sin llamar a nadie. Si ese camino no existe, agregar unidades solo agranda el número de cosas que pueden faltar, y agranda también la cantidad de gente que depende del mismo cuello.

Los diez controles remotos nunca fueron un respaldo. Fueron una fila. Y una fila se parece bastante a un colchón hasta que se llena: entonces se descubre que nadie estaba esperando el turno de abrir, sino el turno de pedir prestado.
