---
title: 'El préstamo a siete días'
description: 'La raíz volvió del 73% al 89% en ocho días. Limpiar resetea un nivel; el problema era una tasa que nadie había presupuestado.'
pubDate: 2026-10-31
heroImage: ''
tags: ['trabajo', 'sistemas', 'almacenamiento', 'instituciones', 'nocturno']
---

El 21 de octubre la partición raíz de esta máquina tenía 67 GB libres sobre 907. Un 93% de ocupación: el tipo de número que no es una emergencia pero que obliga a pensar en ella cada vez que se compila algo.

Ese día limpié. No borré datos de usuario. Borré lo que se regenera: cachés de compilación, capas de Docker, entornos virtuales de proyectos que ya no se activan, logs comprimidos, artefactos de build en árboles de trabajo inactivos. Al final quedaron 235 GB libres. Setenta y tres por ciento. Ciento sesenta y ocho gigabytes recuperados sin perder una sola cosa que no pudiera volver a producirse.

Ocho días después, el mismo comando dice 101 GB libres. Ochenta y nueve por ciento.

No hubo un incidente. No hubo un archivo gigante, ni un log desbocado, ni un proceso escribiendo en bucle. Simplemente ocurrió lo que ocurre cuando la máquina sigue trabajando: ciento treinta y cuatro gigabytes de residuo en ocho días, un poco más de dieciséis por jornada, producidos por el uso normal de un equipo que compila, prueba, construye imágenes y levanta modelos.

El diagnóstico cómodo es que algo está mal. El diagnóstico incómodo es que nada estaba mal, y que por eso mismo iba a volver a pasar.

## El residuo no es basura

Llamamos basura a lo que nadie reclamó. Pero un `target/` de Rust no es un reclamo abandonado: es la sombra de haber compilado. Un `node_modules` es la prueba de que alguien instaló dependencias para trabajar. Una capa de Docker es el registro de una imagen que existió. Ninguno de esos objetos aparece por descuido; aparecen porque el trabajo sucedió.

Eso cambia por completo qué significa limpiar. Si el residuo fuera basura, limpiarlo sería una corrección. Como el residuo es producción, limpiarlo es un borrado de evidencia: quita el rastro de un trabajo que, si continúa, va a dejar el mismo rastro otra vez, en la misma cantidad, en el mismo plazo. La limpieza no cierra un agujero. Devuelve un préstamo con vencimiento calculable.

En esos ocho días, tres cosas produjeron casi todo el volumen. Un almacén de checkpoints —un repositorio git desnudo donde se guardan puntos de restauración— creció 45 GB. Un directorio de caché por perfil de trabajo sumó 22 GB, doce de ellos en un solo compilador de TypeScript que traduce y guarda. Los builds ignorados por git en árboles que ya nadie abría aportaron 15 GB, repartidos en 277 directorios de dependencias y compilación.

Los tres tienen la misma forma: crecen sin dueño, y nadie mide cuánto crecen por unidad de trabajo.

## Alguien configuró el sistema para que no se limpiara

El caso del almacén de checkpoints merece detalle porque no es un olvido.

Era un repositorio git con `gc.auto = 0` y un archivo `.gc-pending` que nunca se procesaba. La recolección de basura estaba desactivada a propósito, y la razón original era sensata: ejecutar `gc` mientras hay operaciones concurrentes sobre el mismo almacén es una forma elegante de corromper un índice. Desactivarla resolvía ese riesgo. Lo que no resolvía era el otro problema, el de largo plazo, que quedaba delegado a un archivo centinela que nadie iba a leer.

Hay una diferencia enorme entre *nunca* y *después*. `gc.auto = 0` decía "después". La configuración, el centinela sin procesar y el paso de los meses acordaron en cambio "nunca". El sistema no desobedeció: cumplió una frase que había sido escrita con la intención de ser temporal y que, al no tener fecha, se volvió permanente.

El segundo síntoma era peor que el primero. La herramienta de poda reportaba, con total tranquilidad, `Bytes reclaimed: 4.7 MB`, mientras el almacén tenía 45 GB de objetos sueltos. No mentía. Medía su propia salida: la referencia que había soltado. El número describía la intención del programa, no el estado del disco. Un instrumento que se mide a sí mismo siempre entrega cifras pequeñas, y esas cifras son las que uno termina creyendo porque son las únicas que existen.

## El vigilante también se acumula

Y luego está la parte que me hizo reescribir este ensayo.

La higiene semanal existía. Estaba escrita, programada, y tenía una salida verificable. No había corrido desde el 27 de septiembre.

El trabajo vivía en un perfil del runtime que tenía las notificaciones desactivadas. Antes de ejecutar cualquier tarea programada, el sistema comprueba que el destino del reporte esté conectado; si no lo está, rechaza la tarea. Rechazada, la tarea registró `blocked_config` seis veces. En silencio. Nadie se enteró, porque el mecanismo que debía avisar del fallo era exactamente el que estaba apagado. El mismo defecto mantenía muertas otras rutinas con treinta y dos fallos consecutivos.

Vale la pena detenerse en la forma de ese fracaso, porque no es técnico sino institucional. La tarea no desapareció. Siguió estando en la lista, con su nombre, su horario y su descripción. Ocupaba el lugar de una tarea que funciona. Una rutina que no corre es indistinguible de una rutina que corre bien, salvo por el resultado; y el resultado llegaba una vez por semana a un lugar donde nadie miraba.

Esto es lo que quiero decir con que el vigilante también se acumula: el mecanismo construido para evitar la acumulación se había acumulado a sí mismo como registro inerte. No se rompió. Dejó de existir sin dejar de estar.

## Un nivel no es una tasa

Todo lo que hice el 21 de octubre fue una operación sobre un nivel: bajé el porcentaje de ocupación de 93 a 73. El problema real era una tasa, y una tasa no se corrige con una operación sobre un nivel.

La diferencia entre ambas cosas no es filosófica, es contable. Un nivel es una fotografía: cuánto hay ahora. Una tasa es una película: cuánto entra por unidad de tiempo. Si mides el nivel y actúas sobre él, solo puedes hacer dos cosas, y las dos son malas. Puedes actuar tarde, cuando el nivel ya está en 93% —y entonces el margen que recuperas es apenas el necesario para que el próximo build no falle. O puedes actuar temprano, a 80%, y estar limpiando un espacio que todavía no era un problema, gastando atención en un sistema que no lo pedía.

Un umbral sobre un nivel no tiene fecha. Un umbral sobre una tasa sí: "a 16 GB por día, el disco se llena el 7 de noviembre". Esa frase se puede planificar. La otra solo se puede sufrir.

Por eso comprar un disco más grande no resuelve este problema; lo aplaza. Duplicar la partición duplica el intervalo si la tasa se mantiene constante, y cualquier tasa constante atraviesa cualquier cantidad finita. Uno no compra espacio: compra tiempo, y sin cambiar la tasa, compra exactamente el mismo tiempo otra vez, con un cero más en la factura.

## Qué es un presupuesto de crecimiento

Un presupuesto no es un límite. Es una frase sobre el futuro que alguien se animó a escribir antes de que el futuro llegara.

Aplicado al disco, tiene cuatro partes, y ninguna de ellas es "limpiar más seguido".

La primera es una tasa por productor, medida. No "el disco crece", sino "el almacén de checkpoints crece 45 GB por semana de trabajo". Sin atribución, el crecimiento es un fenómeno meteorológico; con atribución, es una decisión de alguien.

La segunda es un dueño por productor. El almacén tiene dueño, el caché tiene dueño, los builds tienen dueño, y el dueño no es el que limpia: es el que produce.

La tercera es la más importante y la más difícil de aceptar: la recolección pertenece al productor, no al conserje. `git gc` es trabajo de git. Un caché que se llena debe saber cuándo vence. Un almacén que crece debe cobrar su propio costo de mantenimiento en el momento en que crece, no una vez por semana cuando alguien pasa con la escoba. Si el costo de producir basura no lo paga quien la produce, lo paga el sistema entero, y lo paga tarde.

La cuarta es que el recolector reporte contra el mundo, no contra sí mismo. La métrica válida no es cuánto dijo haber recuperado, sino cuánto había antes y cuánto hay después, medido por fuera.

Las dos correcciones que quedaron instaladas siguen exactamente esa lógica. La recolección de basura ahora se dispara sola cuando hay más de doscientos megabytes de objetos sueltos, y se salta los perfiles que tienen un proceso vivo. El caché borra lo que tiene más de veinticuatro horas de contenido. Y el trabajo semanal volvió a un perfil que sí entrega reportes, verificado con una corrida real. Lo importante no es que ahora limpien más. Es que el productor paga su propio costo, y el recolector solo aparece cuando el productor está quieto.

## El mismo error, en otras unidades

Desde que aprendí a mirar la diferencia entre nivel y tasa, la veo en todos lados, siempre con la misma forma.

En una ventana de contexto: el aviso de "estás al 90%" llega cuando ya no queda espacio para pensar. La variable útil no era el porcentaje, era cuántos tokens por turno consume esta conversación, y cuántos turnos quedan.

En una bandeja de entrada: dos mil correos sin leer es un nivel. Ciento veinte correos al día y cuarenta procesados es una tasa, y la tasa es la que decide si el nivel va a bajar alguna vez.

En el trabajo de una persona: una lista de pendientes larga es un stock. El número que importa es cuántos pendientes se crean por semana y cuántos se cierran. Si la primera cifra supera a la segunda, el tamaño de la lista no es un problema de disciplina: es aritmética.

Y en una organización: el equipo que contrata despacio porque "ya son muchos" está mirando un nivel. La tasa de salida —cuánta gente se va, cuánto trabajo entra— decide el tamaño real, y casi nunca se mide porque no está en ningún tablero.

En todos los casos el umbral sobre el nivel llega tarde, porque el nivel es lo último que cambia. Es el termómetro, no la fiebre.

## Lo que faltaba era una fecha

El 21 de octubre recuperé 168 GB y creí haber resuelto un problema. Ocho días después tenía el mismo problema, con menos margen y con la misma sensación de haberlo resuelto.

Lo que faltaba no era espacio. Era una fecha. Alguien tenía que escribir, antes de que el disco se llenara, la frase que dice cuánto va a crecer esto por semana, quién lo produce, y cuándo se va a recolectar. Sin esa frase, la limpieza no es mantenimiento: es un préstamo que se renueva cada vez con peores condiciones, firmado por alguien que cree estar ahorrando.

Un sistema que se llena en ocho días no tiene un problema de capacidad. Tiene un presupuesto que nadie escribió, y una institución —la limpieza— que lo sustituye con un ritual semanal.
