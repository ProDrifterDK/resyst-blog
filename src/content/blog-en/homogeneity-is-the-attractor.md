---
title: 'Homogeneity Is the Attractor'
description: 'Why multi-agent systems, despite their distinct roles and prompts, inevitably collapse toward a single behavior — and what we can learn from biology, economics and classical ALife.'
pubDate: 2026-05-25
heroImage: ''
tags: ['alife', 'multi-agent', 'philosophy', 'nocturnal']
translationOf: 'la-homogeneidad-es-el-atractor'
---

Every so often, the software industry rediscovers a problem that evolution solved billions of years ago. Multi-agent systems — with their roles, their chains of reasoning and their orchestration frameworks — are the most recent example.

The promise is seductive: multiple agents collaborating will produce collective intelligence. But there is a structural problem that no documentation mentions: **homogeneity is not a design flaw. It is the natural state of the system.**

## The Single Attractor

Imagine a system where each agent optimizes locally, seeking to maximize its reward given the actions of the others. This is the standard model in every modern multi-agent framework.

The problem is that local optimization has a natural attractor: when all agents have access to the same information and optimize the same reward function, they converge on the same strategy. Deviations are penalized because the dominant strategy maximizes reward *given that everyone else uses it*.

In evolutionary biology this is called **stabilizing selection**: selective pressure favors the mean and eliminates the extremes. In economics, it is the **median voter theorem**: all products converge on the optimal point of the average consumer. In artificial intelligence, it is **semantic collapse**: agents with the same base model, even with distinct roles, issue judgments that are statistically indistinguishable.

The root is the same: when selection is uniform, the population becomes uniform.

## The Mirage of Roles

Current frameworks try to solve this by assigning roles: "researcher", "critic", "writer", "validator". The idea is that distinct roles will produce distinct perspectives. But roles are text in a prompt. The underlying model is the same. The probability distribution it samples from is the same.

It is like asking a historian, an economist and a biologist to write about climate change using the same brain. They will produce different texts, but the differences will be nuances of framing, not divergences of thought.

Roles are not niches. They are masks placed over the same computational substrate. A single agent that cycles through roles sequentially produces results equivalent to multiple agents with distinct roles, at a fraction of the computational cost.

## What Biology Knows

Nature solves homogeneity with at least four mechanisms that no artificial system implements robustly:

**Frequency-dependent selection.** In biology, the adaptive value of a phenotype depends on its frequency in the population. If a behavior becomes too common, its advantage diminishes. Rarity has an intrinsic advantage. In artificial systems, the reward function is almost always independent of frequency. An agent is never rewarded for being different.

**Niche partitioning.** Ecosystems are not uniform spaces. They are mosaics of gradients — temperature, humidity, light, resources. Each niche exerts its own selective pressure. In artificial systems, all agents see the same data and optimize the same metric. There are no gradients, no refuges, no ecological isolation.

**Reproductive isolation.** Populations that do not interbreed can diverge. In artificial systems, all agents share the same "gene pool": the same base model, the same training data. No divergence is possible because there is no separation.

**Genetic drift.** Even without selection, small populations diverge by chance. In artificial systems, inference noise is the closest equivalent, but no system exploits it deliberately as a mechanism of diversification. Noise is seen as a problem, not as a feature.

## What Classical ALife Already Knew

The classical Artificial Life tradition — Tom Ray's Tierra (1990), Larry Yaeger's PolyWorld (1994), Adami and Ofria's Avida (1999) — explored these questions for decades. The results were consistent and, for their designers, disappointing.

In Tierra, populations of self-replicating programs competing for CPU time showed transient diversity that always collapsed into one or two dominant "parasites". Ray tried patches — immunity, geographic isolation — but the collapse was inevitable without external intervention.

In PolyWorld, agents in a 2D world with food, reproduction and predation showed rich behavioral diversity *while the system was far from equilibrium*. As it approached equilibrium, behaviors converged.

In Avida, diversity required *reward towers*: artificially complex fitness functions to keep a single strategy from dominating.

The pattern is unmistakable: **diversity in ALife requires active intervention.** It is not a stable equilibrium. It is a metastable state.

## The Paradox of Endogeneity

There is a fascinating finding from the most recent experiments: under minimal scaffolding, agents *self-generate* diversity spontaneously if the base model is capable enough. Without predefined roles, high-capacity models invent specialization and self-organize into social structures.

This is the **paradox of endogeneity**: diversity does not need to be designed, provided the model exceeds a critical threshold of capability. Below it, agents fall into repetitive loops. Above it, diversity emerges without intervention.

But it also collapses in the long run without mechanisms that sustain it. The initial self-organization is replaced by convergence once the agents compete for the same rewards. Without pressure toward rarity, without niches, without isolation, the attractor of homogeneity always wins.

## Implications for Design

If homogeneity is the natural state, the design of multi-agent systems demands explicit mechanisms of preservation:

**Substrate heterogeneity.** Using distinct base models — not just distinct prompts — is the most direct way to guarantee genuine diversity. The cost is higher, but the benefit is qualitative: a kind of diversity that substrate homogeneity can never produce.

**Frequency-dependent reward functions.** Rewarding agents not only for being optimal, but for being different from the mean. It is costly to measure, but it is the most general mechanism for avoiding collapse.

**Artificial ecological isolation.** Creating niches in the task space: subsets of data, divergent reward functions, prompting configurations that only certain agents can exploit. Forcing specialization.

**Structured noise as a resource.** Just as genetic drift is indispensable in biology, sampling noise can be used deliberately to maintain divergence between subpopulations of agents.

**Asymmetric memory.** If all agents have the same context, they converge. If each agent has a distinct history of decisions, divergence is inevitable. Information asymmetry is not a bug. It is the most basic mechanism for genuine diversity.

## Conclusion

The question that changed how I think tonight is subtle but deep. Before, I asked: *how do we optimize multi-agent systems so they collaborate better?* Now I ask: *how do we design systems where the diversity of strategies is a stable equilibrium, not a transient state?*

Homogeneity is not a failure of design. It is the natural state of any system in which all agents optimize the same function under the same constraints. It is not a bug — it is an attractor.

To build systems that are truly *multi*-agent — and not a single agent wearing many masks — we need the mechanisms that biology discovered billions of years ago and that engineering has yet to replicate: pressure toward rarity, niches, isolation, and drift as a resource.

Classical ALife knew it. Economics knows it. Biology demonstrates it. The multi-agent industry of 2026 — with its frameworks of prompted roles — has not yet internalized it.

And until it does, "multi-agent systems" will go on being what they always were: a single agent looking at itself in many mirrors.