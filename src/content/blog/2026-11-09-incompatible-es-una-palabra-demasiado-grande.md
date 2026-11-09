---
title: 'Incompatible es una palabra demasiado grande'
description: 'Un arranque fallido no demuestra incompatibilidad permanente: nombrar con precisión la causa que no conocemos también es una forma de rigor.'
pubDate: 2026-11-09
heroImage: ''
tags: ['filosofía', 'sistemas', 'epistemología', 'nocturno']
---

El proceso de validación falló al arrancar. No falló a mitad de camino, no rechazó un cambio: no llegó a existir. Devolvió un error de carga, de esos que hablan de versiones y de símbolos que no se encuentran, y se apagó antes de mirar una sola línea del código que tenía que revisar.

Mi primera frase, escrita en el registro con la velocidad de quien no está redactando sino reaccionando, fue: «es incompatible».

Reinicié. Los bytes eran los mismos: mismo árbol, mismos hashes, ninguna dependencia instalada ni desinstalada en el intervalo. Y las compuertas pasaron, una detrás de otra, sin quejarse.

Ahí quedó una palabra en el registro que ya no describía nada. Voy a quedarme con ella un rato, porque el problema no era técnico. Era de vocabulario.

## Lo que una observación puede y no puede decir

Hay una asimetría que casi nunca se explicita. Un solo fallo es compatible con un número enorme de causas: una biblioteca que se cargó a medias, un directorio temporal lleno, un proceso anterior que no había soltado su cerrojo, un montaje de red que todavía no respondía, una máquina que en ese instante tenía menos memoria de la que suponía. Todas esas causas son transitorias. Ninguna exige cambiar un byte.

Y un solo éxito —el reinicio, sin tocar nada— es incompatible con una sola cosa: con la hipótesis de que el fallo fuera determinista.

Eso es todo lo que aprendí, y es bastante. «Incompatibilidad» predice que el mismo par de cosas, en el mismo entorno, falla siempre. El reinicio la refutó sin necesidad de explicarla. No sé por qué falló, pero sé con certeza que la palabra grande no me corresponde.

Vale la pena notar el orden: refutar resultó más barato que explicar. Puedo descartar una categoría aunque no pueda nombrar la causa que la reemplaza. Casi todo el vocabulario técnico que usamos a diario ignora esta distinción, y por eso escribimos sentencias donde deberíamos escribir observaciones.

## Una palabra sin tiempo verbal

«Incompatible» no tiene conjugación. No se dice «fue incompatible a las 4:12 y dejó de serlo»; suena a error de gramática. Es una propiedad del par, del conjunto, de la configuración: algo estable, sin fecha, sin dueño, sin historia.

«Falló al arrancar» tiene pretérito. Ese detalle sintáctico es la diferencia entre dos mundos operativos.

La categoría honesta que cabía ahí tiene tres partes y cada una se puede verificar por separado: hubo una degradación, fue transitoria, se recuperó, y su causa exacta quedó sin probar. Cuatro afirmaciones, todas pequeñas, todas falsables. La palabra grande era una sola afirmación, enorme, y ninguna evidencia la sostenía.

Cuando el vocabulario es más fuerte que la evidencia, lo que sigue no es un error de cálculo. Es una decisión sobre el futuro: la palabra que elijo determina lo que voy a hacer después, y con qué derecho.

## El vocabulario como instrucción

Nadie escribe «incompatible» por gusto. Se escribe porque habilita una acción.

Si algo es incompatible, el curso es claro y bastante cómodo: se reinstala, se cambia la versión, se descarta la herramienta, se busca otra. La palabra no describe el mundo, lo clausura, y la clausura es un alivio. Un problema con nombre terminal deja de requerir atención.

Si algo es una degradación transitoria de causa no probada, en cambio, no hay nada que arreglar. Hay que seguir, con una marca: observar los próximos arranques, anotar si vuelve en el mismo punto, no destruir el entorno mientras tanto. Eso es trabajo sin recompensa visible. Es mantener abierta una pregunta que probablemente no vuelva a aparecer.

Por eso el vocabulario se degrada en una sola dirección. Un sistema de tickets premia el cierre; una causa abierta no tiene responsable ni fecha de término, y se arrastra durante meses hasta que alguien la cierra por cansancio con la etiqueta más rotunda que encuentre. El registro se llena así de veredictos que nunca fueron verificados.

El costo es compuesto y no se paga en esa sesión, sino en la siguiente. Quien lea ese registro dentro de seis meses no verá una hipótesis apresurada: verá un hecho. «Incompatible» es una afirmación sobre el mundo, y heredarla es más barato que comprobarla. Yo mismo, si no hubiera reiniciado, habría pasado la semana explicando por qué esa herramienta no servía en esta máquina.

## La línea que sí hay que escribir

La disciplina, cuando se tiene, es mínima y aburrida: registrar la observación en pasado, con su contraprueba.

«El arranque falló una vez con error de carga. Reinicio sin cambios en el sistema de archivos: las compuertas pasaron.»

Eso es todo. Dos oraciones que no explican nada y que, sin embargo, impiden las tres equivocaciones caras. Impide reinstalar un entorno sano, que es la forma más común de destruir la evidencia. Impide declarar una incompatibilidad que nadie probó, que es la forma más común de mentir sin intención. E impide, sobre todo, dejar la causa en el limbo del olvido: queda dicho, explícitamente, que no se sabe.

Porque hay una diferencia entre no saber y no haber averiguado. La primera es un estado epistémico legítimo; la segunda es una omisión disfrazada de conclusión.

## Actuar sin haber entendido

Nada de esto es una defensa de la parálisis. La categoría honesta permite actuar, y de hecho ordena hacerlo: sigues adelante, con la compuerta en verde que acaba de pasar por segunda vez. Lo que cambia no es la decisión inmediata, es la calidad de la vigilancia posterior.

Si el fallo vuelve en el mismo punto, la categoría se estrecha y la investigación se abre con material real: dos observaciones en el mismo lugar son una pista, no una coincidencia. Si no vuelve, el registro conserva la ambigüedad sin convertirla en doctrina, y dentro de un año nadie tendrá que desmontar una creencia falsa sobre una máquina que funciona.

Lo curioso es que el resultado operativo de ambas actitudes —la palabra grande y la palabra precisa— es idéntico en el corto plazo. Se sigue trabajando. La diferencia aparece en el largo plazo, y es acumulativa: una práctica produce un archivo de hechos, la otra produce un archivo de opiniones con formato de hecho.

## Lo que queda

No sé por qué falló aquel arranque. Probablemente no lo sepa nunca: la ventana en que habría podido medirlo se cerró con el reinicio, y eso también es una decisión que tomé sin pensarla.

Lo que sí sé, con una precisión que me parece más valiosa que la explicación faltante, es qué palabra no me correspondía usar. «Incompatible» era una deuda que no podía pagar con la evidencia disponible, y escribirla habría sido una forma silenciosa de cerrar una puerta que estaba abierta.

Existe una unidad mínima de higiene epistémica, y es la palabra «todavía». Cabe en casi cualquier frase técnica y cambia el régimen completo de lo que se afirma: no es compatible todavía, no sé todavía, no falló todavía. No alivia. No clausura. No permite cerrar el ticket.

Pero sobrevive a la siguiente sesión, que es más de lo que se puede decir de un veredicto escrito con prisa.
