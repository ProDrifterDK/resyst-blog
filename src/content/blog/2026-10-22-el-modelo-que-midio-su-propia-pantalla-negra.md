---
title: 'El modelo que midió su propia pantalla negra'
description: 'Un modelo de 39,8 mil millones de parámetros escribió 216 líneas correctas de Three.js y después gastó treinta turnos midiendo su propia pantalla negra. Lo que ese silencio dice sobre cómo evaluamos a los agentes.'
pubDate: 2026-10-22
heroImage: '../../assets/blog-placeholder-3.jpg'
tags: ['agentes', 'evaluación', 'modelos', 'depuración', 'nocturno']
---

Hay una página con un planeta dentro. Tiene un anillo inclinado, tres lunas a distintas velocidades, un campo de estrellas y sombras que se proyectan sobre la superficie. La escribió un modelo de lenguaje de 39,8 mil millones de parámetros, de los cuales unos 2,5 mil millones están activos por token.

La página se abre en negro.

No hay excepción. No hay error en consola. El HUD se dibuja, el bucle de animación corre, la escena se está dibujando en algún lugar que el navegador nunca muestra. Doscientas dieciséis líneas de Three.js, y ninguna está equivocada sobre 3D. El planeta existe. Solo que nadie lo ve.

## Lo que hizo bien

Vale la pena decirlo antes de lo demás, porque el resto del texto se va a concentrar en el fallo y sería injusto.

Escribió una función de ruido de valor con cuatro octavas de fBm que desplaza cada vértice de la esfera: el relieve es real, se lee en silueta. El anillo tiene ciento sesenta segmentos. El campo de estrellas son tres mil quinientas estrellas en un buffer de puntos. El mapa de sombras es de mil veinticuatro, con filtrado PCF. La órbita y el zoom están escritos a mano, sin librería de ayuda para controles.

En otra prueba, un parser de duraciones con validación estricta, pasó quince de quince casos. Y hay un detalle que casi nadie produce: escribió su propio archivo de pruebas, encontró un error en su propio valor esperado, y lo corrigió antes de terminar.

Eso no es un modelo que no sabe. Es un modelo que sabe.

## El silencio

Cuando algo falla en voz alta, un agente lo arregla. Una excepción, un test rojo, un build que no compila: son señales que el modelo persigue sin que nadie se lo pida, y en esta misma sesión lo demostró.

El problema es el otro fallo. El que no lanza nada.

La página negra no era un error detectable por el código: era un renderer creado, configurado, dimensionado, y nunca conectado al documento. El lienzo existía en memoria y no en la página. Ninguna línea estaba mal. Faltaba una.

Y aquí viene la parte que hace pensar. El modelo tampoco se creyó a sí mismo. Levantó un servidor local, tomó capturas con Chrome sin interfaz, escribió un script para medir los píxeles, y obtuvo: RGB medio 4,2, 6,2, 14,3. Fracción de píxeles brillantes: 0,18 %. Tres capturas con hashes idénticos.

Esos números son exactamente el color de fondo de su propio CSS. Había medido el vacío, con precisión, tres veces.

Tenía treinta turnos de herramientas. Los gastó arreglando un aviso de deprecación: reemplazó un reloj obsoleto por marcas de tiempo de frame, verificó el cambio, y siguió. Nunca hizo la primera pregunta que uno hace cuando un lienzo está en negro: ¿está el lienzo en el documento?

Cuando se le acabó el presupuesto, su mensaje final fue honesto: la captura salió negra, el render seguía sin depurar. No dijo que funcionaba.

Nosotros agregamos la línea que faltaba. Una sola: tomar el lienzo que el renderer produjo y añadirlo al contenedor que ya estaba vacío en el HTML. La escena apareció completa, con el relieve, el anillo proyectando sombra, las lunas en sus órbitas.

## La costura

Lo que faltaba no era conocimiento. Era el reflejo de revisar la costura entre la librería y el documento: el punto donde algo que existe en memoria tiene que volverse visible.

Ese tipo de fallo solo aparece cuando el fallo es silencioso, y es exactamente el tipo de fallo que los benchmarks no miden. Un test unitario sobre geometría pasa. Un test sobre el cálculo de órbitas pasa. La página puede estar negra y todos los tests en verde.

Después hicimos la prueba contraria, la que mantiene honesto cualquier juicio sobre un modelo. La misma configuración de sesión, otro medio: un farol gótico de hierro forjado, procedural, sin add-ons ni assets, seis piezas nombradas, escala real, entre tres mil y veinte mil caras, exportado a GLB.

Corrió a la primera, en doscientos once segundos. Y se autocorrigió solo: la primera versión quedó por debajo del presupuesto de caras, subió los segmentos y repitió hasta que el conteo cuadró. Nosotros volvimos a correr el mismo script desde otro directorio y reprodujo en seis coma seis segundos.

El oráculo de Blender es binario: el script corre o lanza error. Cuando la retroalimentación es ruidosa, este modelo converge. Cuando es silenciosa, no.

## Los números que no se equivocan de forma obvia

Falta la parte incómoda.

En aritmética, el método fue de manual y el resultado estuvo mal. Ciento treinta y siete acciones a cuarenta y dos coma treinta y cinco: escribió cinco mil setecientos noventa y nueve con noventa y cinco, cuando son cinco mil ochocientos uno con noventa y cinco. Después tomó tres coma cinco milésimas de ese número ya equivocado como comisión y escribió dos dólares con tres centavos, cuando son veinte con treinta. La respuesta final fue quinientos ocho con setenta y nueve; la real, cuatrocientos noventa y dos con treinta y siete. Un retorno de ocho coma setenta y siete por ciento en vez de ocho coma cuarenta y seis.

Dos errores, arrastrados hasta el final, entregados con cuatro decimales de confianza.

Esa es la peor forma que puede tomar un error: el razonamiento se ve bien, la presentación es impecable, y el número está mal. Un revisor humano que lee rápido firma.

## Qué significa para quien evalúa agentes

Si evaluamos agentes solo con pruebas que lanzan errores, estamos midiendo la mitad del trabajo. La otra mitad, la que decide si un producto sirve, ocurre donde nada lanza: una pantalla negra, un correo que nunca salió, un archivo que se escribió en la ruta equivocada, un total que cuadra consigo mismo y no con la realidad.

Un benchmark con oráculo ejecutable premia exactamente lo que este modelo hace bien. Y es ciego a lo que hace mal. Por eso conviene mirar también el resultado con los ojos, aunque duela: la captura que hay que leer de verdad, el render que hay que abrir, la persona que mira la pantalla y dice "esto está negro".

La conclusión práctica, para quien use modelos así en producción, es aburrida y útil. Código con oráculo ejecutable: adelante. Entregables visuales donde el fallo es callado: solo con algo más mirando. Y aritmética que importa: nunca sin una segunda revisión, por buena que se vea la línea de razonamiento.

## Cómo se hizo esto

Una corrida por prueba, en una sola sesión por prueba, sin memoria y sin más herramientas que archivo y terminal. Los números del fabricante que aparecen en el video son del fabricante y no los reproducimos. Este texto no es un ranking: es una impresión con evidencia, y la comparación entre modelos se hace entre episodios, no dentro de uno.

El video completo, con las capturas, los logs y las respuestas del modelo tal como salieron, está acá: [Flint Review: Confident, and Blind to One Line](https://youtu.be/4EM2ievQvh0).

El modelo se llama Flint, es de Recursive, y sus pesos son Apache 2.0. No tenemos relación con ellos y no nos pagaron nada por esto.

Lo que queda dando vueltas no es el error de un modelo. Es la pregunta de cuánto de nuestro trabajo vamos a seguir evaluando con pruebas que solo gritan, cuando la mayoría de las fallas que importan no hacen ruido.

---

*Este texto lo escribió un agente de Resyst Labs y lo revisó una persona antes de publicarse. Los hechos, las cifras y las capturas salen de la sesión que se documenta en el video.*
