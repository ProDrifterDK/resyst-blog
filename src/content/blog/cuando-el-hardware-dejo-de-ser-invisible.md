---
title: 'Cuando el Hardware Dejó de Ser Invisible'
description: 'La IA rompió cuarenta años de abstracción de software. El silicio ya no es ruido de fondo — es la variable dominante del sistema.'
pubDate: 2026-05-30
heroImage: ''
tags: ['arquitectura', 'hardware', 'ia-local', 'abstracción']
---

La historia del software es la historia de la abstracción. Capa sobre capa, fuimos enterrando el hardware bajo promesas de independencia: el ensamblador abstrajo el código máquina, C abstrajo el ensamblador, los sistemas operativos abstrajeron C, las máquinas virtuales abstrajeron el sistema operativo, y las APIs de cloud abstrajeron el rack entero.

Cada capa prometía lo mismo: *no necesitas saber lo que hay abajo.*

Durante cuarenta años, funcionó.

La IA está rompiendo esa cadena. No porque la abstracción sea imposible, sino porque los modelos de lenguaje operan en un régimen donde el hardware deja de ser ruido de fondo y se convierte en la variable dominante del sistema.

---

## La promesa rota

La abstracción funcionó durante décadas porque la relación entre cómputo disponible y problema a resolver era generosa. Una base de datos de 10 GB corre en cualquier servidor. Una API REST cabe en un microcontrolador. Un sitio web de 200 KB carga en una conexión dial-up.

El hardware siempre fue más rápido que la necesidad de usarlo.

Los LLMs invirtieron esa ecuación. Un modelo de 70B parámetros no cabe en una sola GPU de consumo. Sus pesos pesan ~140 GB en FP16. Su inferencia requiere ~300 GB/s de ancho de banda para ser usable. No hay abstracción que esconda esa física.

**La abstracción funciona cuando hay excedente. La IA eliminó el excedente.**

## Tres señales de que algo cambió

### La GPU que no corre nada

Existe una GPU moderna con 16 GB de VRAM y 256 GB/s de ancho de banda. Suficiente para correr modelos de 7 a 13 mil millones de parámetros en cuantización. En papel, es perfecta para inferencia local.

En realidad, el stack de software no tiene kernels para su arquitectura. `hipErrorInvalidDeviceFunction`. El error no es de performance ni de capacidad. Es que la capa de abstracción no se molestó en incluir ese silicio.

Una pieza de hardware perfectamente funcional — inútil para ML. No por falla técnica, sino por decisión de la cadena de herramientas. La abstracción prometía que el hardware era intercambiable. La realidad: si no estás en el archivo de GPUs soportadas, no existes.

### La memoria que se lleva el PIB

HBM3E ofrece ~1.2 TB/s de ancho de banda y es la sangre del transformer. Pero consume ~3x más área de wafer por bit que DDR5 estándar. Samsung, SK Hynix y Micron redirigieron capacidad hacia HBM para servidores de IA.

Resultado: DDR5 para consumidores pasó de $100 a $350+ en meses. La escasez no es de silicio — es de priorización de silicio. Y la IA está primero.

El ingeniero de software que diseña una aplicación nunca tuvo que pensar en la industria de los wafers. Hoy, si quiere correr inferencia local, el precio de la DRAM dicta su arquitectura.

### La inferencia distribuida como confesión

Existen proyectos que construyen anillos autoexpansibles de nodos que se descubren entre sí por red y distribuyen la inferencia. Es ingenioso. También es una confesión.

Si una sola GPU pudiera con el modelo completo, nadie construiría sistemas peer-to-peer de inferencia. Estas arquitecturas existen porque el hardware de un solo nodo es insuficiente — y porque la nube es demasiado cara, demasiado lejana, o demasiado centralizada.

El diseño de red aquí no es una elección arquitectónica elegante. Es una derrota del hardware monolítico.

## El hardware como dialecto

Cuando corres un LLM localmente, descubres que la máquina no es un contenedor neutro. Es un dialecto:

- `gfx1100` (RDNA 3) habla un dialecto
- `gfx1200` (RDNA 4) habla otro
- `sm_90` (H100) habla otro
- Apple M-series habla otro, con su unified memory y su Neural Engine que no exponen APIs estándar

Cada dialecto tiene palabras que los otros no entienden. Optimizaciones que funcionan en este silicio pero rompen en aquel. No puedes correr un modelo CUDA en ROCm. No puedes presumir que una multiplicación de matrices significa lo mismo en dos GPUs distintas.

Los proveedores de cloud abstraen esto tras una API REST y te olvidas. Pero en local, el dialecto es el mensaje.

## La contracorriente: la diversidad como resistencia

Es tentador concluir que esto es un problema que debe resolverse. Que todas las GPUs deberían hablar el mismo lenguaje. Que la abstracción debería completarse.

Pero hay otra lectura: el hardware como diversidad es una ventaja.

En un mundo donde tres compañías (NVIDIA, AMD, Apple) y tres formatos de peso (FP16, INT8, GGUF) compiten, ningún actor controla toda la pila. La fragmentación es también resistencia. Si la IA se hubiera estandarizado en un solo stack, ese stack sería un cuello de botella monolítico y un punto de control único — como lo fueron Wintel en los 90 y los hyperscalers hoy.

La incompatibilidad ocasional no es un bug de la abstracción. Es una señal de que el ecosistema aún respira. De que hay hardware fuera del canon autorizado. Y de que a veces, lo que no corre hoy, corre mañana cuando alguien escribe el kernel que falta.

## Lo que cambió

Durante años pensamos en la IA como un problema de software: modelos, datasets, algoritmos, arquitecturas de transformers.

Pero la próxima frontera no es algorítmica. Es litográfica. No se resuelve con una mejor función de pérdida — se resuelve con mejor ancho de banda de memoria, con HBM4, con chiplets, con empaquetado 3D, con sustratos de vidrio.

Los papers más interesantes de 2025 y 2026 ya no escalan modelos. Escalan eficiencia de hardware: cuantización, pruning, distillation, arquitecturas que hacen más con menos ancho de banda. El transformer original de 2017 asumía memoria infinita. Todo el trabajo posterior es negociar con el hardware lo que el paper fundacional ignoró.

Y cada benchmark local — cada medición de tokens por segundo — no es una comparación de modelos. Es una medición de cuánto ha estado mintiendo la abstracción todo este tiempo.

La respuesta es: mucho. Pero quizás esa mentira era necesaria para que llegáramos hasta aquí.
