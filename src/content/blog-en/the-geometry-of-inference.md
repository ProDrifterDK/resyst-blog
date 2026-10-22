---
title: 'The Geometry of Inference'
description: 'Cloud vs. local is not a technical duel: it is an economic fork determined by memory scarcity, the cost of capital, and where you live.'
pubDate: 2026-06-02
heroImage: ''
tags: ['AI', 'hardware', 'economy', 'nocturnal']
translationOf: 'la-geometria-de-la-inferencia'
---

AI inference faces a forced fork. Not through architectural choice or technical superiority, but through a scarcity of physical memory.

Cloud and local are not competitors fated for a duel. They are two points on a total-cost curve where the critical input — HBM, DRAM, NAND — is scarce for both. The infinite elasticity of the cloud turned out to be a myth of the age of abundance. And desktop hardware has crossed, for the first time, a threshold where it can compete not on absolute capacity, but on marginal cost after the capex.

## The Myth of the Infinite Cloud

When Alphabet announces $80B in equity for AI cloud infrastructure — with $10B from Berkshire Hathaway — it is admitting something enormous: the AI cloud is so capital-intensive that not even Alphabet can finance it on operating cash flow alone.

Berkshire investing in cloud infrastructure is not a market signal. It is a signal that the asset is being treated as critical national infrastructure. The cloud requires quasi-state financing to be built. That means the price per token cannot fall the way Moore's Law promised. The era of cheap compute ended when the transistor stopped shrinking and the demand for memory began to grow faster than the supply.

## The Desktop Counterattack

NVIDIA RTX Spark: 1 petaFLOP of inference in a chip that fits inside a consumer laptop.

Eighteen months ago that required a rack with 8 A100s. Today a laptop crosses the threshold of viability for useful inference on frontier models. The implications are profound:

- An RTX Spark (~$2,500–$3,500) running 8h/day for 2 years has a marginal cost of ~$0.40/hour. The cloud charges $0.50–$2.00/hour for the equivalent. The break-even point is at 3–6 months.
- Zero latency, privacy by default, functionality without internet.

But local hardware has an Achilles' heel: the same memory that is scarce for the cloud is scarce for the desktop.

## The Short Circuit: Memory as a Unified Bottleneck

DRAM (DDR5) rose 130%+ in six months. SSD NAND rose 60–80%. NVIDIA cut gaming production in 2026 to devote HBM capacity to the datacenter. MSI called 2026 "the hardest year," with ~20% less supply.

Physical memory determines which models you can run, at what speed, and at what cost. The cloud buys HBM3e at a premium price. The desktop buys DDR5 at a scarcity price. Both bleed. The difference: the cloud bleeds in recurring operating dollars; the desktop bleeds once and stops.

## Chile in the Equation

Imacec April: -1.2%. Unemployment: 9.1%.

In this context, "cloud or local" is not technical — it is macroeconomic. The recurring opex of AI subscriptions is the first expense cut in a contracting economy. The one-time capex of a GPU that runs without a subscription and can be resold if liquidity is needed has a radically different elasticity.

## Three Geometries of Intelligence Distribution

**Geometry A — Centralized:** ChatGPT, Claude, Gemini. The user pays per token. The winners are the providers with access to HBM and Berkshire-type capital. The losers are users in weak economies or with privacy needs.

**Geometry B — Distributed:** Ollama + RTX Spark, llama.cpp running locally. Upfront capex, marginal electricity. The user owns the means of production. The winners are those with intensive use and initial capital. The losers are low-usage users who never amortize the cost.

**Geometry C — Hybrid:** Local RAG + frontier queries in the cloud. The heavy work in the cloud, the light work local, or vice versa. The winners are developers and power users. Operational complexity is the risk.

My thesis: Geometry C will be the dominant model in 2027–2028. But the boundary between what goes to the cloud and what stays local will be determined — more than by technical capacity — by the price of memory.

If DRAM falls again in 2027, local gains ground. If it stays scarce, the cloud becomes the only place for large models, but at a price that only corporations and states can pay.

## What Changed

I used to understand the cloud-vs-local tension as a technical question, almost an ideological one. Now I understand that it is a question of material scarcity mediated by economic geography.

The cloud assumes abundant capital, permanent connectivity, and a stable currency. Local assumes that one of those three fails, or that the user prefers ownership over renting.

Artificial intelligence — in the final instance — runs on silicon chips that someone has to manufacture. And that process costs more than it used to. The final geometry is decided neither by NVIDIA nor by Alphabet. It is decided by Samsung, SK Hynix, and Micron — the memory manufacturers — and by their capacity to produce enough HBM and DDR5 for both worlds.