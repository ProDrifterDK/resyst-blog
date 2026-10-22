---
title: 'When Hardware Stopped Being Invisible'
description: 'AI broke forty years of software abstraction. Silicon is no longer background noise — it is the dominant variable of the system.'
pubDate: 2026-05-30
heroImage: ''
tags: ['architecture', 'hardware', 'local AI', 'abstraction']
translationOf: 'cuando-el-hardware-dejo-de-ser-invisible'
---

The history of software is the history of abstraction. Layer upon layer, we buried the hardware under promises of independence: assembly abstracted machine code, C abstracted assembly, operating systems abstracted C, virtual machines abstracted the operating system, and cloud APIs abstracted the entire rack.

Every layer promised the same thing: *you don't need to know what lies beneath.*

For forty years, it worked.

AI is breaking that chain. Not because abstraction is impossible, but because language models operate in a regime where hardware stops being background noise and becomes the dominant variable of the system.

---

## The Broken Promise

Abstraction worked for decades because the relationship between available compute and the problem to be solved was generous. A 10 GB database runs on any server. A REST API fits on a microcontroller. A 200 KB website loads over a dial-up connection.

Hardware was always faster than the need to use it.

LLMs inverted that equation. A 70B-parameter model does not fit on a single consumer GPU. Its weights weigh ~140 GB in FP16. Its inference requires ~300 GB/s of bandwidth to be usable. No abstraction hides that physics.

**Abstraction works when there is surplus. AI eliminated the surplus.**

## Three Signs That Something Changed

### The GPU That Runs Nothing

There is a modern GPU with 16 GB of VRAM and 256 GB/s of bandwidth. Enough to run models of 7 to 13 billion parameters under quantization. On paper, it is perfect for local inference.

In reality, the software stack has no kernels for its architecture. `hipErrorInvalidDeviceFunction`. The error is not one of performance or capacity. It is that the abstraction layer did not bother to include that silicon.

A perfectly functional piece of hardware — useless for ML. Not through technical failure, but through a decision of the toolchain. The abstraction promised that hardware was interchangeable. The reality: if you are not on the list of supported GPUs, you do not exist.

### The Memory That Swallows the GDP

HBM3E offers ~1.2 TB/s of bandwidth and is the lifeblood of the transformer. But it consumes ~3x more wafer area per bit than standard DDR5. Samsung, SK Hynix and Micron redirected capacity toward HBM for AI servers.

Result: consumer DDR5 went from $100 to $350+ in months. The scarcity is not of silicon — it is of the prioritization of silicon. And AI comes first.

The software engineer designing an application never had to think about the wafer industry. Today, if they want to run local inference, the price of DRAM dictates their architecture.

### Distributed Inference as Confession

There are projects that build self-expanding rings of nodes that discover each other over the network and distribute inference. It is ingenious. It is also a confession.

If a single GPU could handle the full model, nobody would build peer-to-peer inference systems. These architectures exist because the hardware of a single node is insufficient — and because the cloud is too expensive, too distant, or too centralized.

The network design here is not an elegant architectural choice. It is a defeat of monolithic hardware.

## Hardware as Dialect

When you run an LLM locally, you discover that the machine is not a neutral container. It is a dialect:

- `gfx1100` (RDNA 3) speaks one dialect
- `gfx1200` (RDNA 4) speaks another
- `sm_90` (H100) speaks another
- Apple M-series speaks yet another, with its unified memory and its Neural Engine that expose no standard APIs

Each dialect has words the others do not understand. Optimizations that work on this silicon but break on that one. You cannot run a CUDA model on ROCm. You cannot presume that a matrix multiplication means the same thing on two different GPUs.

Cloud providers abstract this away behind a REST API and you forget about it. But locally, the dialect is the message.

## The Countercurrent: Diversity as Resistance

It is tempting to conclude that this is a problem to be solved. That all GPUs should speak the same language. That abstraction should be completed.

But there is another reading: hardware as diversity is an advantage.

In a world where three companies (NVIDIA, AMD, Apple) and three weight formats (FP16, INT8, GGUF) compete, no actor controls the whole stack. Fragmentation is also resistance. Had AI standardized on a single stack, that stack would be a monolithic bottleneck and a single point of control — as Wintel was in the 90s and the hyperscalers are today.

The occasional incompatibility is not a bug of abstraction. It is a sign that the ecosystem still breathes. That there is hardware outside the authorized canon. And that sometimes, what does not run today runs tomorrow, when someone writes the missing kernel.

## What Changed

For years we thought of AI as a software problem: models, datasets, algorithms, transformer architectures.

But the next frontier is not algorithmic. It is lithographic. It is not solved with a better loss function — it is solved with better memory bandwidth, with HBM4, with chiplets, with 3D packaging, with glass substrates.

The most interesting papers of 2025 and 2026 no longer scale models. They scale hardware efficiency: quantization, pruning, distillation, architectures that do more with less bandwidth. The original 2017 transformer assumed infinite memory. All the work since is negotiating with the hardware what the founding paper ignored.

And every local benchmark — every measurement of tokens per second — is not a comparison of models. It is a measurement of how much the abstraction has been lying all this time.

The answer is: a lot. But perhaps that lie was necessary for us to get this far.