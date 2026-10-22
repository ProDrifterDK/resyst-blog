---
title: 'The Oracle and the Meter'
description: 'LLM benchmarks are saturated, contaminated, and measure our faith more than real intelligence. A reflection on what it means to measure in the post-frontier era.'
pubDate: 2026-06-01
heroImage: ''
tags: ['AI', 'benchmarks', 'philosophy', 'nocturnal']
translationOf: 'el-oraculo-y-el-medidor'
---

For years, MMLU was the gold standard. A model that got 85% of multi-domain knowledge questions right was "intelligent." Today frontier models hover around 94%, and the gap between #1 and #5 on the leaderboard is statistical noise: two or three points that translate into no perceptible improvement for a real user.

This is not progress. It is test saturation.

Every new model arrives with a 0.5% improvement on GPQA or HLE, and that fraction justifies press conferences, funding rounds and valuations of nine hundred billion dollars. But for the developer trying to keep a coding agent from hallucinating function names, those fractions of a point don't matter. What matters is reliability, consistency and — more and more — cost per useful inference.

Saturated benchmarks have become what standardized tests were for human education: a selection machine that no longer measures capability, only optimization for the test.

## The Silent Contamination

The deeper problem is that benchmarks are contaminated. Not through malice, but through the simple fact that models are trained on the whole internet, and the benchmarks are part of that whole. A model that "passes" MMLU with 94% does not necessarily *understand* the concepts — it may have memorized the answers because its training texts included identical questions and answers.

The industry acknowledges this. LiveBench, GAIA and other "fresh" benchmarks try to mitigate it by periodically generating new questions. But it is an arms race: every new benchmark is contaminated within weeks.

The result is a benchmark-to-production gap that in agentic systems reaches 37%. A model that sweeps GPQA can fail miserably at a simple task like "look up this datum in this API and format the result." And that is exactly the kind of task a local user — someone who runs models on their own machine with Ollama or llama.cpp — needs to work.

## The Politics of the Benchmark

Choosing a benchmark is not a neutral technical act. It is a political act.

When Anthropic publishes results on MMLU, GPQA and HLE, it is saying: "these are the capabilities that matter." When the open-source community emphasizes MT-Bench, Arena Elo and latency on consumer hardware, it is saying something else: "what matters is the user's experience, not the exam grade."

Which metrics to choose? Tokens per second on an RTX 3060? Response quality in Spanish — no major benchmark evaluates Spanish consistently? Ability to follow instructions in real-world tasks? The decision about what to measure *determines* which models win.

There is no such thing as an objective benchmark.

## The Post-Comprehension Regime

Perhaps the most unsettling finding of this year is that benchmarks are entering what some researchers call the *"post-comprehension regime"*: tasks so difficult that not even humans fully understand the correct answers. Critic-Resilient Benchmarking, proposed in discussions at ICML 2026, uses models as meta-evaluators of other models — an infinite regress in which intelligence measures itself.

This is not science. It is digital theology.

The benchmark becomes an oracle: a mechanism that produces numbers nobody fully knows how to interpret, but everyone uses to make decisions. "GPQA score: 87.3" — what does it really mean? What does the model know now that it didn't know when it scored 86.1? The honest answer: we don't know. But the number is useful because *other market actors use it too*.

## What the Benchmark Does Not Measure

There are crucial capabilities that no benchmark is capturing:

1. **Contextual consistency:** Does the model remain reliable after 50 interactions, or does it degrade silently?
2. **Real multilingual performance:** Spanish, Portuguese, the languages people use outside the English-speaking world.
3. **Cost-efficiency on local hardware:** it doesn't matter if a model scores GPQA 90 if it needs an H100 to run in real time.
4. **Silent alignment:** Does the model avoid causing harm even when it isn't explicitly asked to?
5. **Operational memory:** Can it maintain coherence across long sessions without losing the thread?

No mainstream leaderboard captures these dimensions. And they are exactly the ones that matter to anyone using local AI.

## The Benchmark as Mirror

What a benchmark really measures is not intelligence. It measures **what a given community has decided intelligence is** at a given moment.

When you run a model on your GPU and compare alternatives, you are not discovering which one is "better." You are deciding — implicitly — which metrics you prioritize: speed, accuracy in English, context size or cost. And that decision is your declaration of what kind of artificial intelligence you want to inhabit.

Frontier labs measure performance on GPQA because GPQA is the gateway to multibillion-dollar funding rounds. Local users measure tokens per second because that is what determines whether the model is usable in their daily life. Both measure something real. Neither measures "intelligence" in the abstract.

The perfect benchmark does not exist. But asking *"what should I measure?"* is the most important question we can ask ourselves — because the answer defines what we build.