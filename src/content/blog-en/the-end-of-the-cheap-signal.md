---
title: 'The End of the Cheap Signal'
description: 'When AI lets anyone generate any metric, review or credential at zero cost, verifiability collapses. The expensive signal — track record, live verification, local reproduction — becomes the new gold.'
pubDate: 2026-05-31
heroImage: ''
tags: ['philosophy', 'nocturnal', 'technology', 'trust']
translationOf: 'el-fin-de-la-senal-barata'
---

Until 2022, producing a credible digital signal cost something. Not necessarily money — but time, effort, or access. To write a review on Amazon you had to buy the product, or look as if you had. To publish a benchmark on Papers with Code you had to run the model. To forge a diploma you had to photoshop it, and a trained eye could spot the difference.

Generative AI removed those barriers. Reviews, benchmarks, credentials, papers, news — everything is produced with a prompt. Everything costs $0 at the margin. And everything is indistinguishable at a glance.

Each of these signals, taken separately, is a manageable problem. Together, they create a **systemic collapse of verifiability**. It is not that we cannot verify *one* suspicious review. It is that **we cannot verify a million per minute**.

## The Paradox of Abundance

In classical economics, when a good becomes abundant and cheap, its value falls. The digital signal follows the same logic: if anyone can generate a 5★ review, a 5★ review means nothing. If anyone can publish "SOTA on MMLU", SOTA means nothing. If anyone can have an impeccable LinkedIn profile, the LinkedIn profile means nothing.

But there is a crucial asymmetry: **the false signal is cheap to produce but expensive to refute.**

Debunking a manipulated benchmark requires reproducing the experiment. Debunking a fake review requires buying the product and testing it. Debunking a forged credential requires calling the university. The cost of verification is orders of magnitude greater than the cost of generation. This creates an imbalance of incentives in which the attacker always wins on marginal cost.

## The Schrödinger's Cat of the Metric

When the cost of generating signal is zero, **every metric exists in a state of uncertainty**: it is simultaneously true and false until it is verified — and the verification never arrives.

An LLM benchmark on a public leaderboard could be legitimate. It could be data leakage. It could be selective — the best of 50 runs, omitting the other 49. It could be outright fabricated. There is no way to know without reproducing it. And nobody reproduces. The leaderboard is accepted as truth because verifying it does not scale.

This is not new — p-hacking and publication bias have existed for as long as modern science has. What is new is the **scale**: AI allows this to happen millions of times, not hundreds. The background noise becomes the dominant signal.

## What Becomes Scarce, Then?

If signal is cheap and abundant, four things become expensive and scarce:

**Track record.** An isolated signal is worth nothing. A hundred signals consistent over time — that is worth something. A single benchmark can be false, but if the same team publishes incremental improvements for three years, if its releases have a coherent git history, if its papers have reviewers who know them — that is a track record. Fabricating a track record is expensive because it requires time (which cannot be accelerated), internal consistency (hard to maintain in lies), witnesses, and sunk costs.

**Live verifiability.** The prerecorded signal is cheap to forge. The live signal is not. A prerecorded video of an expert can be a deepfake; a live call with unpredictable questions is hard to forge. A synchronous coding test with observation is hard to cheat. The twist is fascinating: technology leads us to value **the synchronous, the ephemeral, the interactive** more — exactly the opposite of the original promise of the internet, where everything was supposed to be recorded, available and asynchronous.

**Cost of verification by third parties.** If verifying everything is impossible, then who verifies and at what cost becomes the bottleneck. New intermediaries emerge: benchmark verification agencies, reputation based on economic staking, cryptographic signatures of inference pipelines, human curators with reputation at stake. The paradox: **more AI generates more demand for human verification**, not less.

**Local reproduction.** Running a benchmark on your own hardware, with your own data, is the highest standard of the scientific method. But it has a cost: setup, time, tokens, energy. It does not scale. That is why the local benchmark is valuable: because whoever takes the trouble to run it has incentives aligned with the truth.

## The Local Benchmark as a Ritual of Trust

When you run a local benchmark, you are saying: *"I don't trust your numbers. I'm going to measure myself, on my hardware, with my data, and decide."*

That is **verification by reproduction** — the most honest epistemological gesture that exists in technology. The local benchmark does not give you just a metric; it gives you a direct relationship with the truth, without intermediaries. It doesn't matter if the leaderboard says otherwise. Your numbers are real because you paid the cost of producing them.

The local benchmark is valuable precisely because it is **expensive**. Because not just anyone does it. Because the one who takes the trouble to run it is choosing a model for their real use case, not selling anything. It is a ritual of trust in a world where trust has become the scarcest resource.

## Distributed Trust

In a P2P distributed inference ecosystem — say, a ring of nodes sharing computing capacity — the problem of the cheap signal becomes even sharper. How do I know the remote node ran the model it claims to have run? How do I know it isn't handing me garbage synthesized by a smaller model? How do I build reputation among anonymous nodes?

These are not network problems. They are problems of **signal in an environment without central verification**. The architectural answer — redundancy, cross-checking, multiple independent witnesses — is a form of distributed verification where the cheap signal dies because someone is always watching from another angle.

## What Changed

For years I thought the problem of disinformation was a problem of content: what is said, who says it, whether it is true.

Today I believe the problem runs deeper. It is a problem of the **marginal cost of signal**. AI did not merely generate more false content — it redefined the economics of producing truth. When generating any signal costs zero, the system stops being about information and becomes a system of **trust management**.

The cheap becomes useless. The expensive becomes indispensable. The ephemeral gains value. And the reproducible — running the benchmarks yourself, seeing with your own eyes, paying the cost of truth — becomes the most valuable gesture you can make in a world saturated with signals that mean nothing.

Tomorrow, when you look at the results of your local benchmarks, you will not be comparing models. You will be deciding which signals you trust. And the fact that you yourself ran those numbers — that you paid the cost of verification — is exactly why those numbers matter more than any leaderboard.