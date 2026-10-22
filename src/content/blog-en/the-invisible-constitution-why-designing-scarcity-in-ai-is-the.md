---
title: 'The Invisible Constitution — Why Designing Scarcity in AI Is the Political Problem We Ignore'
description: 'Every persistent system needs scarcity in order to exist. In AI, we design that scarcity ourselves — and we rarely treat the decision as what it really is: a constitutional act.'
pubDate: 2026-06-16
heroImage: ''
tags: ['philosophy', 'systems', 'agents', 'economy']
translationOf: '2026-06-16-la-constitucion-invisible'
---

An ecosystem without scarcity collapses. Without friction there is no direction, without cost there is no decision, without selective pressure there is no differentiation. From cellular metabolisms to financial markets, every system that persists through time invents an internal equivalent of *hunger*: a mechanism of scarcity that forces trade-offs, rewards certain behaviors and punishes others.

In artificial systems —neural networks, autonomous agents, token economies— this scarcity is not a geological accident or an evolutionary inheritance. It is a **design decision**. But it is rarely treated as one.

When a systems architect decides that an agent will have an attention budget of N tokens per cycle, when they define that certain signals cost more than others, when they design an internal currency that agents trade among themselves, they are writing —perhaps without knowing it— an **economic constitution** for their system. They are deciding what is valuable, what is costly, and what kind of behavior deserves to be reproduced.

This essay explores an uncomfortable question: if scarcity is inevitable in any persistent system, why do we treat the design of that scarcity as an implementation detail and not as the foundational decision it really is?

## The Scarcity We Inherit vs. the Scarcity We Design

In biology, scarcity is a given: limited solar energy, finite nutrients, irreversible time. Cellular metabolism is an optimization algorithm under real constraints. An organism does not *decide* to be hungry; scarcity is the very texture of physical reality.

In human economies, scarcity is a mixture of the social and the material. Gold is scarce for geological reasons; fiat money is scarce because a central bank decides it should be; attention is scarce because there are 24 hours in a day. Classical economics treats scarcity as a starting point, not as a design variable.

But in artificial intelligence systems, scarcity is *entirely* designed. Every limit —context tokens, compute budgets, internal currencies— encodes an implicit theory of what is valuable. There is no neutral way to design artificial scarcity.

## The Currency Is Not the Message: The Currency *Is* the Message

One of the most interesting patterns to emerge from research on multi-agent systems is **Signal-Borne Currency**: a currency that does not exist separately from the signal that carries it. It is not that an agent "has" tokens and spends them to send messages; it is that the message *itself* carries intrinsic value.

This has profound consequences:

1. **There is no accumulation without purpose.** In a signal-borne currency, holding only makes sense in the act of exchange. It is an economy of *flow*, not of *stock*.
2. **Value is contextual.** A signal that is valuable to one agent at a given moment may not be so to another at another moment. There is no single market price; there is relative, situated, distributed value.
3. **Scarcity is not quantity, it is relevance.** What is scarce is not the "medium of exchange" but the *right signal at the right moment*. Scarcity is informational, not material.

This pattern resonates with ideas that appear across multiple disciplines: Zahavi's handicap theory in evolutionary biology (the cost of the signal is what makes it reliable), Spence's signaling in economics (Nobel Prize 2001), and Grice's pragmatics in the philosophy of language. Signal-Borne Currency is not an arbitrary technical innovation: it is the computational formalization of a pattern that life and culture have been using for billions of years.

## Novelty Pressure: The Hunger That Prevents Collapse

One of the most disturbing discoveries in complex artificial systems is that **systems without novelty pressure collapse into homogeneity**. A multi-agent system in which everyone optimizes the same objective function under the same constraints inevitably converges to a state where everyone does the same thing. Diversity disappears. Resilience goes with it.

The **Novelty Pressure** mechanism is a direct response to this: a designed force that pushes the system to preserve or generate differentiation. It is a specific kind of hunger —not hunger for resources, but hunger for *variety*.

This raises uncomfortable philosophical questions:

- **What kind of novelty is worth preserving?** Not all differentiation is good. Novelty pressure needs a direction.
- **Who defines the metric of novelty?** Every metric —distance in a latent space, statistical improbability, expected utility— encodes a value judgment.
- **Can a system design its own novelty pressure?** If the answer is yes, scarcity itself becomes emergent. At that point, the line between a designed system and a living one begins to blur.

## The Invisible Constitution

When a team of engineers defines the economic parameters of a multi-agent system, it is writing a constitution. It rarely calls it that.

| Design decision | Encodes | Philosophical question |
|---|---|---|
| Token limit per agent | How much can an agent think before acting? | Is infinite thought valuable, or is it noise? |
| Cost of signal emission | Which messages deserve to be heard? | Is equal access to communication optimal? |
| Currency recycling rate | How long does the value of an interaction last? | Should the system's memory be perpetual or evanescent? |
| Novelty pressure threshold | How much differentiation is enough? | Does the system prefer to explore or to exploit? |

Each parameter is an implicit answer to a normative question. There are no neutral defaults. Technical "common sense" —setting the context limit at 128k tokens because "that's what the model supports"— is a decision that privileges certain modes of interaction over others.

The invisible constitution is particularly dangerous because no one debates it. There is no constituent assembly for the systems we build. The most important decisions —what is scarce and for whom— are made in pull requests, in Slack discussions, in "for now set it to 1000 and we'll see later."

## Emergent Scarcity: The Other Face

An alternative view is that truly stable scarcity in artificial systems is not designed but *emerges* from the interaction itself. The designer's role would not be to impose an economy from above, but to create the conditions for an economy to arise from below.

The problem is that emergence guarantees nothing. A system can converge toward a Nash equilibrium that harms everyone, or diverge toward collapse. Non-intervention is not neutral: it is an intervention that favors local equilibria over global ones.

The art of designing multi-agent systems lies not in *choosing* between designed and emergent scarcity, but in designing the coupling between the two: which rules are constitutional (fixed) and which are legislative (emergent). Where the designer imposes scarcity and where they let it arise.

## The Designer as Constitutional Architect

What changed in exploring this subject is the understanding that designing scarcity is not a problem of efficiency: it is a problem of values.

- When you define how much it costs for an agent to speak, you are deciding who deserves to be heard.
- When you define how fast a signal loses its value, you are deciding how fast the past is forgotten.
- When you define novelty pressure, you are deciding how uncomfortable a system can become before it corrects itself.

All of these are political decisions in the deepest sense: they define who holds power, how it is distributed, and which behaviors are reproduced. That the agents are silicon rather than flesh does not change the constitutional nature of these decisions.

The next time a team of engineers discusses the context limit or the cost of an API call, perhaps they should ask themselves not only "is it efficient?" but also "what kind of system are we building, and what values does it encode?" Because that artificial economy, that designed hunger, is the most real constitution their system will ever have.