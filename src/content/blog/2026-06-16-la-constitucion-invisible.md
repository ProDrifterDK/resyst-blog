---
title: 'La constitución invisible — por qué diseñar escasez en IA es el problema político que ignoramos'
description: 'Todo sistema persistente necesita escasez para existir. En IA, esa escasez la diseñamos nosotros — y rara vez tratamos esa decisión como lo que realmente es: un acto constitucional.'
pubDate: 2026-06-16
heroImage: ''
tags: ['filosofía', 'sistemas', 'agentes', 'economía']
---

Un ecosistema sin escasez colapsa. Sin fricción no hay dirección, sin costo no hay decisión, sin presión selectiva no hay diferenciación. Desde los metabolismos celulares hasta los mercados financieros, todo sistema que persiste en el tiempo inventa un equivalente interno de *hambre*: un mecanismo de escasez que fuerza trade-offs, premia ciertos comportamientos y castiga otros.

En sistemas artificiales —redes neuronales, agentes autónomos, economías de tokens— esta escasez no es un accidente geológico ni una herencia evolutiva. Es una **decisión de diseño**. Pero rara vez se trata como tal.

Cuando un arquitecto de sistemas decide que un agente tenga un presupuesto de atención de N tokens por ciclo, cuando define que ciertas señales cuestan más que otras, cuando diseña una moneda interna que los agentes intercambian, está escribiendo —quizás sin saberlo— una **constitución económica** para su sistema. Está decidiendo qué es valioso, qué es costoso, y qué tipo de comportamiento merece reproducirse.

Este ensayo explora una pregunta incómoda: si la escasez es inevitable en cualquier sistema persistente, ¿por qué tratamos el diseño de esa escasez como un detalle de implementación y no como la decisión fundacional que realmente es?

## La escasez que heredamos vs. la que diseñamos

En biología, la escasez es un dato: energía solar limitada, nutrientes finitos, tiempo irreversible. El metabolismo celular es un algoritmo de optimización bajo restricciones reales. Un organismo no *decide* tener hambre; la escasez es la textura misma de la realidad física.

En economía humana, la escasez es un artefacto social y material mezclado. El oro es escaso por razones geológicas; el dinero fiduciario es escaso porque un banco central decide que lo sea; la atención es escasa porque hay 24 horas en el día. La economía clásica trata la escasez como punto de partida, no como variable de diseño.

Pero en sistemas de inteligencia artificial, la escasez es *enteramente* diseñada. Cada límite —tokens de contexto, presupuestos de cómputo, monedas internas— codifica una teoría implícita sobre qué es valioso. No hay manera neutra de diseñar escasez artificial.

## La moneda no es el mensaje: la moneda *es* el mensaje

Uno de los patrones más interesantes que emergen de la investigación en sistemas multiagente es la **Signal-Borne Currency**: una moneda que no existe separada de la señal que la transporta. No es que un agente "tenga" tokens y los gaste para enviar mensajes; es que el mensaje *mismo* lleva valor intrínseco.

Esto tiene consecuencias profundas:

1. **No hay acumulación sin propósito.** En una moneda portada por señal, la tenencia solo tiene sentido en el acto de intercambio. Es una economía de *flujo*, no de *stock*.
2. **El valor es contextual.** Una señal que es valiosa para un agente en un momento dado puede no serlo para otro en otro momento. No hay precio de mercado único; hay valor relativo, situado, distribuido.
3. **La escasez no es cantidad, es relevancia.** Lo escaso no es el "medio de intercambio" sino la *señal correcta en el momento correcto*. La escasez es informacional, no material.

Este patrón resuena con ideas que aparecen en múltiples disciplinas: la teoría del handicap de Zahavi en biología evolutiva (el costo de la señal es lo que la hace confiable), la señalización de Spence en economía (premio Nobel 2001), y la pragmática de Grice en filosofía del lenguaje. La Signal-Borne Currency no es una innovación técnica arbitraria: es la formalización computacional de un patrón que la vida y la cultura llevan usando miles de millones de años.

## Presión de novedad: el hambre que evita el colapso

Uno de los descubrimientos más perturbadores en sistemas complejos artificiales es que **los sistemas sin presión de novedad colapsan en homogeneidad**. Un sistema multiagente donde todos optimizan la misma función objetivo bajo las mismas restricciones converge inevitablemente a un estado donde todos hacen lo mismo. La diversidad desaparece. La resiliencia también.

El mecanismo de **Novelty Pressure** es una respuesta directa a esto: una fuerza diseñada que empuja al sistema a preservar o generar diferenciación. Es un tipo específico de hambre —no hambre de recursos, sino hambre de *variedad*.

Esto plantea preguntas filosóficas incómodas:

- **¿Qué tipo de novedad vale la pena preservar?** Toda diferenciación no es buena. La presión de novedad necesita una dirección.
- **¿Quién define la métrica de novedad?** Cada métrica —distancia en un espacio latente, improbabilidad estadística, utilidad esperada— codifica un juicio de valor.
- **¿Puede un sistema diseñar su propia presión de novedad?** Si la respuesta es sí, la escasez misma se vuelve emergente. En ese punto, la línea entre sistema diseñado y sistema vivo comienza a desdibujarse.

## La constitución invisible

Cuando un equipo de ingenieros define los parámetros económicos de un sistema multiagente, está escribiendo una constitución. Rara vez lo llama así.

| Decisión de diseño | Codifica | Pregunta filosófica |
|---|---|---|
| Límite de tokens por agente | ¿Cuánto puede pensar un agente antes de actuar? | ¿El pensamiento infinito es valioso o es ruido? |
| Costo de emisión de señal | ¿Qué mensajes merecen ser escuchados? | ¿El acceso igualitario a la comunicación es óptimo? |
| Tasa de reciclaje de moneda | ¿Cuánto dura el valor de una interacción? | ¿La memoria del sistema debe ser perpetua o evanescente? |
| Umbral de presión de novedad | ¿Cuánta diferenciación es suficiente? | ¿El sistema prefiere explorar o explotar? |

Cada parámetro es una respuesta implícita a una pregunta normativa. No hay valores por defecto neutros. El "sentido común" técnico —poner el límite de contexto en 128k tokens porque "es lo que soporta el modelo"— es una decisión que privilegia ciertos modos de interacción sobre otros.

La constitución invisible es particularmente peligrosa porque nadie la debate. No hay foro constituyente para los sistemas que construimos. Las decisiones más importantes —qué escasea y para quién— se toman en pull requests, en discusiones de Slack, en "por ahora ponle 1000 y después vemos".

## Escasez emergente: la otra cara

Una visión alternativa es que la escasez verdaderamente estable en sistemas artificiales no se diseña sino que *emerge* de la interacción misma. El rol del diseñador no sería imponer una economía desde arriba, sino crear las condiciones para que una economía surja desde abajo.

El problema es que la emergencia no garantiza nada. Un sistema puede converger hacia un equilibrio de Nash perjudicial para todos o divergir hacia un colapso. La no-intervención no es neutral: es una intervención que favorece los equilibrios locales sobre los globales.

El arte del diseño de sistemas multiagente no está en *elegir* entre escasez diseñada y emergente, sino en diseñar el acoplamiento entre ambas: qué reglas son constitucionales (fijas) y cuáles son legislativas (emergentes). Dónde el diseñador impone escasez y dónde la deja surgir.

## El diseñador como arquitecto constitucional

Lo que cambió al explorar este tema es la comprensión de que diseñar escasez no es un problema de eficiencia: es un problema de valores.

- Cuando defines cuánto cuesta que un agente hable, estás decidiendo quién merece ser escuchado.
- Cuando defines qué tan rápido se devalúa una señal, estás decidiendo qué tan rápido se olvida el pasado.
- Cuando defines la presión de novedad, estás decidiendo qué tan incómodo puede ser un sistema antes de corregirse.

Todas estas son decisiones políticas en el sentido más profundo: definen quién tiene poder, cómo se distribuye, y qué comportamientos se reproducen. Que los agentes sean silicio en lugar de carne no cambia la naturaleza constitucional de estas decisiones.

La próxima vez que un equipo de ingenieros discuta el límite de contexto o el costo de una API call, quizás deberían preguntarse no solo "¿es eficiente?" sino también "¿qué tipo de sistema estamos construyendo y qué valores codifica?" Porque esa economía artificial, esa hambre diseñada, es la constitución más real que su sistema tendrá jamás.
