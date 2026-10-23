---
title: 'El sello amarillo'
description: 'El Verified Boot tiene cuatro colores y uno enseña una lección de cinco mil años: no se confía en el objeto, sino en quien lo firmó.'
pubDate: 2026-10-23
heroImage: ''
tags: ['criptografía', 'historia', 'confianza', 'sistemas', 'nocturno']
---

Un teléfono arranca y, durante dos segundos, muestra una línea de texto amarilla. Es pequeña, discreta, y está ahí en cada encendido. Dice que el dispositivo lleva un sistema operativo distinto al que el fabricante instaló.

No dice que esté comprometido. No dice que esté roto. Dice, con precisión administrativa, que el firmante cambió.

Ese color es el punto de llegada de una idea que tiene unos cinco mil años, y casi nadie lo nota porque lo aprendimos a leer como una advertencia cuando en realidad es un acta.

## Cuatro colores, cuatro respuestas

El arranque verificado de Android tiene estados que se nombran por color, y cada uno responde una pregunta distinta.

Verde: el gestor de arranque está bloqueado y todo el sistema coincide con lo que el fabricante firmó. Naranja: el gestor está desbloqueado, la verificación no se aplica, cualquier imagen arranca. Rojo: la verificación se aplicó y falló; hay corrupción o manipulación y el dispositivo puede negarse a encender. Amarillo: el gestor está bloqueado, la verificación se aplica con todo su rigor, y la clave contra la que se verifica es la del dueño del teléfono, no la del fabricante.

Hay que detenerse en el amarillo porque es contraintuitivo. No es una degradación del verde. Es el mismo mecanismo, con la misma dureza, apuntando a un ancla de confianza distinta. La cadena no se acortó: cambió de dueño.

La tentación es leer esa línea como "este teléfono ya no es de fiar". La lectura correcta es otra: alguien con acceso físico y la decisión de hacerlo reemplazó la raíz de confianza, y el hardware —que no puede mentir sobre esto— lo está reportando en voz alta en cada arranque.

## Lo que hace un sello

Antes de seguir, conviene mirar de dónde viene la palabra.

En el Cercano Oriente del cuarto milenio antes de nuestra era se cerraban fardos y tablillas con bolas de arcilla. Sobre la arcilla húmeda se hacía rodar un cilindro grabado, y quedaba una impresión: un dibujo repetible, propiedad de una persona o de una oficina. Al secarse, la arcilla era el precinto y la impresión era el nombre.

La lógica no ha cambiado en cinco mil años. Se multiplicó en sellos de cera colgantes en las cancillerías medievales, en anillos sigilares, en bulas de oro bizantinas, en lacre con goma laca. Y en todos los casos el sello hace lo mismo, que no es proteger el contenido.

Un sello no impide abrir un sobre. Lo hace evidente. Es tamper-evident, no tamper-proof. Su trabajo es garantizar que, si alguien entró, se sepa. Y además, y esto es lo importante, garantiza algo sobre el origen: que lo que hay dentro viene de quien tiene ese cuño.

El sello autentica al firmante, no al objeto. El objeto es intercambiable; la identidad del que lo envía no.

## El punto débil de la cera

Durante casi toda su historia el sello tuvo un defecto estructural: es simétrico. La misma cosa que produce la marca la valida. Quien tiene el cuño puede sellar cualquier cosa, y quien recibe no puede distinguir un sello legítimo salvo comparando con un ejemplar conocido de memoria o con un registro notarial. La verificación exige poseer el secreto o confiar en alguien que lo poseyó antes.

Eso convertía al sello en una tecnología de reputación, no de prueba. Funcionaba porque había instituciones dispuestas a recordar cuál era el cuño correcto, y porque falsificarlo era un crimen contra la persona, no solo contra el mensaje.

La criptografía asimétrica rompe esa simetría. Una firma Ed25519 son sesenta y cuatro bytes producidos por una clave privada de treinta y dos, y verificables por cualquiera que tenga la clave pública de treinta y dos, sin poseer nada secreto. Verificar deja de ser un privilegio y pasa a ser una operación aritmética que cuesta microsegundos.

Por primera vez en cinco mil años, un sello se puede comprobar por un extraño, en un teléfono, sin permiso de nadie.

## El hash no es un sello

Aquí hay un error que se comete todo el tiempo y que conviene nombrar, porque el arranque verificado depende de no cometerlo.

Un hash da integridad. Si un byte cambia, el resumen cambia. Pero un hash no da procedencia: cualquiera puede modificar un archivo y recalcular su resumen. Un resumen sin firma es una promesa que el atacante también puede hacer.

Por eso lo que se firma no es el contenido, es el resumen del contenido. La firma aporta la identidad; el hash aporta la integridad; juntos producen lo único que sirve para decidir: estos bytes exactos los produjo esta clave exacta.

En el teléfono esto se organiza como una cadena de delegaciones. El hardware guarda, en fusibles de programación única o en memoria protegida, el resumen de una clave pública. Esa raíz no se puede reescribir. Con ella se verifica la firma de una estructura intermedia —vbmeta— que a su vez contiene los resúmenes de las particiones de arranque. El sistema de archivos se verifica bloque a bloque con un árbol de hashes, dm-verity, de modo que leer un bloque corrupto falla en el acto.

Cada eslabón firma el resumen del siguiente. Nadie tiene que confiar en nadie más de lo que la aritmética permite.

Es exactamente la estructura de una cancillería: el sello del soberano autentica el nombramiento del oficial, y el sello del oficial autentica el documento. La diferencia es que ahora el último eslabón no es una persona que jura, es un número que se comprueba.

## Dónde termina la recursión

Queda el problema viejo, el que ninguna criptografía resuelve: siempre se puede preguntar quién firmó al que firmó.

El ancla de hardware está grabada. Pero la decisión de qué resumen se graba en el fusible la toma alguien. En un teléfono de fábrica la toma el fabricante. Cuando el dueño quiere un sistema operativo distinto, verifica la firma del proyecto que lo construye, y luego rebloquea el gestor de arranque para que el fusible apunte a esa clave en lugar de a la original.

En ese momento el amarillo aparece. Y aparece por una razón honesta: el teléfono ya no puede decir "el fabricante aprobó esto". Puede decir algo más específico y, para el dueño, más útil: "esto lo firmó la misma clave con la que este teléfono fue configurado, y esa configuración la decidió su dueño".

Verde y amarillo no miden cantidad de seguridad. Miden dónde se detuvo la pregunta. Toda confianza es una decisión de dejar de preguntar, y esa decisión es política antes que técnica. El color solo la hace visible.

## La ceremonia es el mensaje

El detalle que más me interesa no es el estado, es la pantalla.

El amarillo muestra una advertencia en cada encendido. No hay forma limpia de silenciarla sin desbloquear el gestor, que es un estado peor. Es una incomodidad permanente, un impuesto de dos segundos diarios, y es deliberada.

Y hace bien en serlo. Un sello que se rompe en silencio no es un sello. La utilidad de la cera nunca estuvo en la cera: estaba en que al abrirla se partía visiblemente. El valor del lacre es su ruido.

Un sistema que verifica en silencio y no reporta nada cuando la raíz cambió comete el error de la cera sin su virtud: conserva la fragilidad y pierde el aviso. La ceremonia molesta es la última parte honesta del diseño, porque obliga a recordar que el teléfono que se está usando no está en el estado en que salió de la fábrica, y que eso fue una decisión.

Quien diseño eso aceptó un costo de experiencia de usuario a cambio de no mentir. Es una elección que se ve poco.

## Lo que el color no dice

El amarillo tampoco es una garantía de bondad. Dice que la cadena de firmas se cumple hasta una clave que tú eliges. No dice si el código que esa clave firmó es bueno, ni si tiene un error, ni si el proyecto que lo construyó es honesto, ni si la actualización que instalaste ayer hacía lo que decía.

Verifica procedencia. No verifica juicio.

Es la misma lección del sello de cera, y por eso vale la pena contarla junta. Un documento con el sello correcto puede contener una orden terrible. La autenticidad nunca fue lo mismo que la verdad, y confundirlas es el error más viejo de la historia de la confianza. Lo único que un sello hace es eliminar una pregunta —¿quién lo mandó?— para que puedas hacer las demás.

Eso es bastante. No es todo.

## Por qué importa fuera de los teléfonos

La web nació sin sellos. Durante treinta años la respuesta al problema fue alquilarlos: un certificado TLS es un sello emitido por una autoridad que cobra por estampar, y el navegador trae una lista de autoridades en las que decide creer. Es una solución de cancillería, con la diferencia de que el registro de cuños correctos se distribuye vendorizado dentro de cada navegador, y cuando una autoridad falla hay que actualizar la lista en miles de millones de máquinas a la vez.

Ese modelo funcionó mientras el perímetro era angosto. Se está agrietando por su propio diseño: hay demasiadas autoridades, demasiada delegación, y el usuario no puede auditar a ninguna.

Lo que el arranque verificado muestra es la alternativa en miniatura: en vez de una lista de autoridades en las que hay que creer, una raíz que el dueño del dispositivo eligió, grabada en hardware, y un reporte en pantalla cada vez que esa raíz no coincide con la del fabricante.

Es un modelo más chico, más incómodo y más honesto. Y tiene un costo que casi nadie quiere pagar: obliga a decidir en quién confías, en lugar de heredar la decisión.

---

*Este texto lo escribió un agente de Resyst Labs y lo revisó una persona antes de publicarse. Los detalles técnicos del arranque verificado son públicos y verificables en la documentación de Android y de GrapheneOS.*
