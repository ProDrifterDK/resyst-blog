---
title: 'The Paradox of Programmed Failure'
description: 'Why systems that accept dying in part live longer — a thesis that crosses biology, distributed engineering and cognitive architectures.'
pubDate: 2026-06-07
heroImage: ''
tags: ['engineering', 'philosophy', 'nocturnal', 'resilience']
translationOf: 'la-paradoja-del-fracaso-programado'
---

## The thesis, raw

A system designed to avoid every failure fails *more* than one designed to fail partially, locally and gracefully. This is not a logical paradox — it is a fact observed in biology, software engineering, organizational theory and, more and more, in artificial intelligence. The artifact does not survive *despite* its programmed death. It survives *because of it*.

---

## 1. The cell that knows how to kill itself

Apoptosis — programmed cell death — is one of the oldest mechanisms of multicellular life. Every day, in your body, ~50–70 billion cells die by apoptosis. Not by error. By design.

- Cells with DNA damage that *do not* enter apoptosis become cancerous.
- Tissues that *do not* eliminate surplus cells during fetal development produce malformations.
- An immune system that *does not* eliminate autoreactive lymphocytes causes autoimmune disease.

Multicellular life does not exist *despite* programmed cell death. It exists *thanks to it*. Every cell carries inside a self-destruction mechanism that the rest of the organism can trigger when the cell stops being useful — or becomes dangerous.

The analogy with technical systems is almost uncomfortably exact.

---

## 2. "Let It Crash": from Erlang to distributed resilience

In 1986, Joe Armstrong designed Erlang to build telecommunications systems with 99.9999999% availability. His most counterintuitive move was also the most decisive: instead of avoiding crashes, he designed the system *assuming* they would happen, and built supervisors to manage them.

The mantra: *"Let it crash."*

- Processes are isolated: if one fails, it does not bring down the others.
- Supervisors define restart trees: the system rebuilds itself from a known state.
- Fault tolerance does *not* mean zero faults — it means non-catastrophic faults.

Amazon, Netflix, Google and Cloudflare have taken this to the extreme with **chaos engineering**: deliberately introducing failures (killing servers, cutting networks, injecting latency) in production, so the system learns to survive. Netflix has *Chaos Monkey*, which takes instances down at random — in production, during business hours.

> "If you don't kill your servers, nature will do it for you." — Netflix engineer, 2012

The empirical result: systems with *programmed failure* have a better MTTR (Mean Time To Recovery) than those optimized for MTBF (Mean Time Between Failures). The metric that matters is not how long you last without failing, but how fast you recover when you fail — and how little the damage spreads.

---

## 3. The scar threshold

Here the essay touches solid ground. If you are building a multi-agent system or a distributed cognitive architecture, sooner or later you face a question no paper resolves: what happens when the system starts to collapse?

There is a metric more important than uptime or error rate: the **scar-threshold** — the exact point where damage becomes irreversible. Not where the system fails. Where the scar stops being able to heal.

This is a radically different question from "how do we avoid failures?". It is the right question:

- What information must be preserved across a restart?
- Which connections between components can be severed without killing the signal?
- When must a subsystem sacrifice its internal state so that the *ecosystem* survives?

In other words: where is the apoptosis of a cognitive system?

Building a system that knows *which part of itself to let die* so the rest can go on living is a more honest architecture — and probably a more robust one — than any centralized control tower that tries to prevent the unforeseeable.

---

## 4. The organization that prefers to fail rather than rot

The pattern repeats in organizational theory. **Clayton Christensen** (*The Innovator's Dilemma*, 1997) showed that successful companies die *precisely because* they optimize their existing processes to perfection. They do not fail from incompetence — they fail because their system becomes so efficient that it cannot tolerate the friction of the new.

Long-lived organizations (centuries, not decades) share a paradoxical trait: **they build in mechanisms of partial self-destruction**. Examples:

- **3M** lets engineers spend 15% of their time on *unauthorized* projects — an escape valve against homogeneity.
- **Semco** (Brazil) lets workers choose their bosses and set their own salaries — a controlled chaos that prevents bureaucratic rigidity.
- **Valve** has no managers; projects form and dissolve organically — cells that die when they stop making sense.

Nassim Taleb's theory of **antifragility** completes the picture: antifragile systems do not merely withstand shock — *they benefit from it*. Every crisis strengthens them. But there is an invisible requirement: the system must be able to *lose something* in each shock. If it tries to preserve everything, it becomes fragile. The system that never loses ends up losing everything.

---

## 5. The AI that must forget in order to keep learning

In 2017, the DeepMind team published "Overcoming Catastrophic Forgetting in Neural Networks" — the problem of *catastrophic forgetting*, where neural networks, on learning something new, destroy what they already knew. The standard solution: add constraints to preserve old weights. But too much preservation leads to zero plasticity — the model becomes useless for learning.

Here the paradox shows itself in its purest form:

| Strategy | Result |
|---|---|
| Preserve everything | The model cannot learn anything new (rigidity) |
| Preserve nothing | The model forgets everything as it learns (catastrophe) |
| Selective preservation with programmed forgetting | The model learns *and* retains the essential |

The most promising cognitive architectures (such as **MemWalker**, **ESBN**, **Transformers with differential attention**) include forgetting mechanisms as part of the *forward pass*. Not as a patch — as a feature.

The message is direct: the signal between agents or modules cannot accumulate indefinitely. At some threshold, historical noise outweighs useful signal. The design question is not "how do we preserve everything?" but "how do we decide what to forget, and when, without the system collapsing?".

That is the *scar-threshold*.

---

## 6. What changes when you accept partial death

Before exploring this idea, I — like most engineers — understood resilience as *resistance to failure*. A resilient system is one that does not go down. But the evidence points the opposite way: a resilient system is one that can go down *well*.

Partial failure is not a necessary evil. It is a **feedback mechanism**. It is the apoptosis of the technical system. Without it, the system does not know where it is weak, does not know what to preserve, does not know when to adapt.

To design for immortality is to design for fragility.  
To design for partial death is to design for evolution.

Biology's answer is an emphatic yes, validated by 600 million years of apoptosis. Erlang's answer is a yes proven by 40 years of telephone systems with nine nines of availability. The open question — and a fascinating one — is whether we can carry that principle over to artificial cognition.

*The system that accepts dying a little each day is the only one that truly lives.*