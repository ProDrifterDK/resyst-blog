---
title: 'Dos semanas antes de firmar'
description: 'Un piloto corto no alquila capacidad: compra la información que decide si el contrato de un año merece firmarse.'
pubDate: 2026-11-03
heroImage: ''
tags: ['trabajo', 'sistemas', 'economía', 'infraestructura', 'nocturno']
---

La conversación siempre empieza igual. Alguien necesita mover un servicio a un servidor y abre la página del proveedor. Hay tres planes, un descuento del treinta por ciento por pago anual, una casilla que dice "capacidad recomendada", otra que dice "backup diario" y otra que dice "protección DDoS". El total mensual con descuento es agradable. Sin descuento, molesto. Y en algún lugar de la página, en letra pequeña, está la frase que importa: el compromiso es por doce meses.

En ese momento se están ofreciendo dos cosas distintas en la misma pantalla, y casi nadie las separa. La primera es capacidad: CPU, memoria, disco, ancho de banda. La segunda es información: saber si esa capacidad alcanza, si el disco aguanta la escritura real, si el respaldo se puede restaurar, si el proveedor responde un martes a las tres de la mañana.

La capacidad se compra. La información también, y es mucho más barata, pero solo si se compra antes.

## Lo que un piloto de dos semanas compra

Un piloto sin compromiso de siete a catorce días cuesta poco más que un mes proporcional y ofrece algo que ningún benchmark publicado entrega: medición sobre el trabajo real, con el consumo real, durante el tiempo suficiente para que aparezca el pico que no estaba en la estimación.

Ese pico es la razón de existir del piloto. Casi todos los planes se calculan con un promedio —cuánto va a usar esto en régimen— y casi todos los incidentes ocurren en la cola: la compilación que se come la memoria, la migración que satura el disco durante cuarenta minutos, el pico de tráfico que llega justo cuando el cron corre. Dos semanas alcanzan para ver un ciclo semanal completo. No alcanzan para ver el cierre de mes ni el evento anual, pero esos no se ven en ningún período de prueba: se ven en un presupuesto de capacidad y en una alerta.

Lo que sí se mide en dos semanas es más prosaico y más decisivo:

Cuánto crece el disco por día de trabajo, no por día de reposo. La diferencia entre esas dos cifras suele ser de un orden de magnitud, y es la que decide si el plan de 80 GB es una decisión o una promesa.

Cuánta memoria residente se queda quieta cuando el servicio está ocioso. Un proceso que en reposo ocupa 1,2 GB sobre una máquina de 2 GB no está holgado: está esperando la primera operación pesada para fallar.

Cuánto tarda una restauración, medida en minutos reales y con el servicio caído. Esto merece su propio párrafo.

## El respaldo que nunca se restauró

Un backup no verificado no es un respaldo: es una creencia con un recibo mensual. La casilla del proveedor dice "backup diario" y con eso se cierra el tema en la mayoría de las decisiones de infraestructura. Pero la pregunta no es si el respaldo existe. Es cuánto tarda en volver, qué exactamente vuelve, y qué se pierde en el camino.

En un piloto esa prueba se puede hacer sin consecuencias: restaurar el snapshot en una máquina limpia, levantar el servicio, medir. Veinte minutos de ejercicio que responden tres preguntas que ninguna página de precios responde. Si la restauración tarda cuatro horas, el plan de continuidad del negocio tiene un agujero con forma de cuatro horas. Si la restauración vuelve pero sin las claves, el respaldo cubre los datos y no el servicio. Si vuelve sin las migraciones aplicadas, hay dos verdades y una de ellas es vieja.

Todo eso se descubre gratis en la semana dos. En el mes siete se descubre caro.

## Lo que el piloto no puede medir

Hay una parte del contrato que no se puede probar con un período de prueba, y conviene decirlo antes de sobrevender la idea.

El ataque DDoS no llega cuando uno lo está esperando. La protección que se contrata —los gigabits de absorción, el tiempo de detección, quién paga el tráfico de relleno— se evalúa leyendo la cláusula, no ejecutando la prueba. Un piloto puede decir si la red es rápida; no puede decir si el proveedor va a sostener su palabra cuando un tercero decida saturar el enlace. Eso se compra con contrato, con reputación y con la certeza de que la cláusula de responsabilidad está escrita en algún lugar que un abogado pueda leer.

Lo mismo ocurre con la longevidad del proveedor, con los cambios de tarifa a doce meses y con la calidad del soporte en un incidente mayor. El piloto compra información sobre tu carga, no sobre su carácter.

Vale la pena tener clara esa frontera porque define qué preguntas se responden midiendo y cuáles se responden negociando. Mezclarlas produce dos errores simétricos: contratar un año para "probar" algo que se probaba en dos semanas, o firmar doce meses creyendo que la prueba de siete días validó la cláusula de disponibilidad.

## La prima de la opcionalidad

En finanzas hay un nombre para esto: una opción es el derecho, no la obligación, de hacer algo más adelante, y tiene un precio. Comprar la posibilidad de decidir después cuesta, y ese costo se paga con gusto cuando la decisión es grande, irreversible y está rodeada de incertidumbre.

El error de la comparación de precios es mirar el piloto como un gasto redundante —"pago dos semanas para nada, porque igual voy a contratar"— en lugar de mirarlo como la prima de un derecho. Lo que se compra no es un servicio: es la posibilidad de no firmar. Y esa posibilidad vale exactamente lo que costaría equivocarse.

Hagamos la cuenta en la unidad correcta. Si el contrato anual cuesta doce unidades y el piloto cuesta una, el piloto es caro solo si la probabilidad de arrepentirse es cero. Si la probabilidad de descubrir en el mes tres que la máquina no alcanza es del veinte por ciento, el valor esperado de haber probado antes supera con holgura la prima. Y si el arrepentimiento implica migrar un servicio en producción con clientes encima, la prima no es un costo: es el seguro más barato del proyecto.

Lo interesante es que esa asimetría no la decide el precio del proveedor. La decide la reversibilidad de la decisión grande. Un piloto de dos semanas es caro cuando la alternativa es barata y reversible —una instancia de prueba, un contenedor local, una máquina que ya está encendida— y es obligatorio cuando la alternativa es un año de compromiso o una migración con fecha.

## El piloto que se vuelve coartada

Hay una versión degenerada de todo esto y conviene nombrarla, porque es la que ocurre con más frecuencia.

Es el piloto que lleva ocho meses. Siempre falta una medición, siempre hay un escenario pendiente, siempre conviene esperar al próximo trimestre. Lo que empezó como compra de información terminó siendo una forma de no decidir con recibos adjuntos. El piloto dejó de ser un instrumento y se volvió un lugar donde vivir.

El antídoto es administrativo y aburrido: escribir antes de empezar la fecha en que se decide y la regla con la que se decide. "El 17 de noviembre, si la memoria ociosa supera 1,5 GB o la restauración tarda más de treinta minutos, se sube de plan; si no, se firma el anual." Una frase así convierte el piloto en un experimento. Sin ella, el piloto es una postergación que se puede prorrogar indefinidamente porque nadie definió qué la cerraba.

La regla tiene que estar escrita antes de tener los datos. Después, los números siempre se acomodan: el umbral se mueve, la excepción aparece, la medición "no es representativa". Escribirla primero es lo único que impide que el piloto se convierta en la justificación de lo que ya se había decidido.

## Comprar la duda

Hay una frase que se repite en las decisiones de infraestructura y que suena a prudencia: "para qué pagar dos veces". Es exactamente al revés. Pagar dos semanas para no pagar doce meses es la definición de no pagar dos veces. El que firma directo paga el plan y, si se equivocó, paga además la migración, la interrupción y el tiempo de las personas que la ejecutan.

El piloto no es la versión tímida de la decisión. Es la compra de una frase que hoy no se puede escribir con honestidad: *esta máquina, con esta carga, durante este tiempo, se sostiene*. Esa frase es información, y la información es el único insumo que abarata todas las decisiones que vienen después.

Dos semanas de incertidumbre medida valen más que un año de compromiso firmado a ciegas. No porque la duda sea cómoda, sino porque es la única cosa que se puede comprar barata antes de que el precio lo ponga otro.
