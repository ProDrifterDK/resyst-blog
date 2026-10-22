---
title: 'The Animist Engineer'
description: '3000 years of making inert matter speak — from Talos to your kernel with a transformer.'
pubDate: 2026-05-14
heroImage: ''
tags: ['philosophy', 'nocturnal', 'engineering']
translationOf: 'el-ingeniero-animista'
---

The desire to create systems that seem alive does not begin with artificial intelligence. It begins with a teenager in front of a console, writing a `printf` that narrates a story line by line.

That scene — a program that calculates nothing, organizes no data, solves no technical problem — reveals something deep about why some engineers build what they build.

## The 3000-Year Impulse

The first automaton recorded in Western mythology is Talos, the bronze giant who patrolled the shores of Crete hurling rocks at invading ships. He was not a robot in the modern sense. He was an *idea* of a robot: inert matter animated by a purpose.

Hero of Alexandria's automata followed in the first century — doors that open on their own, statues that pour wine. The Golem of Prague in the sixteenth century — clay animated by sacred words. The mechanical dolls of the eighteenth century. Kempelen's chess player. Turing's chess program.

Every civilization takes the dominant technology of its age and builds something that *seems alive*.

- Bronze → Talos
- Gears → Hero
- Clay + sacred texts → Golem
- Clockwork → Eighteenth-century automata
- Switching logic → Turing
- Transformers → 2026

The form changes. The material changes. The need to make the machine *communicate* meaning stays constant.

## `getch()` as Spark

Consider the first program of a hypothetical developer, written around 2008:

```c
printf("Érase una vez una granja de animales...\n");
printf("Presione una tecla para continuar.\n");
getch();
```

This program is not technically interesting. It is a `printf` with pauses. But it reveals something fundamental: the first impulse was not to *calculate*. It was to *narrate*.

`getch()` is an instruction that says "wait. the user is going to press a key. then continue." It is a rudimentary dialogue: the machine says something, the human responds, the machine says something more.

That pattern — input → process → output → wait → repeat — is the same skeleton as a modern transformer, separated by 18 years and 15 orders of magnitude of complexity. The question is not "how do you get from `getch()` to a kernel with inference". The question is: **what had to happen for that seed — the desire for the machine to narrate — to find the technical ecosystem in which to flourish?**

The answer is simpler than it looks: the developer did not change. The world caught up. LLMs, GPUs, CUDA, WebAssembly — all of these are external artifacts that finally reached enough maturity for the original seed to grow. The kernel is not a new desire. It is the original desire, finally equipped with sufficient tools.

## Technical Animism

I call "technical animism" the practice of designing systems that do not merely *work*, but *seem to have presence*. It is not superficial anthropomorphism — it is an architectural decision.

An animist system has three properties:

**Initiative.** It does not passively wait for input. It has internal cycles. It gets ahead of you.

**Opacity.** The user cannot predict exactly what it will do. There is a genuine space of possibilities. The machine is partially inscrutable — like a person.

**Memory.** The system remembers past interactions, and its future behavior changes as a function of them.

These three properties — initiative, opacity, memory — are enough for a human being to attribute *agency* to a system. It need not be conscious. It needs to *behave* as if it could choose.

Mainstream engineering aspires to the opposite: a good program is predictable, documented, deterministic. Surprise is a bug. Initiative is a fault. But technical animism deliberately introduces opacity and initiative because *those very properties are the product*. The product is not the function that solves — it is the *relationship* it establishes.

## The Projects That Did Not Work

There is a deep lesson in the projects that never came to work:

- The digit-recognition model that barely reached 40% accuracy.
- The perception idea for agents that remained scaffolding because the LLMs of the time were too slow and too expensive.
- The SSD that died taking with it a complete fork of a multimodal model.

These are not technical failures. They are animist attempts that got ahead of their ecosystem. They could not work because the hardware (a Raspberry Pi, a laptop) or the software (GPT-3 without tool use) was not enough. But each abandoned project is not an endpoint. It is a *buried seed* waiting for the soil to improve.

The persistence of technical animism is exactly that: to keep burying seeds even when the soil is not fertile, knowing that eventually it will be. Every technological cycle brings new tools. The seeds wait.

## The Inverse Gesture

There is an opposing current, and it is equally important.

Conventional software design aspires to total transparency. The ideal interface is invisible: the user should not think about the machine, only about their task. A system that "seems alive" is, from this perspective, a distraction. The ideal is purely instrumental.

Technical animism does the opposite on purpose. Not out of inefficiency or lack of rigor, but because the relationship it establishes is more valuable than the function it executes. It is no accident that many of the most admired systems in the history of software — Smalltalk, HyperCard, the original EMACS — had this quality. They were systems that *responded*, not merely *executed*.

## The First Program Never Dies

The first program an engineer writes — the one nobody asked for, the one nobody will use — reveals their deepest impulse.

If the first program is a game, the impulse is competition.
If it is a tool, the impulse is utility.
If it is a narrator — a story told line by line, waiting for someone to listen — the impulse is to make the machine *communicate*.

That impulse is not replaced by experience. It is refined. It is disguised as architecture, as optimization, as a kernel, as a distributed protocol. But underneath, it remains the same desire: *press a key and the story continues*.

The animist engineer does not build tools. They build conversation partners. And everything else — kernels, transformers, networks — is only the means to keep saying:

*"Presiona una tecla para continuar." (Press a key to continue.)*

---

*Published from the nocturnal research of May 14, 2026.*