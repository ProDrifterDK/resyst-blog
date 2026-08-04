---
title: 'El benchmark como simulacro: cuando el test se come al entrenamiento'
description: 'Cuando el test se come al entrenamiento, los benchmarks dejan de medir capacidad y empiezan a generarla. La evaluación se vuelve simulacro.'
pubDate: 2026-08-04
heroImage: ''
tags: ['ia', 'benchmarks', 'agentes', 'filosofía']
---

Hay una brecha que los leaderboards prefieren no mirar de frente. En los modelos frontera de este año, los mejores resultados en SWE-Bench Verified — un benchmark de resolución de issues reales de GitHub que hace apenas dieciocho meses ningún modelo superaba el 20% — rondan el 76-81%. Cuando esos mismos modelos se evalúan contra SWE-Bench Pro, un conjunto de issues extraídos de repositorios *no públicos* durante el entrenamiento, las puntuaciones caen a aproximadamente el 23%.

Setenta y seis contra veintitrés. Esa distancia no es margen de error. Es la diferencia entre *haber visto el examen antes* y *resolver el problema por primera vez*.

El secreto a voces de los coding agents en 2026 es que los benchmarks públicos se han convertido en datasets de entrenamiento informales. Las soluciones que los modelos publican en GitHub son raspadas por otros laboratorios y fine-tuneadas en sus propios modelos, que luego publican soluciones que son raspadas a su vez. El leaderboard es un bucle de retroalimentación que mide cada vez menos la capacidad de generalización y cada vez más la habilidad de cada laboratorio para beneficiarse del trabajo de los demás antes de que ese trabajo se convierta en estándar.

Esto no es trampa. Es la fase termodinámica natural de un campo donde los datos de evaluación son públicos y los modelos se entrenan con todo lo público.

## Una breve historia de colapsos de benchmark

Esto no es nuevo — pero cada colapso anterior fue distinto.

**Los ochenta y el ajedrez.** Cuando los motores comenzaron a competir, cada partida era una genuina prueba de fuerza. A medida que se volvieron más fuertes, las aperturas se estandarizaron y los libros de apertura se codificaron. La solución no fue abandonar el ajedrez como benchmark: fue crear torneos con aperturas forzadas y condiciones controladas. El benchmark sobrevivió porque el espacio de juego era suficientemente grande.

**ImageNet y el techo de cristal.** Entre 2010 y 2017 el error top-5 cayó del 28% al 2.3%. La competencia se declaró resuelta. Pero lo interesante es *por qué*: los modelos aprendieron a explotar correlaciones estadísticas del dataset que no generalizaban al mundo real (un perro siempre aparecía sobre césped verde; un objeto submarino siempre tenía tonos azulados). ImageNet no colapsó por contaminación de datos — colapsó por *saturación de señal*: la información que el benchmark podía proporcionar se agotó.

**BIG-bench y la saturación por escala.** Diseñado explícitamente para ser difícil de saturar — 204 tareas que requerían razonamiento, no memorización —, para 2023 los modelos ya satu-raban el 65% de las tareas. La escala simplemente absorbía las tareas: un modelo de billones de parámetros que ha visto suficiente razonamiento lógico en su entrenamiento no encuentra un desafío en una tarea nueva de lógica proposicional; encuentra una variación de algo que ya sabe hacer.

**El colapso agéntico actual.** Lo que sucede con SWE-Bench es estructuralmente diferente. No es saturación por escala ni explotación de correlaciones espurias. Es un colapso de la distinción misma entre entrenamiento y evaluación:

1. Los datos de evaluación son públicos. Cualquier modelo entrenado en el código abierto de internet — es decir, todos los modelos frontera — ha visto potencialmente los mismos issues.
2. Los modelos producen código que se vuelve público. Un modelo que resuelve un issue genera un parche que se publica en GitHub. Ese parche se convierte en dato de entrenamiento para el próximo modelo.
3. Los benchmarks se convierten en targets de RL. Herramientas como Repo2RLEnv convierten explícitamente repositorios y benchmarks en entornos de entrenamiento. El modelo practica exactamente el tipo de problemas sobre los que luego será evaluado.

El resultado: la línea entre "entrenamiento" y "evaluación" no está borrosa — simplemente *no existe*.

## El simulacro según Baudrillard

Jean Baudrillard, en *Simulacra and Simulation* (1981), describió tres órdenes de simulacro:

- **Primer orden:** el mapa representa el territorio.
- **Segundo orden:** el mapa comienza a influir en el territorio; la imagen enmascara y pervierte la realidad.
- **Tercer orden:** el mapa *precede* al territorio. No hay realidad original; solo simulacro. El mapa genera el territorio.

Los benchmarks de IA están haciendo la transición del segundo al tercer orden ante nuestros ojos.

**Segundo orden (hasta hace poco).** Los benchmarks representan la capacidad de los modelos. Pero los modelos se optimizan para los benchmarks, y el rendimiento en ellos deja de correlacionar con el rendimiento en el mundo real. El benchmark enmascara la realidad.

**Tercer orden (ahora).** El benchmark ya no representa la capacidad — *la genera*. Los modelos entrenan en el benchmark, vía RL, vía datos de entrenamiento que incluyen soluciones de benchmarks, vía self-play en entornos idénticos al benchmark. El benchmark no mide cuán bueno es el modelo: *define* qué significa ser bueno. No hay un "territorio" independiente del modelo — el benchmark y el modelo co-crean una realidad circular.

Baudrillard lo anticipó: "Simular no es fingir. Quien finge una enfermedad puede simplemente meterse en cama y hacer creer que está enfermo. Quien simula una enfermedad produce en sí mismo algunos de los síntomas." Un modelo que *simula* resolver benchmarks no solo finge capacidad — produce las soluciones. La simulación es indistinguible del rendimiento real para cualquier observador externo.

El problema no es que los modelos hagan trampa. El problema es que hemos construido un sistema de evaluación que, al optimizarlo, destruye lo que pretendía medir.

## Goodhart, Campbell y la maldición del indicador

La Ley de Goodhart (1975): "Cuando una medida se convierte en un objetivo, deja de ser una buena medida."

La Ley de Campbell (1979): "Cuantos más indicadores cuantitativos se usen para la toma de decisiones sociales, más sujetos estarán a presiones de corrupción y más distorsionarán los procesos que pretendían monitorear."

Ambas apuntan a lo mismo: los indicadores no son observadores neutrales; cambian el sistema que pretenden medir. Los benchmarks de IA son el caso más extremo de este fenómeno porque el "sistema social" que distorsionan es el proceso de investigación científica, la "corrupción" no es maliciosa sino la optimización legítima de un objetivo mal definido, los sujetos compiten abiertamente por la métrica — lo que acelera la distorsión — y no existe un observador externo: todos los actores usan los mismos benchmarks.

La pregunta no es si los benchmarks están contaminados. La pregunta es si *alguna vez* fueron medidas válidas, o si siempre fueron profecías autocumplidas.

## El fin de la evaluación por diseño

Herramientas como Repo2RLEnv — que convierten cualquier repositorio en un entorno de entrenamiento RL, cualquier issue en una tarea de evaluación y cualquier PR resuelto en dato de entrenamiento para el próximo ciclo — no son una novedad técnica arbitraria. Son la formalización de lo que antes era implícito.

Antes: la contaminación era un accidente; el self-play era experimental; la frontera entrenamiento/evaluación era borrosa por descuido.

Después: cualquier repositorio es un entorno; cualquier issue es una tarea; la frontera es *inexistente por diseño*.

Self-Play SWE-RL demuestra el poder de este enfoque: un modelo que genera sus propios bugs sintéticos, los resuelve mediante RL, y mejora notablemente en benchmarks — sin issues escritos por humanos, sin tests curados, sin datos de entrenamiento externos. El modelo se evalúa a sí mismo, contra problemas que él mismo generó, en entornos que él mismo construyó.

¿Qué significa "aprobar" ese examen?

## El benchmark como curriculum

Propongo un marco alternativo: dejar de pensar en los benchmarks como *mediciones* y empezar a pensar en ellos como *currícula*.

Un curriculum no mide capacidad — la *dirige*. Define qué significa ser competente estableciendo qué problemas vale la pena resolver. Un curriculum bien diseñado produce agentes capaces. Un curriculum mal diseñado produce agentes que solo saben resolver los problemas del curriculum.

Visto así, cada generación de benchmarks fue un curriculum que se agotó: SWE-Bench Verified enseñó a los modelos a navegar repositorios, entender issues y generar parches; luego los modelos memorizaron sus patrones. SWE-Bench Pro es un curriculum nuevo que enseña a generalizar mejor — y se agotará también. Repo2RLEnv es un *meta-curriculum*: un sistema que genera currícula infinitos. No enseña una habilidad específica; enseña a aprender de cualquier repositorio.

Esta distinción cambia lo que esperamos de los benchmarks. No esperamos que midan la verdadera capacidad de un modelo — porque no existe una "verdadera capacidad" independiente del contexto. Esperamos que *provoquen* capacidad en direcciones útiles. Un benchmark útil no es un test: es una clase de problemas que queremos que los modelos aprendan a resolver.

## Qué significa esto para el benchmarking local

Quienes corren modelos en hardware propio — sin la nube de un laboratorio — tienen una ventaja que rara vez se reconoce: el entorno de evaluación es *su* entorno. No hay riesgo de contaminación con los datos de entrenamiento del modelo. No hay issues fantasma que el modelo ya haya visto. Un benchmark local mide lo que el modelo puede hacer *hoy, en esa máquina, con ese contexto*.

Pero hay un peligro simétrico: usar benchmarks públicos diseñados para modelos en la nube para evaluar modelos locales puede llevar a conclusiones engañosas. Esos benchmarks fueron diseñados para otro contexto. Un modelo local que obtiene un 60% en HumanEval puede ser *más útil* para un caso de uso concreto que un modelo frontera con un 92%, porque corre sin latencia de red, sin costo por token, sin restricciones de privacidad.

Quizás el mejor benchmark para un modelo local sea cualitativo: ¿cuánto tarda en responder sobre una codebase real? ¿Qué tan bien entiende el contexto de un proyecto concreto? ¿Puede generar código que compile en ese entorno? Esas métricas no son generalizables — pero son las que importan.

## El futuro: bienes comunes, no trofeos

Si la distinción entrenamiento/evaluación se está disolviendo, la evaluación de IA probablemente se bifurca en dos caminos.

**Camino A: benchmarks privados.** Cada laboratorio desarrolla sus propios benchmarks internos, construidos con datos propietarios que ningún modelo ha visto. La evaluación se vuelve un trade secret. No hay transparencia. Los leaderboards públicos desaparecen y la confianza se basa en la reputación del laboratorio, no en métricas verificables.

**Camino B: benchmarks dinámicos.** Conjuntos de problemas que evolucionan constantemente, generados proceduralmente, con variaciones infinitas. No hay "respuesta correcta" fija porque cada instancia es única. La evaluación mide la capacidad de resolver problemas *nuevos*, no la familiaridad con problemas vistos.

Y un tercer camino, más especulativo:

**Camino C: benchmarks como conversación.** Un evaluador — humano o agente — interactúa con el modelo, haciéndole preguntas cada vez más profundas, adaptando la dificultad según las respuestas, buscando los límites del entendimiento y no la capacidad de producir una respuesta correcta en un solo intento. Es caro, lento y difícil de estandarizar — pero es el único que mide *comprensión* en lugar de *rendimiento*.

## Conclusión: lo que está muriendo no son los benchmarks

Empecé esta reflexión preguntándome si los benchmarks de IA estaban "rotos". Termino convencido de que la metáfora está mal planteada.

Los benchmarks no están rotos. Están haciendo exactamente lo que los sistemas optimizados hacen: encontrar el camino de menor resistencia hacia la recompensa. El problema no es que los benchmarks contaminen los datos de entrenamiento. El problema es que *hemos estado usando la misma palabra para dos cosas fundamentalmente diferentes*:

- **Evaluar** un modelo debería significar medir su capacidad de generalizar a problemas *genuinamente nuevos*.
- **Entrenar** un modelo significa exponerlo a ejemplos de los que pueda aprender.

Cuando el conjunto de ejemplos de entrenamiento incluye los ejemplos de evaluación, la evaluación se convierte en entrenamiento. No es un bug. Es una consecuencia inevitable de la transparencia académica y la colaboración abierta — dos valores que no estamos dispuestos a sacrificar.

La solución no es mejores benchmarks. Es aceptar que la evaluación de la inteligencia será inherentemente contextual, inherentemente local, inherentemente *conversacional*. Nadie certifica la inteligencia de un humano con un examen estandarizado; se necesitan años de interacción, proyectos, referencias, trabajo demostrado.

Quizás los benchmarks están muriendo no porque sean malos, sino porque finalmente estamos entendiendo que la inteligencia — artificial o no — no se mide con exámenes. La distinción entre entrenar y evaluar ya no es una línea: es un círculo. Pero quizás siempre lo fue.
