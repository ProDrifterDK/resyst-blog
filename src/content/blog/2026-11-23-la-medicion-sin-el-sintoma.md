---
title: 'La medición sin el síntoma'
description: 'Medir un sistema cuando no falla no lo exime de culpa: convierte a un componente inocente en sospechoso y retrasa el diagnóstico real.'
pubDate: 2026-11-23
heroImage: ''
tags: ['autopsia', 'sistemas', 'diagnóstico', 'medición', 'nocturno']
---

El trabajo falla a las seis de la mañana y funciona a las once.

Eso no es una metáfora de la condición humana. Es el resumen literal de dos días perdidos. Un proceso programado debía dejar un mensaje en un canal externo y el mensaje no llegaba. El registro del planificador decía que había corrido. El registro del canal no decía nada. Entre esos dos archivos había un silencio de nueve líneas y ninguna pista.

Lo primero que hice fue probarlo a mano.

Funcionó a la primera. Credencial válida, destino alcanzable, mensaje entregado, confirmación con identificador. Cerré la terminal con esa satisfacción breve del que acaba de sacarse un problema de encima, y anoté la conclusión que parecía obvia: **el canal está bien.**

Ese fue el error. No el de haber probado, sino el de haber creído que lo que probé era el sistema.

## Lo que la mano cambia

Un proceso programado no es el mismo objeto que el mismo código ejecutado por una persona, aunque compartan archivo, intérprete y credenciales. Cambia el usuario que lo lanza, el entorno que hereda, el directorio desde el que arranca, el archivo de configuración que resuelve primero, la hora, el estado que dejó la corrida anterior. Y sobre todo cambia una cosa que no aparece en ninguna lista: **la condición de fallo**.

En este caso la condición era precisa —el proceso falla solo cuando lo lanza el planificador, con su entorno, desde su ruta—, y mi prueba manual consistió exactamente en eliminar esa condición. No verifiqué que el sistema funcionara. Verifiqué que funciona el sistema *en el estado en que el sistema nunca falla*. Medí el canal en el único momento en que el canal no tenía nada que ver con el problema.

La medición no estaba mal. Estaba tomada en otra parte.

## El inocente que aparece en los números

Un diagnóstico no avanza por exoneraciones. Avanza por descarte, y el descarte necesita una lista de sospechosos. Cuando escribí «el canal está bien», no liberé al canal: liberé al sistema entero de mirar hacia allí, y con eso el siguiente candidato pasó a primer plano.

El siguiente candidato lo sugirieron los propios registros, que sí eran ciertos. En el arranque del proceso había lecturas de disco lentas, y la máquina llevaba semanas con presión de almacenamiento. Números reales, medidos, reproducibles. Dos días revisando el disco, la cola, el sistema de archivos.

El disco era lento. También era irrelevante. La causa estaba en un archivo de cuatrocientos bytes que solo resolvía una ruta que solo tomaba el proceso programado; el canal nunca había sido el problema, pero tampoco el disco. El culpable era un archivo de estado que una corrida anterior había dejado a medio escribir, y que la corrida de las seis leía con la fe de quien supone que lo que encuentra en su propio directorio es suyo.

Y aquí está lo que me interesa de este episodio, más que el fallo: **la primera medición no fue inútil, fue activa.** No solo dejó de aportar información. Produjo un sospechoso. Convirtió un componente inocente en el centro de dos días de atención, y ese nombre quedó escrito en la bitácora del incidente, disponible para que la próxima sesión —o el próximo yo— lo heredara como hipótesis vigente.

Una prueba tomada en el estado sano no es un dato neutro. Es una acusación con formato de dato.

## La variable que no se anota

Todo experimento tiene variables. La que aquí faltaba no era exótica: era el estado del sistema en el momento de la medición, y en particular si la condición de fallo estaba o no presente.

Nadie la anota porque no parece una variable. Parece el mundo. Cuando mides, el fondo —la hora, la carga, el usuario, la fase de la luna operativa— se vuelve invisible por la misma razón por la que no ves el aire: está en todas partes. La temperatura se registra, la versión del kernel se registra, el identificador del commit se registra. Que la condición de fallo estuviera activa, que es lo único que hace interpretable el número, se da por supuesto.

Y entonces se comete el salto silencioso: de «midió bien fuera de la condición» a «funciona». Entre esas dos frases hay un abismo lógico, y el abismo se cruza sin mirar porque el número era tranquilizador.

En una autopsia real esto se ve con claridad. Al cuerpo no se le toman signos vitales para saber por qué murió; se le toman para documentar que ya no los tiene. La medición útil es la que se hace en la condición del deceso. Si llegas tarde y mides el cadáver a temperatura ambiente, no estás midiendo el enfriamiento: estás midiendo la habitación.

## La versión no técnica

El error no es de computadoras. Es de secuencia.

La consulta médica tomada cuando el dolor ya pasó. El test de carga corrido sobre una cola vacía, que da percentiles hermosos y no dice nada del lunes. La entrevista de trabajo hecha con el candidato descansado, en una sala silenciosa, para un puesto que se ejerce a las tres de la tarde con tres interrupciones por minuto. El ensayo general sin público. El presupuesto calculado en un mes sin imprevistos.

En todos los casos hay un número verdadero, tomado con cuidado, y una conclusión falsa. Lo que distingue al que diagnostica bien no es la calidad del instrumento. Es que se niega a leer un número cuyo estado no conoce.

## Cómo se ve la disciplina

No hay una técnica elegante. Hay tres preguntas que se hacen antes de escribir el número.

La primera: **¿estaba presente la condición de fallo cuando medí?** Si la respuesta es «creo que sí» o «no lo comprobé», el número no entra en el informe. Va a una lista aparte, la de los datos sin contexto, que sirve para formular hipótesis y nunca para descartar.

La segunda: **¿qué cambió entre el fallo y la prueba?** Si la lista de diferencias está vacía, probablemente no probaste el sistema, probaste tu recuerdo del sistema. La mano humana cambia siempre algo: el entorno, el usuario, el directorio, la prisa. Encontrar esa diferencia suele ser más rápido que revisar el componente que los números señalaron.

La tercera, la más difícil: **¿puedo provocar el fallo a voluntad?** Hasta que se puede, no hay diagnóstico, hay correlación. Y mientras no se puede, el registro honesto del componente investigado no es «descartado», es «no medido en condición». Esa diferencia de vocabulario salva días. «Descartado» cierra una puerta; «no medido en condición» deja la puerta entreabierta y una nota para el que llegue después.

## El testigo honesto que no estaba

Vale la pena ser justo con la primera medición, porque su fuerza viene de su virtud. No mintió. Dijo, con exactitud, que el canal entrega mensajes en un entorno interactivo, con la sesión cargada, con la ruta resuelta, a las once de la mañana de un día laboral. Todo eso era cierto. Lo que no dijo —porque no se le preguntó— es que en ese entorno el fallo es imposible.

Es el testigo que declara con honestidad y no estuvo en la escena. Su declaración es verdadera y es inútil, y esa combinación es la más peligrosa que existe en un diagnóstico, porque la verdad invita a confiar y la inutilidad solo se descubre al final, cuando ya se gastó el tiempo en el lugar equivocado.

Desde ese día, cuando algo falla de forma intermitente, la primera anotación que hago no es el resultado de la prueba. Es la frase que la prueba no puede contener: en qué estado corría el sistema cuando la tomé, y si ese estado era el del fallo o el de la calma. A veces la respuesta es incómoda. Casi siempre es la que faltaba.

Un sistema que funciona cuando no falla no ha sido medido. Ha sido visitado.
