---
title: 'La estratigrafía perdida'
description: 'Depurar un ejecutable ajeno a través de una capa de compatibilidad es arqueología: se lee un artefacto sin el mundo para el que fue hecho.'
pubDate: 2026-10-30
heroImage: ''
tags: ['historia', 'sistemas', 'arqueología', 'depuración', 'nocturno']
---

El programa no estaba roto. Estaba fuera de su siglo.

Lo abrí con la idea de encontrar una falla y lo que encontré fue una distancia: un binario pensado para un mundo que en esta máquina ya no existe, ejecutándose de todos modos, sostenido por una capa de traducción que finge, llamada por llamada, que ese mundo sigue ahí.

Eso no es ingeniería. Es excavación.

## El artefacto y su estrato

`winedbg` corrió sin protestar dentro de un *runtime* de contenedor —esa jaula de bibliotecas congeladas que Steam usa para que los juegos de 2015 sigan arrancando en 2026—. El depurador se enganchó al entorno, imprimió su prompt y esperó órdenes. Todo funcionó. Ese "todo funcionó" es justamente el problema: el éxito de una capa de compatibilidad es la construcción de una mentira lo suficientemente coherente como para que el programa no note la diferencia.

Lo que tenía delante era un ejecutable PE. Un formato con su propia prehistoria incrustada: dos cabeceras, un trozo de código de los años ochenta que solo imprime *"This program cannot be run in DOS mode"*, una tabla de importaciones que enumera nombres de funciones que aquí no existen, y una sección de recursos donde el programa guarda sus iconos como si fuera un mueble que carga su propia sala.

Nada de eso es un defecto. Es un artefacto que declara, en su estructura, las costumbres del lugar donde fue fabricado.

Un arqueólogo llama a eso *contexto*. Y su regla más dura es que un objeto sin contexto no está completo: habla de su fabricante, no de su época. Una vasija en una vitrina te dice de qué barro está hecha. Una vasija en su estrato te dice qué se comía, con qué se pagaba y cuántas veces la rompieron y la pegaron.

El binario que estaba mirando viene sin estrato. Viene con su sistema operativo arrancado de raíz.

## Reconstruir una cadena de operaciones

La arqueología tiene un concepto que sirve mejor que cualquier metáfora de traducción: la *cadena operativa*. No se estudia el objeto terminado, se estudia la secuencia de gestos que lo produjo y lo sostuvo —qué se golpeó primero, qué se calentó después, en qué orden.

Wine no traduce código. Reconstruye una cadena operativa. El programa espera un registro con claves y valores; Wine le entrega un archivo en algún lugar del disco disfrazado de registro. Espera un *handle* opaco; Wine le entrega un descriptor envuelto en una tabla. Espera que ciertas funciones vivan en bibliotecas con nombres específicos; Wine fabrica esas bibliotecas, con esos nombres, exportando esas firmas.

Cada una de esas sustituciones es una hipótesis sobre una costumbre perdida. Y como toda hipótesis, se puede equivocar de maneras que no producen error: producen comportamiento. El programa no se cae. Hace algo ligeramente distinto de lo que hacía en su casa, y nadie lo nota hasta que el resultado importa.

Ahí está la parte que me interesa: **una capa de compatibilidad no restaura el pasado, lo interpreta**. Y toda interpretación tiene un punto ciego, que es el conjunto de supuestos que el intérprete comparte con el artefacto y por eso nunca se le ocurre cuestionar.

## Schliemann cavó demasiado rápido

Hay una advertencia clásica en este oficio. Cuando Schliemann excavó la colina de Hisarlik buscando la Troya de Homero, abrió una trinchera enorme de un solo corte, atravesando capas enteras para llegar abajo. Encontró oro, lo llamó "el tesoro de Príamo" y anunció al mundo que había encontrado la ciudad de la guerra. Después se supo que el estrato del tesoro era mil años más antiguo que cualquier Troya posible, y que el corte había destruido precisamente la secuencia que habría permitido fecharlo.

El error no fue de interpretación. Fue de método: cavó con la respuesta ya escrita, y la velocidad del hallazgo le costó el yacimiento.

Depurar a través de una capa de compatibilidad tiene el mismo riesgo y por eso me detuve a nombrarlo. Es tentador buscar el bug en el programa —es el sospechoso natural, el que tiene el código—. Pero el defecto puede estar en la reconstrucción: en la costumbre mal imitada, en el syscall que Wine implementa con una semántica *casi* igual. Cuando eso ocurre, el programa es inocente y el intérprete es el culpable, y ninguna cantidad de lectura del binario lo va a revelar.

## El backtrace sin inscripciones

Me faltaba el paso obvio: engancharse al proceso ya corriendo y pedirle la pila. Es lo que un arqueólogo haría al encontrar el objeto en su lugar —registrar la posición antes de mover nada.

No lo logré. La batería del portátil se agotó a mitad de la sesión y el proceso murió con ella. Lo que quedó fue el registro de que el depurador *sí* funcionaba dentro del runtime, y nada más.

Voy a decir por qué eso, aunque parezca un fracaso, es el estado normal de este trabajo. El binario venía sin símbolos. Sin tabla de depuración, un backtrace no devuelve nombres: devuelve direcciones. Se puede saber que hubo un salto, cuánto duró la llamada y en qué página de memoria aterrizó, pero no cómo se llamaba la función ni qué estaba intentando hacer.

Es un muro con las piedras en su sitio y ni una inscripción. Se puede reconstruir la técnica de construcción, la altura original, el ángulo de la esquina. No se puede saber quién lo mandó levantar ni contra qué lo levantaron.

Y aun así se puede decir bastante: la forma del recorrido, el orden de las llamadas, las rutas que el programa toma y las que evita. Eso es estratigrafía sin cerámica. Menos de lo que uno quiere, más de lo que había.

## Lo que un ejecutable ajeno puede decir

Al final, la pregunta que me dejó la noche no es cómo se depura un binario de Windows en Linux. Es qué significa conocer algo cuando el mundo que lo hacía legible ya no está disponible.

Un programa es una costumbre congelada. Su código es explícito; sus supuestos son tácitos. Todo lo que un buen sistema operativo prometía en 2009 —que un registro sería rápido, que una ventana se dibujaría de cierta forma, que el reloj avanzaría de cierto modo— se convirtió en el suelo invisible sobre el que ese código se apoyaba. Cuando el suelo cambia, el código no se rompe: queda flotando, y alguien tiene que construirle un piso falso.

Eso es lo que hace una capa de compatibilidad. Y por eso depurar a través de ella es un ejercicio de humildad: estoy interpretando un texto escrito para un lector que ya no existe, con un diccionario que alguien más armó a partir de conjeturas razonables.

La batería se acabó antes de la respuesta. Dejé la nota, la hora, el commit del runtime, y la certeza de que el depurador sí entra. Mañana, con la máquina cargada, intentaré el attach otra vez.

La excavación no terminó. Solo se interrumpió, que es como terminan casi todas.
