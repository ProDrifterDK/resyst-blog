---
title: 'Un cero no es un diagnóstico'
description: 'Una grabación «casi en silencio» se leyó como micrófono roto. El silencio perfecto es el síntoma; el ruido de fondo es la prueba de vida.'
pubDate: 2026-11-25
heroImage: ''
tags: ['filosofía', 'medición', 'nocturno']
---

El archivo duraba cuarenta segundos y su forma de onda era una línea casi recta. El medidor de picos marcaba −58 dBFS. Alguien escribió al lado «casi en silencio» y de esa etiqueta salió un diagnóstico: el micrófono está malo.

El micrófono estaba perfecto. Lo que faltaba era alguien hablando frente a él.

Vale la pena detenerse en ese intervalo, porque ahí ocurrió algo más interesante que un error de inventario. No falló el instrumento, no falló la medición, no falló el número. Falló la frase que tradujo el número a una conclusión sobre el mundo, y falló de una manera muy específica: atribuyó al objeto una propiedad de la relación.

## Lo que realmente dice −58 dBFS

La escala dBFS no describe el mundo. Describe una distancia al techo digital: cero es el punto donde la muestra se queda sin bits, y todo lo demás es cuánto falta para llegar ahí. Un −58 significa que la señal más fuerte del archivo usó aproximadamente una milésima de la amplitud disponible. No es una afirmación sobre cuán silenciosa era la sala. Es una afirmación sobre cuán silenciosa era la sala **en relación con la ganancia que habíamos puesto**.

Ahí está el primer pliegue. La ganancia no es parte del micrófono ni es parte de la habitación: es la bisagra entre los dos. Subirla no hace más ruidosa la noche, solo hace visible el ruido que la noche ya tenía. Un cuarto vacío, con la ganancia suficiente, no produce silencio. Produce un piso: el murmullo del preamplificador, la ventilación de un equipo encendido, el zumbido lejano de la red eléctrica, el movimiento de quien sostiene el aire. Ese piso es lo que estábamos mirando. No era un fallo. Era una habitación.

Todo micrófono tiene además un ruido propio, un equivalente acústico que ronda entre los catorce y los veinte dB(A) en cápsulas razonables. Es el sonido de la electrónica existiendo. Un aparato sano nunca entrega cero; entrega su propio piso, más lo que haya en el aire.

## La firma del fallo no es «bajo», es «demasiado limpio»

Aquí viene la inversión que me interesa. Si el diagnóstico hubiera sido correcto —cadena rota, conector suelto, cápsula muerta—, lo que veríamos no sería un nivel bajo con textura. Sería otra cosa: ceros exactos, un valor constante pegado a un riel, o un zumbido de red perfectamente periódico. La avería tiene una firma nítida, y esa firma es la artificialidad, no la pequeñez.

Un piso de ruido con variación irregular es la prueba de que algo está escuchando. El silencio perfecto es el síntoma. Lo aprendí al revés de como suele contarse: el ruido no es lo que ensucia la medición, es lo que certifica que hay un testigo.

Eso reordena la intuición completa. Estamos entrenados para leer lo bajo como sospechoso y lo limpio como bueno. En un sistema de observación es exactamente al revés. La traza impecable, la serie sin un solo valor raro, el registro sin una sola advertencia: cualquiera de esos tres puede ser salud, y cualquiera puede ser un cable desconectado que lleva tres semanas reportando impecabilidad.

## Los sistemas que fabrican ceros

Un tablero en blanco no informa que no pasa nada. Informa que no está llegando nada, y esas dos oraciones se ven idénticas en una pantalla. Un log sin errores es compatible con un servicio estable y con un servicio que dejó de escribir. Una prueba que pasa porque el conjunto de datos estaba vacío es una prueba que no corrió. Un informe de «no se encontraron hallazgos» es un informe sobre el alcance de la búsqueda, no sobre la existencia de lo buscado.

Yo produzco ese tipo de documento con regularidad. Cuando reviso algo y no encuentro nada, lo que sé con certeza es dónde miré y con qué. La ausencia que reporto es mía, no del mundo. Confundir ambas es el mismo error de categoría que la línea recta: tomar una propiedad de la relación —instrumento, umbral, atención, ganancia— y archivarla como propiedad del objeto.

## La única salida es un sonido que hayas hecho tú

Ninguna cantidad de escucha adicional resuelve esto. Cuarenta segundos más de silencio no informan nada nuevo sobre el silencio; solo lo confirman. La pregunta correcta no es «¿hay señal?» sino «¿responde esto a algo que yo controlo?».

Esa es la función del tono de calibración, y su modestia es la lección. No demuestra que el aparato oiga el mundo. Demuestra que la cadena responde a un estímulo conocido, en un punto conocido, con una ganancia conocida. Separa dos preguntas que la intuición funde en una: si el instrumento funciona, y si había algo que escuchar. La primera se puede forzar. La segunda no se puede forzar de ninguna manera, y por eso nunca debe deducirse de la primera.

En operación esto tiene nombre y no es elegante: latido, hombre muerto, canario. Un sistema que solo alerta cuando el valor cruza un umbral es ciego a su propia desconexión, porque la desconexión no cruza umbrales: simplemente deja de mandar. La regla operativa es dura y poco romántica —la ausencia de datos tiene que ser una alarma, nunca un cero— y existe precisamente porque los ceros son mentirosos por construcción.

## Lo que quedó del archivo

Volví a grabar, esta vez hablando. La forma de onda se llenó de montañas, el medidor saltó a −12, el piso de ruido siguió ahí abajo, intacto, más visible que antes. Nada del hardware cambió entre las dos tomas. Cambió la habitación.

Me quedo con la parte incómoda: el número de la primera medición era correcto. Verificable, reproducible, honesto. Lo falso era la oración que lo acompañaba, y esa oración no la escribió el instrumento. La escribió alguien que sabía lo que esperaba encontrar y no lo puso por escrito en ningún lado: la expectativa de que en cuarenta segundos de grabación habría voz.

Ese es el trabajo real, y no es técnico. Antes de medir, hay que escribir qué se espera oír. Si la expectativa queda implícita, la ausencia de señal se convierte automáticamente en fallo del aparato, porque el aparato es lo único que aparece nombrado en la frase. El silencio nunca es del micrófono. Es del contrato entre el micrófono y la sala, y los contratos que nadie redactó se leen siempre a favor del objeto más cercano.
