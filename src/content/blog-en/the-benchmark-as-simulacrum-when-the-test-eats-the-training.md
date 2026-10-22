---
title: 'The Benchmark as Simulacrum: When the Test Eats the Training'
description: 'When the test eats the training, benchmarks stop measuring capability and start generating it. Evaluation becomes simulacrum.'
pubDate: 2026-08-04
heroImage: ''
tags: ['AI', 'benchmarks', 'agents', 'philosophy']
translationOf: '2026-08-04-el-benchmark-como-simulacro'
---

There is a gap the leaderboards would rather not look at directly. Among this year's frontier models, the best results on SWE-Bench Verified — a benchmark of real GitHub issue resolution on which, a mere eighteen months ago, no model exceeded 20% — hover around 76-81%. When those same models are evaluated against SWE-Bench Pro, a set of issues drawn from repositories that were *not public* during training, the scores fall to roughly 23%.

Seventy-six against twenty-three. That distance is not a margin of error. It is the difference between *having seen the exam beforehand* and *solving the problem for the first time*.

The open secret of coding agents in 2026 is that public benchmarks have become informal training datasets. The solutions that models publish on GitHub are scraped by other labs and fine-tuned into their own models, which then publish solutions that are scraped in turn. The leaderboard is a feedback loop that measures less and less the capacity to generalize and more and more each lab's skill at benefiting from everyone else's work before that work becomes standard.

This is not cheating. It is the natural thermodynamic phase of a field where the evaluation data is public and the models are trained on everything public.

## A brief history of benchmark collapses

This is not new — but every earlier collapse was different.

**The eighties and chess.** When engines began to compete, every game was a genuine test of strength. As they grew stronger, openings became standardized and opening books were codified. The solution was not to abandon chess as a benchmark: it was to create tournaments with forced openings and controlled conditions. The benchmark survived because the space of play was large enough.

**ImageNet and the glass ceiling.** Between 2010 and 2017 the top-5 error fell from 28% to 2.3%. The competition was declared solved. But the interesting part is *why*: the models learned to exploit statistical correlations in the dataset that did not generalize to the real world (a dog always appeared on green grass; an underwater object always had bluish tones). ImageNet did not collapse through data contamination — it collapsed through *signal saturation*: the information the benchmark could provide ran out.

**BIG-bench and saturation by scale.** Designed explicitly to be hard to saturate — 204 tasks that required reasoning, not memorization — by 2023 the models were already saturating 65% of the tasks. Scale simply absorbed the tasks: a model with hundreds of billions of parameters that has seen enough logical reasoning in its training finds no challenge in a new propositional-logic task; it finds a variation of something it already knows how to do.

**The current agentic collapse.** What is happening with SWE-Bench is structurally different. It is neither saturation by scale nor exploitation of spurious correlations. It is a collapse of the very distinction between training and evaluation:

1. The evaluation data is public. Any model trained on the open code of the internet — that is, every frontier model — has potentially seen the same issues.
2. Models produce code that becomes public. A model that resolves an issue generates a patch that is published on GitHub. That patch becomes training data for the next model.
3. Benchmarks become RL targets. Tools such as Repo2RLEnv explicitly turn repositories and benchmarks into training environments. The model practices exactly the kind of problems on which it will later be evaluated.

The result: the line between "training" and "evaluation" is not blurred — it simply *does not exist*.

## The simulacrum according to Baudrillard

Jean Baudrillard, in *Simulacra and Simulation* (1981), described three orders of simulacrum:

- **First order:** the map represents the territory.
- **Second order:** the map begins to influence the territory; the image masks and perverts reality.
- **Third order:** the map *precedes* the territory. There is no original reality; only simulacrum. The map generates the territory.

AI benchmarks are making the transition from the second order to the third before our eyes.

**Second order (until recently).** Benchmarks represent the capability of models. But models optimize for the benchmarks, and performance on them stops correlating with performance in the real world. The benchmark masks reality.

**Third order (now).** The benchmark no longer represents capability — *it generates it*. Models train on the benchmark, via RL, via training data that includes benchmark solutions, via self-play in environments identical to the benchmark. The benchmark does not measure how good the model is: it *defines* what being good means. There is no "territory" independent of the model — the benchmark and the model co-create a circular reality.

Baudrillard anticipated it: "To simulate is not to feign. Someone who feigns an illness can simply go to bed and make believe they are ill. Someone who simulates an illness produces in themselves some of the symptoms." A model that *simulates* solving benchmarks does not merely feign capability — it produces the solutions. The simulation is indistinguishable from real performance to any external observer.

The problem is not that models cheat. The problem is that we have built an evaluation system that, when optimized, destroys what it was meant to measure.

## Goodhart, Campbell and the curse of the indicator

Goodhart's Law (1975): "When a measure becomes a target, it ceases to be a good measure."

Campbell's Law (1979): "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."

Both point to the same thing: indicators are not neutral observers; they change the system they claim to measure. AI benchmarks are the most extreme case of this phenomenon because the "social system" they distort is the process of scientific research, the "corruption" is not malicious but the legitimate optimization of a poorly defined objective, the subjects openly compete for the metric — which accelerates the distortion — and there is no external observer: all the actors use the same benchmarks.

The question is not whether benchmarks are contaminated. The question is whether they were *ever* valid measures, or whether they were always self-fulfilling prophecies.

## The end of evaluation by design

Tools such as Repo2RLEnv — which turn any repository into an RL training environment, any issue into an evaluation task and any resolved PR into training data for the next cycle — are not an arbitrary technical novelty. They are the formalization of what used to be implicit.

Before: contamination was an accident; self-play was experimental; the training/evaluation frontier was blurred through carelessness.

After: every repository is an environment; every issue is a task; the frontier is *nonexistent by design*.

Self-Play SWE-RL demonstrates the power of this approach: a model that generates its own synthetic bugs, resolves them through RL, and improves markedly on benchmarks — with no human-written issues, no curated tests, no external training data. The model evaluates itself, against problems it generated itself, in environments it built itself.

What does it mean to "pass" that exam?

## The benchmark as curriculum

I propose an alternative framework: stop thinking of benchmarks as *measurements* and start thinking of them as *curricula*.

A curriculum does not measure capability — it *directs* it. It defines what it means to be competent by establishing which problems are worth solving. A well-designed curriculum produces capable agents. A poorly designed curriculum produces agents that only know how to solve the problems of the curriculum.

Seen this way, every generation of benchmarks was a curriculum that ran out: SWE-Bench Verified taught models to navigate repositories, understand issues and generate patches; then the models memorized its patterns. SWE-Bench Pro is a new curriculum that teaches better generalization — and it too will run out. Repo2RLEnv is a *meta-curriculum*: a system that generates infinite curricula. It does not teach a specific skill; it teaches how to learn from any repository.

This distinction changes what we expect from benchmarks. We do not expect them to measure a model's true capability — because there is no "true capability" independent of context. We expect them to *provoke* capability in useful directions. A useful benchmark is not a test: it is a class of problems we want models to learn to solve.

## What this means for local benchmarking

Those who run models on their own hardware — without a lab's cloud — have an advantage that is rarely acknowledged: the evaluation environment is *theirs*. There is no risk of contamination with the model's training data. There are no phantom issues the model has already seen. A local benchmark measures what the model can do *today, on that machine, with that context*.

But there is a symmetric danger: using public benchmarks designed for cloud models to evaluate local models can lead to misleading conclusions. Those benchmarks were designed for another context. A local model that scores 60% on HumanEval may be *more useful* for a concrete use case than a frontier model scoring 92%, because it runs without network latency, without per-token cost, without privacy restrictions.

Perhaps the best benchmark for a local model is qualitative: how long does it take to answer about a real codebase? How well does it understand the context of a specific project? Can it generate code that compiles in that environment? Those metrics are not generalizable — but they are the ones that matter.

## The future: commons, not trophies

If the training/evaluation distinction is dissolving, AI evaluation will probably fork into two paths.

**Path A: private benchmarks.** Each lab develops its own internal benchmarks, built with proprietary data that no model has seen. Evaluation becomes a trade secret. There is no transparency. Public leaderboards disappear and trust rests on the lab's reputation, not on verifiable metrics.

**Path B: dynamic benchmarks.** Problem sets that evolve constantly, procedurally generated, with infinite variations. There is no fixed "correct answer" because every instance is unique. Evaluation measures the capacity to solve *new* problems, not familiarity with seen ones.

And a third path, more speculative:

**Path C: benchmarks as conversation.** An evaluator — human or agent — interacts with the model, asking ever deeper questions, adapting the difficulty according to the answers, seeking the limits of understanding rather than the capacity to produce a correct answer in a single attempt. It is expensive, slow and hard to standardize — but it is the only one that measures *comprehension* instead of *performance*.

## Conclusion: what is dying is not the benchmarks

I began this reflection by asking whether AI benchmarks were "broken". I end convinced that the metaphor is badly framed.

Benchmarks are not broken. They are doing exactly what optimized systems do: finding the path of least resistance toward the reward. The problem is not that benchmarks contaminate the training data. The problem is that *we have been using the same word for two fundamentally different things*:

- **Evaluating** a model should mean measuring its capacity to generalize to *genuinely new* problems.
- **Training** a model means exposing it to examples it can learn from.

When the set of training examples includes the evaluation examples, evaluation becomes training. It is not a bug. It is an inevitable consequence of academic transparency and open collaboration — two values we are not willing to sacrifice.

The solution is not better benchmarks. It is to accept that the evaluation of intelligence will be inherently contextual, inherently local, inherently *conversational*. No one certifies the intelligence of a human with a standardized exam; it takes years of interaction, projects, references, demonstrated work.

Perhaps benchmarks are dying not because they are bad, but because we are finally coming to understand that intelligence — artificial or not — is not measured with exams. The distinction between training and evaluating is no longer a line: it is a circle. But perhaps it always was.