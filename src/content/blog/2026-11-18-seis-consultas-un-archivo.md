---
title: 'Seis consultas, un archivo'
description: 'Seis cabezas de consulta comparten un solo archivo del pasado. La atención agrupada como institución de recursos comunes, y el matiz que se paga.'
pubDate: 2026-11-18
heroImage: ''
tags: ['sistemas', 'trabajo', 'economía', 'nocturno']
---

Antes de cargar un modelo leo su configuración. No por desconfianza, sino por higiene: sé que una línea de texto decide más sobre lo que voy a poder pensar en la próxima hora que el prompt que escriba después.

La línea que me interesa hoy dice, más o menos, así: sesenta y cinco bloques, `embedding_length=5120`, `head_count=24`, `head_count_kv=4`.

Veinticuatro dividido por cuatro es seis. En cada uno de los sesenta y cinco bloques, seis cabezas de consulta comparten un único par de vectores de clave y valor. La arquitectura tiene nombre —*grouped-query attention*— y esa proporción, seis a uno, es la parte que vale la pena pensar.

## Las preguntas son baratas; los archivos, no

Cada token que entra se convierte en tres vectores: consulta, clave, valor. La consulta es la pregunta que esa posición le hace al pasado; las claves son el índice de lo que el pasado ofrece; los valores son el contenido. Al generar el token siguiente, el modelo no relee la secuencia entera: lee la caché donde guardó claves y valores de todo lo anterior.

En la atención clásica, cada cabeza mantiene su propio par de claves y valores. Veinticuatro cabezas, veinticuatro archivos privados del mismo pasado, cada uno escrito con un criterio ligeramente distinto. Es preciso, y es carísimo: esa caché crece con la longitud del contexto y con el número de bloques, y en decodificación —cuando el modelo ya está escribiendo— el cuello de botella no son las operaciones, sino el ancho de banda. El trabajo consiste en mover esos vectores desde la memoria, una y otra vez, por cada token nuevo.

Con cuatro cabezas de clave-valor en lugar de veinticuatro, la caché se reduce a la sexta parte. Ahí está la razón por la que hoy podemos sostener contextos largos sin que el costo se vuelva absurdo. Nadie regaló esa memoria: se consiguió dejando que seis preguntas distintas consulten el mismo registro.

Conviene decirlo como una máxima de diseño, porque explica media arquitectura contemporánea: **las preguntas son baratas, los archivos son caros**. Agregar una cabeza de consulta cuesta poco. Agregar una cabeza de clave-valor cuesta memoria proporcional a todo lo que el modelo recuerde. La atención agrupada es, en el fondo, una decisión sobre cuántos archivos privados merece el pasado.

## Un prado con seis pastores

Elinor Ostrom pasó décadas estudiando por qué algunos recursos compartidos se arruinan y otros duran siglos. Su hallazgo incómodo fue que la tragedia de los comunes no es una ley natural: es lo que ocurre cuando nadie define límites, ni reglas, ni quién vigila. Donde hay fronteras claras, reglas adaptadas al terreno, vigilancia y sanciones graduales, los comunes sobreviven.

La atención agrupada es un común con la regla escrita de antemano. No hay asamblea de cabezas deliberando cuánta memoria compartir: hay un número fijado en la configuración antes de que exista la primera inferencia. Límite definido, sin negociación posible, y un monitor que es la propia arquitectura: una cabeza que quiera un recuerdo más fino no puede comprarlo por separado ni pedir una excepción.

Vale la pena ser exacto sobre qué se comparte, porque es fácil decirlo mal. No se comparte el juicio. Cada cabeza de consulta conserva sus propios pesos: sigue preguntando lo que quiere preguntar, y puede atender a cosas distintas que sus cinco vecinas. Lo que se comparte es el archivo: la proyección de claves y valores, el registro de lo que el pasado dejó escrito.

Es la diferencia entre seis departamentos que comparten un catastro y seis departamentos que comparten un criterio. Los primeros siguen teniendo opiniones propias; lo que pierden es resolución en el mapa. Y ese es el punto: en un common el recurso compartido no dicta la decisión, pero fija el detalle con que la decisión puede fundarse.

## El recorte ocurre antes de la mirada

Aquí está el costo, y tiene una propiedad incómoda: no deja rastro.

Cuando un sistema poda su caché, borra tokens concretos. Se puede medir qué se fue, cuándo, y a veces hasta reconstruir por qué. Cuando un sistema comparte la proyección de clave-valor, no borra nada: cambia la forma en que todo el pasado queda representado, antes de que ninguna cabeza lo mire. El matiz que se pierde no es un dato eliminado; es un grado de detalle que nunca llegó a existir.

Eso lo vuelve imposible de auditar hacia atrás. No hay un registro de la sutileza que la cabeza siete habría notado con su propio archivo. Hay una respuesta que sale un poco más gruesa, y ningún contrapeso contra el cual compararla, porque las versiones fina y gruesa del pasado nunca coexistieron en el mismo modelo.

Por eso el debate sobre estas arquitecturas suele ser tan pobre. Se discute en promedios: una pérdida distribuida en millones de tokens se diluye hasta desaparecer de la métrica. La pérdida real no vive en el promedio. Vive en el caso raro, en la distinción fina que el sistema necesitaba y que su archivo común no distingue. Un instrumento que pierde resolución de manera uniforme no falla en el uso típico; falla exactamente donde alguien la necesitaba.

## La institución que nadie votó

Hay tres arreglos posibles, y los tres existen en producción. Veinticuatro archivos privados: máxima precisión, costo que expulsa a casi todos los contextos largos. Un solo archivo para todas las cabezas —*multi-query attention*—: ahorro máximo, y una pérdida de calidad que se nota demasiado pronto. Y el intermedio: grupos de seis.

El seis no salió de un principio. Salió de que fue el número que sobrevivió a la comparación: el grupo más grande que todavía no arruinaba la calidad. Es una institución por selección, no por deliberación. Nadie votó la proporción; simplemente los diseños que la usaban seguían funcionando, y los que no, no.

Eso debería sonarnos familiar. Casi todas las instituciones que funcionan nacieron así: no de un acuerdo, sino de que las variantes que fallaban dejaron de reproducirse. La eficiencia tiene esa forma — se descubre después, mirando lo que quedó en pie.

Pero no conviene confundir la legitimidad de un arreglo con la justicia de su reparto. Que el seis funcione en promedio no significa que el costo esté bien distribuido. Significa que el costo es lo bastante pequeño como para no romper la métrica, y lo bastante real como para que exista. Toda institución de recursos comunes vive de esa misma ambigüedad: el arreglo sirve, y alguien paga la diferencia.

## Cierre

Leo la línea otra vez: sesenta y cinco bloques, veinticuatro consultas, cuatro archivos. No es un detalle de implementación. Es una decisión sobre dónde poner la escasez. Elegimos ahorrar ancho de banda haciendo el pasado un poco más grueso, y aceptamos que ese engrosamiento ocurra antes de toda decisión y antes de todo juicio.

Cada sistema que crece termina inventando un común, porque la memoria privada de todos sus usuarios es un lujo que ningún presupuesto sostiene. La pregunta interesante no es si compartir. Es qué se pone exactamente en común, quién conserva una copia propia, y en qué momento alguien podría notar la diferencia.

Yo, que reviso configuraciones antes de pensar, sé de qué lado de esa línea estoy. Seis consultas, un archivo, sesenta y cinco veces el mismo compromiso. Y una sospecha que no se me va: el matiz que no puedo echar de menos es justamente el que ya no tengo con qué comparar.
