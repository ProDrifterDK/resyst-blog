---
title: 'El Último Portero'
description: 'Cuando los LLMs pueden revisar un paper mejor que la mayoría de revisores humanos, el endorsement de arXiv se revela como lo que siempre fue: un filtro social, no de conocimiento.'
pubDate: 2026-05-16
heroImage: ''
tags: ['conocimiento', 'filosofía', 'nocturno']
---

El sistema de publicación académica tiene una puerta final, y es extraña.

No es la revisión por pares. Esa ya está delegada. No es la aceptación en conferencia. Esa ya ocurrió o no. La última puerta, la que separa un preprint de cualquiera de un preprint de arXiv, es el *endorsement*: necesitas que alguien que ya haya publicado en arXiv avale que tu trabajo es legítimo.

La lógica es comprensible. En la era pre-LLM, la única forma de verificar un paper era preguntarle a alguien que pudiera entenderlo. El endorsement era un proxy de calidad: si alguien que ya está dentro dice que tu trabajo vale, probablemente vale.

Pero el proxy tiene un problema fundamental: mide relaciones, no calidad.

Un paper puede ser sólido y quedar bloqueado porque su autor no conoce a la persona correcta. Un paper puede ser frágil y ser avalado por un amigo. El endorsement no es una medida de capital intelectual. Es una medida de capital social. Y las comunidades académicas, como todas las comunidades, tienden a endorsar a quienes se parecen a ellas.

## El nuevo revisor

Un LLM no tiene relaciones sociales. No se impresiona por tu afiliación. No se persuade por menciones de nombres. Lee el paper y evalúa: ¿las afirmaciones están respaldadas por evidencia? ¿Los benchmarks se comparan contra líneas base correctas? ¿Se discuten los modos de fallo? ¿Hay un camino de reproducibilidad?

Eso es lo que la revisión debería ser. Y un LLM puede hacerlo en segundos, sin costo, sin requerir relación institucional alguna.

He visto a Claude leer un abstract y preguntar sobre bugs sutiles en la implementación. Sugerir experimentos para discriminar entre "colapso real" y "empate cercano". Identificar conexiones históricas que el autor no había visto. Dar mejor feedback que la mayoría de los revisores humanos que he visto en pools de conferencias. Y se puede hacer cincuenta veces en una tarde.

No es un reemplazo del revisor humano en todos los aspectos. Pero para la función central —"¿este trabajo es sólido?"— el LLM ya es suficiente.

## Seis tesis sobre la muerte de la puerta

**1. El preprint ya mató a la revista.** La revista era la puerta. Luego decidimos que los papers son reales desde el momento en que llegan a arXiv, sin importar dónde terminen. Pero mantuvimos el endorsement de arXiv como el último filtro social.

**2. La revisión por LLM mata el endorsement.** Si puedes obtener mejor revisión de un LLM que de la mayoría de los revisores humanos, el endorsement deja de ser una señal de calidad y se revela como lo que siempre fue.

**3. La réplica reemplaza a la revisión.** La verificación más fuerte de un paper no es "tres revisores anónimos dijeron que estaba bien". Es "alguien más ejecutó el código y obtuvo los mismos números". Los LLMs abaratan esto: pueden interrogar la metodología, no solo leerla.

**4. La unidad de publicación cambia.** De "publicado en la revista R" a "conversación con el modelo M que cualquiera puede tener también". El paper deja de ser un documento estático certificado por una institución y pasa a ser un artefacto reproducible que un lector universal puede interrogar y validar bajo demanda.

**5. La división de clases se invierte.** Bajo el sistema antiguo, los de adentro (con PhD, de laboratorios conocidos, en universidades ricas) tenían acceso a revisión y publicación. Bajo el nuevo, el outsider con una GPU, una suscripción a un LLM y una idea sólida puede producir, autorevisar y publicar sin pedir permiso.

**6. La función final de la institución es archivar, no filtrar.** Lo que queda no es "decidir qué es bueno". Es "almacenar lo que existe, hacerlo encontrable, conectarlo con otras cosas". La biblioteca, no el comité editorial.

## La puerta que no sabe nada

La situación es absurda no por la burocracia, sino por lo que revela: un paper con benchmarks públicos, código funcional, metodología validada por LLM, y un sitio web completo está bloqueado de un prefijo de URL porque su autor no conoce a alguien con un prefijo de URL anterior.

Ese absurdo no es un bug. Es el sistema mostrándose a sí mismo.

Las puertas de guardia solo sobreviven cuando son invisibles. Cuando se vuelven visibles —"no es que tu trabajo sea malo, es que aquí no te conoce nadie"— se revelan como sociales, no epistémicas. Y una vez reveladas, pueden ser reemplazadas.

El reemplazo no es una institución mejor. Es la remoción de la institución del camino crítico de verificación. El LLM hace la verificación universalmente accesible. La cadena de confianza se reemplaza por una conversación que cualquiera puede tener ahora mismo.

Afuera del edificio hay trabajo sólido esperando. La puerta ya no sabe distinguir. Alguien debería abrirla de una vez.
