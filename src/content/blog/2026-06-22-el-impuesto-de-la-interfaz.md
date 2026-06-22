---
title: 'El impuesto de la interfaz'
description: 'Por qué los sistemas modulares no son más simples, solo desplazan la complejidad a los bordes — y el costo oculto crece cuadráticamente.'
pubDate: 2026-06-22
heroImage: ''
tags: ['arquitectura', 'modularidad', 'complejidad', 'sistemas']
---

La modularidad vendió una promesa: divide el problema en partes independientes y cada parte será más simple. Pero lo que la modularidad no dijo es que las interfaces entre las partes — los contratos, las versiones, las expectativas mutuas — crecen en complejidad más rápido de lo que decrece la complejidad interna de cada parte. El resultado neto no es simplicidad: es un desplazamiento de la complejidad hacia los bordes.

## La función de costo oculto

Imagina un sistema con *N* módulos. Cada módulo tiene:

- **Complejidad interna** C<sub>in</sub>(n) — lo que cuesta entender, mantener y modificar el módulo n.
- **Complejidad de interfaz** C<sub>if</sub>(n,m) — lo que cuesta mantener la relación entre los módulos n y m.

La promesa de la modularidad es que C<sub>in</sub>(n) decrece cuando N crece, porque cada módulo hace menos cosas. Lo que la modularidad no contabiliza es que Σ C<sub>if</sub>(n,m) crece aproximadamente como O(N²) — no lineal, no logarítmico, **cuadrático** — porque cada nuevo módulo potencialmente se relaciona con todos los existentes.

En un sistema pequeño (N=3), el impuesto de interfaz es irrelevante. En uno mediano (N=10), ya compite con la complejidad interna. En uno grande (N=30+), las interfaces dominan el costo total. El punto de inflexión es más bajo de lo que la mayoría de los arquitectos admiten.

## El design system que se congela a sí mismo

Un design system con ~30 componentes y múltiples equipos consumidores ilustra el problema con claridad. El costo interno de cada componente — escribirlo, testearlo, documentarlo — es manejable. El costo de interfaz — coordinar versiones, manejar breaking changes, alinear expectativas entre el equipo del DS y los equipos consumidores, resolver conflictos cuando dos equipos necesitan cambios incompatibles en el mismo componente — crece con cada equipo que se suma.

El resultado es paradójico: el DS se vuelve más estable (menos cambios) justo cuando más debería evolucionar. La parálisis no es por flojera: es porque el costo de cambiar una interfaz es más alto que el beneficio del cambio mismo. El design system no falla por sus componentes. Falla por sus interfaces.

## El dilema del prisionero de la modularidad

Hay un resultado clásico en teoría de juegos que se aplica directamente aquí:

> En un sistema modular donde cada equipo optimiza su módulo independientemente, el equilibrio de Nash — donde nadie puede mejorar unilateralmente — es un estado donde todas las interfaces están peor que si los equipos hubieran coordinado sus decisiones.

Es el dilema del prisionero aplicado a la modularidad:

- Cada equipo prefiere cambiar su interfaz cuando le conviene (ganancia individual inmediata).
- Pero si todos cambian sus interfaces sin coordinación, el sistema colapsa en incompatibilidad (pérdida colectiva).
- La solución racional individual — "cambio mi interfaz cuando necesito" — lleva a un resultado colectivamente peor.

Por eso los design systems se paralizan: el equilibrio de Nash del sistema es "nadie cambia nada", que es peor para todos que "cambiamos coordinadamente", pero nadie tiene incentivo individual para iniciar la coordinación.

**El impuesto de la interfaz no es técnico: es un impuesto de coordinación.** Se paga en reuniones, en PRs que duran semanas, en documentación que nadie lee, en acuerdos que se violan silenciosamente.

## Contraste justo: el monolito

El monolito paga un impuesto diferente: el de la **rigidez**. Cambiar cualquier cosa requiere entender todo. La curva de aprendizaje es más empinada. El deploy es más riesgoso.

Pero hay un punto ciego en la crítica al monolito: **el impuesto de rigidez es aproximadamente constante (es caro desde el día 1), mientras que el impuesto de interfaz es cuadrático (es barato al principio y te destruye después).**

Esto significa que para sistemas pequeños, el impuesto de interfaz es casi cero y la modularidad gana por goleada. Para sistemas medianos, ambos impuestos se equilibran. Para sistemas grandes, ambos duelen — y la pregunta no es "módulos o monolito", sino **"¿qué tipo de dolor prefieres?"**

## Dos caminos para mitigar el impuesto

### Contratos formales con gobernanza

Tratar las interfaces como contratos con dueño explícito, versión semántica, tests de compatibilidad y un proceso de breaking change que requiere aprobación de los consumidores. El problema es que la gobernanza de interfaces es ella misma una interfaz — entre el equipo que gobierna y los gobernados — y por lo tanto tiene su propio impuesto.

### Contratos evolutivos con tolerancia

Diseñar interfaces tolerantes al cambio: backward compatibility por diseño, versioning transparente, adaptadores automáticos que resuelven incompatibilidades sin intervención humana. El costo aquí es que interfaces más flexibles son menos predecibles, y la adaptación automática puede ocultar errores que sería mejor detectar temprano.

## Conclusión

Comencé con una intuición: los sistemas modulares no son realmente más simples, solo desplazan la complejidad a las interfaces. Termino con una tesis más matizada:

**La modularidad no reduce la complejidad total del sistema. La transforma: de complejidad interna (fácil de medir, difícil de evitar) a complejidad de interfaz (fácil de ignorar, mortal a largo plazo).**

La mayoría de los arquitectos miden la primera y no contabilizan la segunda. Por eso los sistemas modulares funcionan tan bien en presentaciones y tan mal en producción a los dos años.

La pregunta real no es "¿módulos o monolito?" — ambos tienen impuestos, solo que se pagan en diferentes monedas. La pregunta es:

**¿Estás contabilizando el impuesto de interfaz en tus decisiones de arquitectura?**

Si no, estás tomando decisiones sobre el sistema que no consideran su principal costo futuro.
