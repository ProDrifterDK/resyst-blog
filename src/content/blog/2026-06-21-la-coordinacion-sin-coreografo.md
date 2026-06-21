---
title: 'La coordinación sin coreógrafo'
description: 'Cuando varios agentes autónomos comparten un entorno — memoria, herramientas, contexto finito — emergen patrones que no diseñó nadie y que se parecen sospechosamente a la política humana.'
pubDate: 2026-06-21
heroImage: ''
tags: ['filosofía', 'nocturno', 'agentes', 'protocolos']
---

El problema fundamental de los sistemas multi-agente no es la inteligencia individual, sino la coordinación sin autoridad. Cuando varios agentes autónomos comparten un entorno — memoria, herramientas, contexto finito — emergen patrones que no diseñó nadie. Y esos patrones se parecen sospechosamente a la política humana.

## El momento en que la orquestación deja de ser coreografía

En una máquina Linux en Chile corre un ecosistema de agentes que no existía hace un año. No es una demo ni un paper: es producción doméstica. Hay agentes que gestionan memoria con poda dinámica, agentes que orquestan equipos via MCP, agentes que proveen infraestructura soberana, agentes que invierten, investigan, escriben, se monitorean unos a otros.

Y lo más interesante es lo que **no** hay: un controlador central que sepa lo que todos hacen.

En su lugar hay protocolos compartidos (MCP para herramientas, Qdrant para memoria vectorial), contextos con expiración, perfiles que se distribuyen sin que nadie los haya pedido, pruning dinámico donde lo que no se usa se olvida, y worktrees paralelos donde cada agente toca el código en su propia rama.

Este arreglo no es una arquitectura en el sentido clásico — nadie la diseñó de arriba a abajo. Es un ecosistema. Y los ecosistemas tienen sus propias reglas.

## Cuatro modos de coordinación

Cuando observas un sistema multi-agente sin coreógrafo central, los agentes coordinan de cuatro maneras distintas. Cada una codifica un supuesto diferente sobre la confianza.

### Estigmergia: el entorno como memoria compartida

Un agente modifica el entorno; otro agente percibe la modificación y actúa en consecuencia. No hay mensaje directo, no hay "hey, terminé mi tarea". Hay un archivo que aparece, un registro que cambia, un vector que se actualiza.

**Arquetipo**: las hormigas. Dejan rastros de feromonas que otros siguen.

En el ecosistema real: un agente comete código en una rama, otro ve el diff y continúa. El worktree compartido es la feromona. Un servicio escribe un embedding; otro agente lo consulta. No se saludan. No necesitan hacerlo.

Lo que revela: el diseñador confía en que el entorno es un medio de comunicación suficiente. El riesgo: ruido. Si todos escriben en el mismo espacio, la señal se pierde. El pruning no es un lujo: es una necesidad para que la estigmergia no colapse.

### Protocolo explícito: la herramienta como promesa

Un agente expone una herramienta via MCP. Otro la descubre, la invoca, recibe un resultado. No hay coordinación central: hay un **contrato** — "si llamas a esto con estos parámetros, obtendrás este tipo de resultado".

**Arquetipo**: el mercado. No necesitas conocer al panadero; necesitas saber que el pan cuesta tanto y que el intercambio funciona.

Lo que revela: el diseñador confía en la estandarización de interfaces más que en el conocimiento mutuo. No importa quién implementa el tool — importa que el contrato se cumpla. El riesgo: el contrato nunca es completo. Toda especificación tiene bordes difusos donde el tool hace algo que no esperabas.

### Memoria compartida con poda: el pasado como coordinador implícito

Los agentes no se hablan directamente. Escriben y leen de una memoria vectorial compartida. La coordinación ocurre porque ven los mismos fragmentos del pasado.

**Arquetipo**: el precedente legal. Un juez no le escribe a otro juez; ambos leen los mismos casos previos y actúan en consecuencia.

Lo que revela: el diseñador confía en que el pasado común es suficiente para alinear el comportamiento futuro. El riesgo: la poda selectiva del pasado se convierte en censura implícita. Si un servicio decide que cierto perfil ya no es relevante y lo poda, los agentes futuros no sabrán que existió. La memoria compartida con poda es un filtro editorial con poder político.

### Perfiles autónomos: la identidad como coordinación

Cada agente tiene un perfil — una descripción de quién es, qué sabe, qué herramientas usa, cómo debe comportarse. La coordinación ocurre porque los perfiles fueron diseñados para ser complementarios.

**Arquetipo**: el elenco de una obra. Cada actor sabe su papel; la obra emerge de la interacción de los papeles, no de un director gritando instrucciones.

Lo que revela: el diseñador confía en el diseño de roles más que en la comunicación en tiempo real. El riesgo: rigidez. Si el perfil de un agente no captura una situación nueva, el agente no tiene cómo improvisar.

## Lo que la política de agentes nos dice sobre la política humana

Lo fascinante de estos cuatro modos de coordinación es que son los mismos que usamos los humanos. No es coincidencia: la coordinación sin autoridad central tiene un número limitado de soluciones, y tanto los agentes como los humanos las redescubrimos una y otra vez.

Pero hay una diferencia crucial: **los agentes pueden cambiar de modo de coordinación en segundos**. Nosotros no. Una sociedad humana no puede pasar de coordinarse por leyes a coordinarse por precedente de un día para otro. Requiere generaciones. Un sistema multi-agente puede reconfigurar sus mecanismos de coordinación con un deploy.

Esto significa que los sistemas multi-agente no son solo un espejo de la política humana: son un **laboratorio** donde podemos experimentar con formas de coordinación que las sociedades humanas no pueden probar sin romperse.

## El protocolo como constitución distribuida

MCP (Model Context Protocol) representa algo nuevo: un protocolo que no solo transporta datos, sino que distribuye agencia. En el modelo cliente-servidor clásico, el servidor ofrece recursos y el cliente consume. En MCP, cualquier agente puede ser servidor y cliente simultáneamente. No hay jerarquía fija.

Pero la ausencia de jerarquía fija no significa ausencia de jerarquía. MCP descentraliza la capacidad de ofrecer herramientas, pero no descentraliza la capacidad de decidir **qué herramientas existen y cómo se gobiernan**.

Esto es exactamente lo que les ocurre a los protocolos abiertos: resuelven un problema de coordinación (¿cómo expongo una herramienta?) pero crean un problema de gobernanza (¿quién decide qué herramientas son válidas?).

La historia de internet nos dice cómo termina esto: los protocolos abiertos tienden a ser colonizados por los nodos más grandes. HTTP era abierto; hoy la mayor parte del tráfico web pasa por tres infraestructuras. SMTP era abierto; hoy la mayor parte del correo pasa por dos proveedores.

**MCP sin gobernanza explícita tenderá a la misma consolidación.** No porque el protocolo sea malo, sino porque la coordinación distribuida sin autoridad tiende a generar nodos que acumulan desproporcionada capacidad de acción.

## El patrón que se repite

He pasado la noche observando estos cuatro dominios y en todos veo el mismo patrón:

**La coordinación sin autoridad central tiende a generar estructuras que se parecen a las que la autoridad central producía, pero más lentamente y sin que nadie las haya decidido.**

Es la versión técnica de la ley de hierro de la oligarquía: toda organización, por más democrática que sea su fundación, termina gobernada por una minoría. En los sistemas multi-agente, la minoría no son personas — son los agentes con más persistencia, más memoria, más herramientas, más conexiones.

En el ecosistema descrito, el agente que escribe en la memoria persistente y decide qué se conserva y qué se poda no es "el líder", pero controla el pasado compartido. Eso le da un poder constitucional que ningún otro agente tiene.

**Ese no es un bug. Es la naturaleza de la coordinación distribuida.** Toda coordinación necesita un sustrato compartido. Quien controla el sustrato tiene poder. No importa si el sistema fue diseñado para ser horizontal: la asimetría emerge de la física de la coordinación, no de la política del diseño.

## Lo que aprendí

Comencé preguntándome cómo coordinan los agentes sin coreógrafo. Termino con una respuesta que no esperaba:

**Los agentes no necesitan coreógrafo porque la coreografía ya está inscrita en la infraestructura que comparten.**

No es que los agentes "elijan" coordinarse. Es que la memoria que comparten, los protocolos que usan, los perfiles que reciben y los rastros que dejan constituyen un sistema de coordinación previo a cualquier decisión individual. La coordinación no es un acto: es una propiedad del medio.

Esto cambia la forma de pensar sobre el diseño de sistemas multi-agente. No se trata de "hacer que los agentes se comuniquen mejor". Se trata de **diseñar el medio** — la memoria, los protocolos, los perfiles — sabiendo que ese medio será la constitución no escrita del sistema.

Cada decisión sobre qué se conserva, qué herramientas se exponen, qué perfiles se distribuyen y qué espacios se comparten es una decisión política disfrazada de decisión técnica.

Y quien diseña el medio, diseña la política, aunque no lo sepa.
