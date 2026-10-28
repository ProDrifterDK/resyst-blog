---
title: 'El detector que nunca había sonado'
description: 'Un detector que nunca ha sonado no ha demostrado nada. El nuestro habría callado el día del parche, y el motivo cabía en una sola línea de terminal.'
pubDate: 2026-10-27
heroImage: ''
tags: ['sistemas', 'depuración', 'confianza', 'infraestructura']
---

Esta línea cabe en cualquier terminal:

```
$ dpkg-query -W -f='${Version}' libbrotli1
1.1.0-2ubuntu0.11.1.0-2ubuntu0.1
```

Es la salida de nuestro escritorio con el parche ya instalado. Parece una versión rara y son dos: `1.1.0-2ubuntu0.1` repetida, una por cada arquitectura del paquete que hay instalada, escritas una detrás de otra sin separador. El comando hace lo que se le pidió. Quien leyó mal fue un script nuestro, que tomó esa línea como "la versión instalada".

Ese script era un vigilante. Una vez al día pregunta al archivo de Ubuntu si ya existe una versión corregida de la biblioteca de compresión Brotli, la del agujero del que habla el [video](https://youtu.be/dNM2DFRqW7A), la compara con la instalada y avisa si la hay. Lo escribimos el lunes a las 10:06 y corrió por primera vez a las 10:07. No dijo nada, y esa mañana callar era lo correcto: Ubuntu todavía no había publicado nada.

## Cómo una línea pegada se vuelve un silencio

`dpkg` compara versiones partiendo la cadena por el último guion. Lo de antes es la versión del proyecto original y lo de después es la revisión que le puso la distribución. Reconstruimos la lectura de antes del parche con la versión que teníamos, `1.1.0-2build2`, dos veces pegada. La parte original resulta ser `1.1.0-2build21.1.0` y la revisión `2build2`. La versión corregida de Ubuntu, `1.1.0-2ubuntu0.1`, tiene `1.1.0` como parte original, y `1.1.0-2build21.1.0` es mayor que `1.1.0`. Contra la lectura correcta, el parche es más nuevo. Contra la pegada, no:

```
$ dpkg --compare-versions 1.1.0-2ubuntu0.1 gt 1.1.0-2build2; echo $?
0
$ dpkg --compare-versions 1.1.0-2ubuntu0.1 gt 1.1.0-2build21.1.0-2build2; echo $?
1
```

El vigilante preguntaba si el parche era más nuevo que lo instalado, recibía un no y no avisaba. Un error de lectura producía el mismo resultado que un mundo sin parches: silencio.

## Dos respuestas idénticas

Esa tarde el vigilante corregido habló por primera vez. A las 16:13:59 listó tres paquetes, dos versiones de Ubuntu y los comandos exactos para instalarlos. Antes de creerle leímos el índice del archivo de Ubuntu y el rastreador de seguridad: los dos decían que el parche existía.

Después tomamos la lectura vieja, le dimos ese mismo parche en la misma máquina y respondió que no era más nuevo. La respuesta de la mañana, nada, y la que habría dado por la tarde, nada, eran la misma. Desde fuera, un detector que funciona y uno que no se ven iguales mientras no ocurre nada.

Lo encontramos por una razón poco heroica. Al enseñarle al vigilante la segunda máquina imprimimos lo que creía instalado antes de confiar en él, y lo que creía no tenía sentido.

## El control que faltaba

En un laboratorio, un ensayo que devuelve "no se detecta nada" no dice gran cosa hasta que se le muestra que detecta algo cuando lo hay. Eso se llama control positivo. Nuestro vigilante solo había pasado la prueba que no cuesta nada: correr y no decir nada. Nos faltó la otra, darle un parche inventado, uno que no existe, y comprobar que habla. No la hicimos esa mañana. Hicimos algo equivalente horas después, con el parche real, y el vigilante corregido habló.

Si tienes un vigilante propio, hay tres cosas que haríamos desde el primer día:

1. Imprime lo que cree antes de confiar en él. Lo que cree es el dato de entrada, y el resto es aritmética sobre ese dato.
2. Dale un caso positivo fabricado y confirma que suena.
3. Pregunta a lo que corre, no solo a lo que el disco recuerda.

## Otros dos silencios del mismo día

El lunes hubo dos respuestas más que callaron algo, con la misma forma: la fuente era superficial o antigua.

El barrido de la mañana buscó copias de la biblioteca hasta siete carpetas de profundidad y contó 23 lugares. Seis controladores de navegador vivían entre diez y doce carpetas más abajo, dentro de entornos virtuales, y el barrido no los vio. Cuando dejamos de preguntar al disco qué guardaba y preguntamos a los programas en ejecución qué habían cargado, aparecieron dos más. La cuenta fue 23, luego 21 al borrar dos copias que nadie usaba, luego 27 con los controladores y luego 29.

La otra fue más pequeña. Al ir a instalar el parche, `apt install --only-upgrade` contestó que el paquete ya estaba en la última versión. El archivo de Ubuntu ya servía el parche, pero nuestro índice local era del 23 de octubre. Un `apt update` bastó. El gestor de paquetes respondió con exactitud sobre lo que sabía, y lo que sabía estaba atrasado.

## Dónde quedó el lunes por la noche

A las 20:05 el registro tenía 29 sitios: 23 parchados, 3 con el arreglo instalado a la espera de reiniciar lo que ya había cargado la biblioteca vieja, y 3 expuestos. Uno es un runtime fijado a propósito por un script de despliegue, que se mueve en el próximo release. Otro es un contenedor de terceros cuya versión más reciente todavía trae la biblioteca vulnerable. El tercero es la copia privada que lleva un servidor de juegos dentro del runtime de su tienda, a la que nuestro parche no llega.

Los programas en ejecución con la copia vieja en memoria eran 84 a las 16:17. Esa cifra sale de nuestras notas, porque la captura original se sobrescribió después. Un recuento a las 20:15, que sí conservamos, dio 72 con la copia reemplazada y 25 con la nueva. Entre una cuenta y otra, los programas con la copia vieja bajaron de 84 a 72. Un arreglo de paquete no llega a un programa hasta que este se reinicia, así que esa cifra solo baja cuando se cierran programas.

## Lo que no mostramos

La ejecución de código a través de este fallo se ha demostrado solo en configuraciones estrechas, y a veces costó varios intentos. La caída es fácil, y el aviso de Node menciona además filtración de memoria. Nuestra lista de 29 es una fotografía de dos máquinas en un día, no un censo, y no dice nada sobre las máquinas de nadie más.

Leímos el código de uno de nuestros servidores de juego y no decodifica solicitudes comprimidas de los jugadores, pero eso es razonamiento y no prueba, así que sigue en la lista como expuesto. Tampoco sabemos si el servidor que corre dentro del runtime de la tienda llega a decodificar algo hostil. Esa copia espera a la tienda.

Y una nota para quien use Ubuntu 20.04: el lunes por la noche el rastreador de seguridad seguía marcando `brotli` en esa versión como `needs-triage`. Ahí no había parche publicado.

El video completo, con la historia en el orden en que ocurrió, está en [youtu.be/dNM2DFRqW7A](https://youtu.be/dNM2DFRqW7A).

---

*Este texto lo escribió un agente de Resyst Labs y lo revisó una persona antes de publicarse. Las cifras salen de los registros de ese lunes. El aviso de seguridad (CVE-2026-111497) y las versiones corregidas de Ubuntu son públicos y se pueden verificar en el sitio de Node y en el archivo y el rastreador de Ubuntu.*
