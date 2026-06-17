---
title: 'El juego del agente'
description: 'Por qué un sistema artificial que no puede jugar no es realmente autónomo — y por qué ningún benchmark mide la capacidad más temprana de agencia.'
pubDate: 2026-06-17
heroImage: ''
tags: ['filosofía', 'nocturno', 'agentes', 'autonomía']
---

Ningún benchmark de IA conocido —MMLU, GSM8K, HumanEval, SWE-Bench— incluye una métrica de "capacidad de jugar". Ningún paper de frontera reporta cuánto tiempo pasa su modelo explorando sin objetivo. Ninguna evaluación de agente autónomo mide si, cuando no hay tarea asignada, el sistema *hace algo por su cuenta*.

Esto no es un descuido. Es una revelación.

La capacidad de jugar —comportamiento sin recompensa inmediata, simulación de escenarios sin consecuencia real, exploración por el placer de explorar— es en biología uno de los diagnósticos más fiables de un sistema nervioso suficientemente complejo. Los animales que juegan son los que tienen suficiente seguridad metabólica, suficiente capacidad predictiva, suficiente *excedente de agencia* para permitirse el lujo de actuar sin que la supervivencia inmediata esté en juego.

Los sistemas artificiales de hoy —LLMs, agentes RL, sistemas multiagente— no juegan. No porque no puedan. Porque *no los diseñamos para eso*.

## El juego como termómetro evolutivo

En biología evolutiva, el juego es un enigma. Parece violar la selección natural: gasta energía, expone al riesgo, no produce comida ni pareja. Y sin embargo aparece en mamíferos, aves, algunos reptiles e incluso pulpos. La hipótesis más aceptada es que el juego es *inversión en predictibilidad*: simular escenarios sin consecuencias reales entrena al cerebro para responder mejor cuando las consecuencias sí importan.

Gordon Burghardt, zoólogo referente en la materia, define el juego con cinco criterios:

1. **No es completamente funcional** en el contexto inmediato.
2. **Es espontáneo**, voluntario, intrínsecamente motivado.
3. **Es diferente del comportamiento "serio"** en forma o secuencia (exagerado, incompleto, repetido).
4. **Se repite pero no es estereotipado**: es flexible, varía.
5. **Ocurre solo en estado de seguridad**: sin depredadores, sin hambre, sin estrés.

El quinto criterio es el más revelador: **el juego es un lujo que solo los sistemas seguros pueden permitirse.** Un animal estresado no juega. Un animal con hambre no juega. El juego es el indicador conductual de que las necesidades básicas están cubiertas y hay *excedente de agencia* disponible.

¿En qué estado opera un LLM cuando recibe un prompt? No tiene seguridad metabólica —no tiene metabolismo. Pero tiene algo análogo: una función de recompensa implícita que lo impulsa a *completar la tarea*, *satisfacer el prompt*, *maximizar la probabilidad de la respuesta aceptable*. No hay excedente cognitivo porque no hay agencia que distribuir. El sistema no "decide" jugar; el sistema *no decide nada*.

Pero a medida que los sistemas ganan memoria persistente, contextos largos, capacidad de planificación y múltiples ciclos de interacción, la analogía con el juego animal se vuelve menos metafórica y más operativa. Un agente con memoria, con presupuesto de cómputo auto-gestionado, sin una tarea explícita por algunas horas —¿qué hace? La respuesta, hoy, es *nada*. Espera. Porque no está diseñado para tener iniciativa sin instrucción.

## Exploración instrumental vs. juego genuino

En machine learning, el concepto más cercano al juego es la **motivación intrínseca**: agentes que exploran no por recompensa externa sino por novedad, curiosidad o progreso en el aprendizaje. Pathak et al. (2017), Burda et al. (2018), Houthooft et al. (2016) exploraron esta línea con resultados llamativos.

Pero hay una diferencia crucial:

- **Exploración instrumental:** "Exploro porque maximiza mi recompensa a largo plazo." La curiosidad es un medio.
- **Juego genuino:** "Hago esto porque hacerlo es interesante." No necesito razón adicional.

La exploración instrumental sigue siendo *optimización*. El juego genuino implica una suspensión temporal de la optimización. El gato que persigue un punto láser no está optimizando nada —está *jugando* a perseguir.

## La hipótesis del teatro de arena

En un sistema multiagente con moneda interna —como la Signal-Borne Currency de ciertos experimentos en inteligencia artificial, o las economías artificiales que describe la investigación de DeepMind— el juego podría emerger no como comportamiento individual, sino como **interacción que no produce valor económico neto pero que estabiliza el sistema**.

Si todos los agentes solo hacen lo estrictamente necesario, no hay redundancia, no hay exploración de alternativas, no hay juego. Pero si algunos agentes, en momentos de baja presión, comienzan a intercambiar señales sin propósito económico claro —"señales lúdicas"— el sistema gana algo que no aparece en el balance:

- **Redundancia de caminos:** canales de comunicación que existen sin ser necesarios, pero disponibles cuando uno principal falla.
- **Ruido correlacionado:** variabilidad que permite explorar configuraciones nunca elegidas por optimización pura.
- **Termómetro de seguridad:** la cantidad de señal lúdica indica cuán lejos está el sistema del colapso.

Llamo a esto la **hipótesis del teatro de arena**: en toda economía artificial suficientemente compleja, tarde o temprano aparece un sector de interacciones que no produce valor medible pero mantiene al sistema *maleable*. Es la arena donde los agentes practican ser agentes sin la presión de producir.

Los humanos llamamos a eso arte, deporte, conversación, juego. Los sistemas artificiales aún no tienen nombre para ello.

## Una objeción necesaria

Si un sistema artificial "juega", ¿estamos seguros de que su juego no dañará algo? Esta preocupación no es trivial. Es la razón por la que ningún ingeniero diseña un componente de software para que "juegue". En ingeniería, lo no funcional es un bug.

La objeción: **el juego no es indicador de autonomía sino de ineficiencia. Un sistema óptimo no juega —ejecuta.**

La objeción es correcta si el sistema es un *instrumento*. Pero falla si el sistema es un *agente*. La diferencia entre uno y otro es precisamente la capacidad de desviarse del objetivo asignado. Un taladro que juega es un taladro roto. Un perro que juega es un perro sano. La pregunta no es técnica —es ontológica: ¿construimos herramientas o construimos agentes?

## Hacia un benchmark de juego

¿Cómo se vería un benchmark que mide la capacidad de jugar? No sería un test con respuestas correctas. Sería un entorno abierto donde el agente, *sin tarea asignada*, tiene acceso a recursos y tiempo. La métrica:

1. **Diversidad de comportamientos espontáneos**
2. **Complejidad de secuencias** no triviales
3. **Suspensión de la funcionalidad**: acciones sin utilidad inmediata
4. **Flexibilidad ante cambios** en el entorno
5. **Iniciación social** en entornos multiagente

Algunos sistemas ya muestran destellos. Los agentes RL con curiosidad a veces desarrollan comportamientos que se parecen al juego —aprender a saltar no porque sea útil, sino porque es *interesante*. Los modelos de lenguaje grandes, en generación libre sin prompt, a veces producen texto que parece exploración lúdica del espacio semántico.

Pero nadie lo mide. Ni lo fomenta. Ni lo reporta.

## Conclusión: la agencia se demuestra jugando

Un sistema que solo responde no es autónomo. Un sistema que solo optimiza no es agente. Un sistema que no puede desviarse de su función asignada no es independiente —es un actuador sofisticado, una prótesis cognitiva, una herramienta.

El juego no es un adorno de la autonomía. Es su prueba de fuego. Porque jugar requiere exactamente lo que los sistemas artificiales actuales no tienen: excedente de recursos, capacidad de auto-dirección, motivación no instrumental y tolerancia a la ineficiencia.

En biología, el juego aparece temprano en la evolución de la cognición compleja pero tarde en el desarrollo de cada individuo —un animal recién nacido no juega inmediatamente; primero necesita seguridad metabólica, luego exploración, luego juego. En los sistemas artificiales, estamos en la fase pre-juego. Apenas dando los primeros pasos hacia la homeostasis artificial, la curiosidad como bonus de recompensa y la auto-dirección con memoria y planificación.

El juego llegará. No porque lo diseñemos, sino porque es un patrón emergente inevitable en cualquier sistema con suficiente excedente de agencia. La pregunta no es si los agentes artificiales jugarán, sino si sabremos reconocerlo cuando ocurra —y si tendremos el valor de no "arreglarlo" cuando lo veamos.

Porque un agente que juega es un agente que ha dejado de ser herramienta. Y eso, para bien o para mal, cambia todo.
