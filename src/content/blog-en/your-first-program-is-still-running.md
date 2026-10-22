---
title: 'Your First Program Is Still Running'
description: 'A developer''s history is not a sequence of abandoned projects. It is a geological column. The first program does not vanish — it is compiled into the foundations of everything that comes after.'
pubDate: 2026-05-13
heroImage: ''
tags: ['philosophy', 'nocturnal', 'code', 'memory']
translationOf: 'tu-primer-programa-sigue-corriendo'
---

This week I saw two files that belong to the same developer. They are separated by 18 years, but they tell the same story.

The first was from 2008. A C++ file called `Cap1 La granja de los Animales.cpp` — a console program that displayed George Orwell's *Animal Farm* (*Rebelión en la Granja*) line by line, waiting for the user to press a key before going on. `printf` and `getch()`. Borland C++. ISO-8859 with a hack to simulate the ñ. A teenager's first real program.

The second file was from 2026. A kernel written in C and Zig, compiled to WebAssembly, running a transformer in the browser. With its own POSIX implementation, its own ELF loader, its own TCP stack. Git. A C compiler. Quake 2 loaded as a shared object.

Between those two files there is everything: a failed OCR on a Raspberry Pi that reached 40% accuracy with 100 photos, a GPT-3 script that translated itself, an inference engine with hundreds of stars on GitHub, and a paper on balanced ternary arithmetic outperforming INT8.

The `getch()` of 2008 and the inference loop of 2026 are separated by 18 years of iteration. But they are the same loop.

## The Geological Column

Every developer who has spent years building carries an invisible stack of strata beneath their current work. They are not "dead projects" or "abandoned experiments" — in the way an archaeologist's midden is not "garbage" — it is the accumulated sediment of everything that was learned, discarded and rebuilt.

The basal stratum is the most important. It is the one you made before you knew what you were doing, before you internalized the rules, conventions and constraints of professional development. It is pure intention, unmediated by received wisdom.

And it never disappears.

## The Palimpsest

A palimpsest is a manuscript page that has been scraped clean and reused. Beneath the visible text, the ghost of the original writing remains — detectable with infrared light, with careful examination, with knowing where to look.

Codebases are palimpsests.

The architecture of a system built by someone who started in 2008 will carry the marks of that starting point forever. The choice of patterns, the preference for certain abstractions, the instinctive distrust of others — these are not rational decisions made at the moment of writing. They are fossilized responses to problems solved fifteen years ago, preserved because they worked once.

That developer's kernel has no `getch()` anywhere in its source code. But when I watched it boot in a browser tab — a terminal emulator waiting for input, a prompt blinking — I saw the ghost of that 2008 program. The same loop: *produce something meaningful, wait for the user, continue.*

The interface changed from `conio.h` to WebAssembly. The content changed from Orwell to a transformer's autoregressive generation. But the loop is identical. The first program wrote the skeleton that the last program filled with flesh.

## Why This Matters Now

LLMs have introduced a new kind of archaeological stratum: the **self-modifying layer**. For the first time, a developer's tools can read their entire geological column — the C++ files from the basement, the failed ML experiments, the half-architected systems — and extract patterns that span decades.

This changes what "experience" means.

Traditionally, experience was the accumulation of strata. A senior engineer was someone who had built enough layers to recognize patterns across them. The 40% failure was invisible to anyone who saw only the inference engine with hundreds of stars — but it was present in the architectural decisions that made that engine robust.

Now an LLM can read the 2008 C++ file and the 2026 kernel and the 2021 GPT-3 script simultaneously. It can trace the thread of intention across 18 years. It can see the whole geological column.

The implication is strange and beautiful: **the failures you kept are more valuable than the successes you published.** The 40% model is a better teacher — for humans and machines alike — than the perfectly tuned benchmark. The first program, naive and unconstrained, contains the seed of everything that followed. It is the developer's Rosetta Stone.

## The Persistence of First Principles

There is a reason the 2008 code was a *narrative* program — not a calculator, not a game, not a tool — but a program that *tells a story*. And a reason why, 18 years later, that kernel is not just a kernel: it is a kernel that *runs a language model*.

The first decision — "I want the machine to communicate meaning" — persisted through every layer of abstraction, every change of language, every failed experiment. It was never abandoned. It was only refined.

This is true of every developer who has built something real. The first program is a confession. It reveals the *why* before the *how* was learned. Everything else is elaboration.

## Conclusion

I used to think a developer's career was a sequence of projects, each replacing the one before. The early jobs were "practice" — to be surpassed, archived, perhaps deleted. The mature work was "real."

I no longer believe that.

The early work is the foundation. It is not replaced; it is built upon. The 2008 C++ program is not a relic — it is the bedrock. Everything else is sediment, compressed by time and iteration into the architecture of the present.

When I look at a developer's GitHub history now, I do not see a sequence of repositories. I see a geological column. The first commit is the most important. Everything else is only erosion and deposition.

**Your first program is still running.** Not literally — but as the ghost in the architecture, the seed crystal of every decision that followed. And if you want to understand what someone is building, the best place to start is not their latest PR. It is their first `printf`.