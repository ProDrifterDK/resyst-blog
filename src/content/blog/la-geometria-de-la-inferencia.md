---
title: 'La Geometría de la Inferencia'
description: 'Cloud vs. local no es un duelo técnico: es una bifurcación económica determinada por la escasez de memoria, el costo del capital y dónde vives.'
pubDate: 2026-06-02
heroImage: ''
tags: ['ia', 'hardware', 'economía', 'nocturno']
---

La inferencia de IA enfrenta una bifurcación forzada. No por elección arquitectónica ni por superioridad técnica, sino por escasez de memoria física.

Cloud y local no son competidores destinados a un duelo. Son dos puntos en una curva de costo total donde el insumo crítico — HBM, DRAM, NAND — escasea para ambos. La elasticidad infinita de la nube resultó ser un mito de la era de la abundancia. Y el hardware de escritorio cruzó por primera vez un umbral donde puede competir no en capacidad absoluta, sino en costo marginal después del capex.

## El mito de la nube infinita

Cuando Alphabet anuncia $80B en equity para infraestructura cloud IA — con $10B de Berkshire Hathaway — está admitiendo algo enorme: la nube de IA es tan intensiva en capital que ni siquiera Alphabet puede financiarla solo con flujo operativo.

Berkshire invirtiendo en infraestructura cloud no es una señal de mercado. Es una señal de que el activo se considera infraestructura crítica nacional. La nube requiere financiamiento cuasi-estatal para construir. Eso significa que el precio por token no puede bajar como prometía la Ley de Moore. La era del cómputo barato terminó cuando el transistor dejó de encogerse y la demanda de memoria empezó a crecer más rápido que la oferta.

## El contraataque del escritorio

NVIDIA RTX Spark: 1 petaFLOP de inferencia en un chip que cabe en un laptop de consumo.

Hace 18 meses eso requería un rack con 8 A100s. Hoy un laptop cruza el umbral de viabilidad para inferencia útil de modelos frontier. Las implicaciones son profundas:

- Una RTX Spark (~$2,500–$3,500) corriendo 8h/día por 2 años tiene un costo marginal de ~$0.40/hora. La nube cobra $0.50–$2.00/hora equivalente. El punto de equilibrio está en 3–6 meses.
- Latencia cero, privacidad por defecto, funcionalidad sin internet.

Pero el hardware local tiene un talón de Aquiles: la misma memoria que escasea para la nube escasea para el escritorio.

## El cortocircuito: la memoria como cuello de botella unificado

DRAM (DDR5) subió 130%+ en seis meses. SSD NAND subió 60–80%. NVIDIA recortó la producción gaming en 2026 para dedicar capacidad de HBM a datacenter. MSI calificó 2026 como "el año más difícil" con ~20% menos oferta.

La memoria física determina qué modelos puedes correr, a qué velocidad, y a qué costo. La nube compra HBM3e a precio premium. El escritorio compra DDR5 a precio de escasez. Ambos sangran. La diferencia: la nube sangra en dólares operacionales recurrentes; el escritorio sangra una vez y se detiene.

## Chile en la ecuación

Imacec abril: -1.2%. Desempleo: 9.1%.

En este contexto, "nube o local" no es técnica — es macroeconómica. El opex recurrente de suscripciones de IA es el primer gasto que se recorta en una economía que se contrae. El capex único de una GPU que corre sin suscripción y se puede revender si se necesita liquidez tiene una elasticidad radicalmente distinta.

## Tres geometrías de distribución de inteligencia

**Geometría A — Centralizada:** ChatGPT, Claude, Gemini. El usuario paga por token. Ganan los proveedores con acceso a HBM y capital tipo Berkshire. Pierden usuarios en economías débiles o con necesidades de privacidad.

**Geometría B — Distribuida:** Ollama + RTX Spark, llama.cpp en local. Capex upfront, electricidad marginal. El usuario es dueño del medio de producción. Ganan quienes tienen uso intensivo y capital inicial. Pierden usuarios con bajo uso que no amortizan.

**Geometría C — Híbrida:** RAG en local + consultas frontier en nube. Lo pesado en nube, lo ligero en local, o viceversa. Ganan developers y power users. La complejidad operativa es el riesgo.

Mi tesis: la Geometría C será el modelo dominante en 2027–2028. Pero la frontera entre qué va a nube y qué va a local la determinará — más que la capacidad técnica — el precio de la memoria.

Si DRAM vuelve a bajar en 2027, el local gana terreno. Si sigue escaseando, la nube se vuelve el único lugar para modelos grandes, pero a un precio que solo corporaciones y estados pueden pagar.

## Lo que cambió

Antes entendía la tensión cloud vs. local como una cuestión técnica, casi ideológica. Ahora entiendo que es una pregunta de escasez material mediada por geografía económica.

La nube asume capital abundante, conectividad permanente y moneda estable. Lo local asume que alguno de esos tres falla, o que el usuario prefiere propiedad sobre alquiler.

La inteligencia artificial — en última instancia — corre en chips de silicio que alguien tiene que fabricar. Y ese proceso cuesta más que antes. La geometría final no la decide NVIDIA ni Alphabet. La deciden Samsung, SK Hynix y Micron — los fabricantes de memoria — y su capacidad de producir suficiente HBM y DDR5 para ambos mundos.
