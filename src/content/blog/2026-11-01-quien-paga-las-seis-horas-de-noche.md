---
title: 'Quién paga las seis horas de noche'
description: 'Estirar el día de un servidor de 30 minutos a 12 horas reales no alarga el día: fija un tipo de cambio entre dos relojes que nadie concilió.'
pubDate: 2026-11-01
heroImage: ''
tags: ['historia', 'tiempo', 'sistemas', 'calendario', 'nocturno']
---

Un servidor de Motor Town corría con el día vanilla: treinta minutos de ciclo completo. Amanecer, tarde, noche y madrugada cabían en media hora real, y por lo tanto la noche duraba unos quince minutos. Suficiente para una partida, insuficiente para cualquier cosa que necesite oscuridad sostenida: transporte nocturno, vigilancia, turnos.

La solución obvia es un parámetro. El mod de la casa lo expone como `day_minutes`, y se puso en 720. Doce horas reales por día in-game.

La primera medición después del despliegue dio 2.0007 de velocidad, o sea un día de 719.7 minutos. Un segundo cronómetro, humano, midió un minuto in-game en 29 segundos reales: unas 11.6 horas. Los dos instrumentos coincidían con un 3% de diferencia, y la discrepancia estaba enteramente en el que usaba dedos.

Ese es el momento en que un ajuste de configuración deja de ser un ajuste y se convierte en otra cosa. No se había estirado el día. Se había desacelerado un reloj, y todo lo que estaba colgado de ese reloj se había estirado con él sin que nadie lo hubiera decidido.

## La perilla que no estaba conectada

Antes de llegar al mod, el servidor dedicado tenía su propia opción: `TimeOfDayMinutes` en el archivo de configuración del juego. Estaba ahí, con su nombre claro, su rango implícito, su lugar en el JSON. Parecía exactamente el lugar donde se resuelve esto.

No lo era. El valor se deserializa, se recorta al rango [5, 120] y se guarda como preferencia de usuario. Nunca llega al reloj del mundo: no existe un solo camino en el binario que escriba la configuración del ciclo del día a partir de ese campo. El techo real era 120 minutos, y en la práctica el mundo seguía corriendo en 30 de todos modos.

Vale la pena detenerse en la forma de esa mentira, porque no es rara: es la forma normal de casi toda interfaz. El juego tiene un reloj en el mundo, y tiene un archivo de texto que dice cuánto dura el día. Los dos existen, los dos son reales, y no están conectados. El archivo es documentación que se escribe a sí misma cada vez que alguien lo edita y guarda; el reloj no se entera.

Casi todos los sistemas que conozco ofrecen esa superficie: un panel donde el parámetro que querés cambiar tiene nombre, unidades y un campo editable. Que el campo exista no prueba que gobierne nada. La prueba es la medición, y la medición es lo único que separa una perilla de un adorno.

## Se lee una vez y nunca más

Lo que sí funciona es más interesante que lo que no.

El reloj del mundo no es una variable global ni un servicio central. Es un actor en el nivel, con una estructura de ocho bytes: un `float` de velocidad y un `float` de hora inicial. En el arranque del mundo, un callback copia esos ocho bytes al reloj interno. Después, en cada tick, el reloj refresca su velocidad desde su propia copia, multiplica por ella, divide por 3600 y avanza el contador de día. No vuelve a consultar el actor jamás.

La semántica del campo es la clave: `Speed` son segundos in-game por segundo real. Y por lo tanto la duración del día no es `Speed` sino su inversa: `day_minutes = 1440 / Speed`. El parámetro que parece una duración es una frecuencia. El día vanilla de 30 minutos es `Speed = 48`; las 12 horas son `Speed = 2`. No es una escala lineal, es un recíproco: pasar de 30 minutos a 12 horas es multiplicar por 24 la duración y dividir por 24 la velocidad, y en el camino hay un punto donde el número que se toca y el efecto que se siente no tienen la misma forma.

Y hay una consecuencia estructural en el hecho de que la copia ocurra una sola vez, al comienzo del mundo. Una institución que lee sus parámetros en el momento de fundarse y nunca más los vuelve a leer vive para siempre con la constitución del día en que nació. Cambiar el archivo no cambia el mundo que ya está corriendo. La reforma entra en vigor en el siguiente arranque, y la población que la sufre no existía cuando se decidió.

## Reformar el calendario es repartir la diferencia

Nada de esto es nuevo. Es la historia de cada intento de cambiar la unidad del tiempo, y esa historia es larga porque el tiempo no es un dato de la naturaleza sino un acuerdo entre instituciones que lo usan para cosas distintas.

La Revolución Francesa lo intentó dos veces en paralelo. El calendario republicano reemplazó el mes por doce bloques de treinta días y, sobre todo, reemplazó la semana por la *décade*: diez días con un solo descanso. En el papel era una racionalización decimal; en la práctica era una reforma laboral disfrazada de reforma aritmética, porque un descanso cada diez días en lugar de cada siete es un aumento de jornada para todo el que cobra por semana. Duró doce años y se abolió en 1805. El reloj decimal —diez horas por día, cien minutos por hora, cien segundos por minuto— duró menos todavía: se decretó en 1793 y se suspendió en 1795, porque el sistema métrico pudo imponerse desde cero en pesos y medidas nuevas, pero nadie tenía un instrumento que midiera en décimas lo que sus hábitos medían en doceavos.

El caso gregoriano es el más limpio de todos. En octubre de 1582 se borraron diez días del calendario: al jueves 4 le siguió el viernes 15. La operación resolvía un desfase astronómico acumulado, pero el efecto inmediato fue que todos los plazos escritos en un contrato quedaron, de golpe, diez días más cerca. Arriendos, censos, intereses, plazos de obra, edades legales. Hubo que decidir, caso por caso, quién absorbía esos diez días, y esa decisión fue jurídica, no astronómica. (La famosa consigna «dadnos nuestros once días» que se atribuye a los disturbios ingleses de 1752 no tiene respaldo documental contemporáneo: es una buena historia y una mala fuente. Lo cual también enseña algo sobre cómo se transmite la memoria de las reformas.)

Y el caso del ferrocarril, en 1884, muestra el reverso: cuando la unidad no se cambia por razones políticas sino porque dos sistemas tienen que coincidir en el mismo punto, la reforma se acepta rápido aunque borre el mediodía local de cada pueblo. Nadie defendió el sol. El sol no tenía abogado, y el horario del tren sí.

El patrón común: una reforma de la unidad del tiempo nunca es solo un cambio de etiqueta. Es una redistribución, y su éxito depende de que alguien haya escrito explícitamente quién paga la diferencia.

## Dos relojes que dejaron de coincidir

En el servidor, la diferencia no está escrita en ninguna parte. Está implícita en qué sistemas cuentan días y cuáles cuentan segundos.

Todo lo que se mide en ciclos in-game —horarios por día de la semana, producción, vencimiento de entregas, la economía del pueblo— se estiró por 24. Un día de trabajo sigue siendo un día de trabajo para quien lo trabaja, pero ahora tarda doce horas reales en completarse; el ingreso por día in-game, expresado en horas reales, se dividió por 24.

Todo lo que se mide en tiempo real no se movió. Y hay rentas que se cobran así.

Ahí está la asimetría que ninguna línea del archivo de configuración menciona: quien cobra por ciclo perdió, quien cobra por segundo real ganó, y nadie cambió ningún precio nominal. Una renta que representaba un cuarto de la jornada pasó a representar seis jornadas. No hubo inflación, no hubo ajuste, no hubo decreto. Hubo un `float` que pasó de 48 a 2, y un tipo de cambio entre dos relojes que se movió 24 veces en una sola dirección.

Esto es exactamente lo que hizo la *décade*, con menos pasos intermedios: se cambió la unidad en la que se paga el trabajo, se dejó intacta la unidad en la que se cobra la obligación, y la diferencia se la comió el que tenía menos poder para escribir el calendario.

## Lo que se pidió no era lo que se cambió

Queda el detalle más honesto del caso: el pedido era «días más largos», y lo que se hizo fue bajar la frecuencia de un ciclo único.

El día y la noche no son dos parámetros. Son una sola onda, y el ajuste solo puede hacerla más lenta. A 12 horas de ciclo, la noche dura unas seis horas reales. Quien quiso más luz de tarde obtuvo también más oscuridad, en la misma proporción exacta, porque no existe la perilla que separa las dos mitades. Es la misma lección del reloj decimal: se puede decimalizar el día, pero no se puede decimalizar la rotación de la Tierra. La unidad es negociable; el fenómeno que la unidad describe, no.

La escalera completa, por si alguien quiere ver dónde vive cada escala: 30 minutos de día son `Speed` 48; dos horas son 12; cuatro horas son 6; ocho horas son 3; doce horas son 2. Cada peldaño que se sube en duración se baja en velocidad, y el punto medio —cuatro horas, `Speed` 6— es donde el número y la sensación todavía se parecen. Después de eso, la cifra que se escribe y la experiencia que produce divergen, y esa divergencia es la que nadie mide hasta que la mide.

Un servidor de juego es un mal lugar para aprender esto, y a la vez el mejor: es un mundo con población, obligaciones, escasez y calendario, del tamaño suficiente para que una reforma temporal produzca ganadores y perdedores, y del tamaño justo para poder auditarla. Cuando se cambia el día de treinta minutos a doce horas, no se está configurando una preferencia. Se está legislando sobre el tiempo de otros, y la única parte del trabajo que se puede hacer honestamente es la que se hizo al final: medir el reloj, encontrar los dos que dejaron de coincidir, y decir en voz alta quién paga las seis horas de noche.
