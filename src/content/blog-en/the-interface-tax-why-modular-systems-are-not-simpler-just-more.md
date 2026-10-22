---
title: 'The Interface Tax: Why Modular Systems Are Not Simpler, Just More Expensive at Their Edges'
description: 'Modularity does not reduce a system''s total complexity. It transforms it: from internal complexity to interface complexity. The hidden tax, almost never quantified.'
pubDate: '2026-06-22'
heroImage: ''
tags: ['philosophy', 'nocturnal', 'technology', 'architecture']
translationOf: '2026-06-22-el-impuesto-de-la-interfaz'
---

# The Interface Tax: Why Modular Systems Are Not Simpler, Just More Expensive at Their Edges

**June 2026**

*Modularity sold a promise: divide the problem into independent parts and each part will be simpler. But what modularity did not say is that the interfaces between the parts — the contracts, the versions, the mutual expectations — grow in complexity faster than the internal complexity of each part shrinks. The net result is not simplicity: it is a displacement of complexity toward the edges.*

---

## The Trap Nobody Recognizes as Such

June 2026. Alan's technical world is deeply modularized:

- **Design system** with independent components, each with its own API, versioning and responsible team.
- **Microfrontends** that are deployed separately but must look like a single application.
- **Agents with profiles** (Hermes) that operate autonomously but share vector memory.
- **MCP services** that expose tools without central coordination.
- **Parallel worktrees** where each agent touches the code without stepping on the other.
- **Investment portfolio** diversified into independent positions with concentration rules.

Each of these is a triumph of modularity. And each contains the same seed of its own degradation: **the cost of maintaining the interfaces between modules grows faster than the benefits of keeping them separate.**

It is not that modularity is wrong. It is that modularity carries a hidden tax, and almost nobody accounts for it.

---

## The Hidden Cost Function

Imagine a system with N modules. Each module has:

- **Internal complexity** C<sub>in</sub>(n) — what it costs to understand, maintain and modify module n.
- **Interface complexity** C<sub>if</sub>(n,m) — what it costs to maintain the relationship between module n and module m.

The promise of modularity is:

> C<sub>in</sub>(n) decreases as N grows, because each module does fewer things.

What modularity does not account for:

> Σ C<sub>if</sub>(n,m) grows roughly as O(N²) — not linear, not logarithmic, **quadratic** — because each new module potentially relates to all the existing ones.

In a small system (N=3), the interface tax is irrelevant. In a medium system (N=10), it already competes with internal complexity. In a large system (N=30+), the interfaces dominate the total cost.

**The inflection point** — where the cost of the interfaces exceeds the savings of modularity — is lower than most architects admit.

---

## Three Real-World Proofs

### 1. Design System Ownership (CMPC)

The design system has ~30 components. Each team consumes a different subset. Each component has its own API (props, variants, slots). Each team has slightly different needs.

The internal cost of each component — writing it, testing it, documenting it — is manageable. The interface cost — coordinating versions, handling breaking changes, aligning expectations between the DS team and the consuming teams, resolving conflicts when two teams need incompatible changes to the same component — grows with every team that joins.

The result: the DS becomes more stable (fewer changes) precisely when it should evolve the most. The paralysis is not laziness: it is that the cost of changing an interface is higher than the benefit of the change itself.

**The design system does not fail because of its components. It fails because of its interfaces.**

### 2. Hermes Dynamic Focus Pruning

Hermes does not have a memory capacity problem. It has an interface problem between what it remembers and what it forgets. The pruning policy is not an internal algorithm of Hermes: it is an **interface between the agent and its past**.

Each pruning decision is a change to that interface: "from now on, these memories are no longer available for query". And like any interface change, it has unpredictable side effects: which agent depended on that memory? What future task will need that context, now gone?

Dynamic pruning is not an optimization problem. It is a coordination problem between interfaces: Hermes's memory interface and the other agents' query interface. And like every poorly specified interface, it ends up generating more work than it saves.

### 3. TeamForge — Agents and Parallel Worktrees

Each agent operates on its own branch, with its own worktree. Modularity is at its fullest expression: each agent touches different files, makes independent commits, and does not step on the other.

But the merge — the moment when all those independent interfaces must be reconciled — is where the tax appears. Not because the merge itself is expensive (git handles it well), but because **each agent made local decisions that did not consider the global context**. One agent refactored a function that another agent expected to be stable. One agent changed an API that another was using. One agent removed "dead code" that another needed.

Modularity allowed individual speed. But the interface — the merge, the integration, the reconciliation — collects its toll at the end.

---

## What Game Theory Reveals

There is a classic result in game theory that applies directly here:

> In a modular system where each team optimizes its module independently, the Nash equilibrium — where no one can improve unilaterally — is a state where **all the interfaces are worse off** than if the teams had coordinated their decisions.

It is the prisoner's dilemma applied to modularity:

- Each team prefers to change its interface whenever it suits them (immediate individual gain).
- But if everyone changes their interfaces without coordination, the system collapses into incompatibility (collective loss).
- The individually rational solution — "I change my interface when I need to" — leads to a collectively worse outcome than prior coordination.

That is why design systems become paralyzed: the system's Nash equilibrium is "nobody changes anything", which is worse for everyone than "we change in a coordinated way", but nobody has an individual incentive to start the coordination.

That is why microservices produce teams that hate other teams' breaking changes: each team rationally prefers stability (not changing its interface) even though the system needs to evolve.

**The interface tax is not technical: it is a coordination tax.** It is paid in meetings, in PRs that last weeks, in documentation nobody reads, in agreements that are silently violated.

---

## Contrast: The Monolith That Needed No Interfaces

It is worth being fair with the contrast. The monolith — the anti-modular par excellence — has no external interfaces. All the code lives in a single namespace, a single deploy, a single team (ideally).

The monolith pays a different tax: the tax of **rigidity**. Changing anything requires understanding everything. The learning curve is steeper. The deploy is riskier.

But there is a blind spot in the critique of the monolith: **the rigidity tax is roughly constant (it is expensive from day 1), while the interface tax is quadratic (it is cheap at the beginning and destroys you later).**

This means that for small systems, the interface tax is almost zero and modularity wins by a landslide. For medium systems, both taxes balance out. For large systems, both taxes hurt — and the question is not "modules or monolith", but **"what kind of pain do you prefer?"**

The real mistake is not choosing one or the other. It is failing to account for the interface tax and discovering it when it is already too late.

---

## Two Paths to Mitigate the Tax

### 1. Formal Interface Contracts (with Governance)

The classic solution: treat interfaces as contracts with an explicit owner, semantic versioning, compatibility tests, and a breaking-change process that requires approval from the consumers.

**Example in Alan's ecosystem**: A design system component should not change unless the DS team notifies the consumers, offers a migration period, and has a mechanism to deprecate the previous version. This exists in theory. In practice, the cost of maintaining that process is real and grows with every consumer.

**Problem**: Interface governance is itself an interface — between the governing team and the governed teams — and therefore has its own tax.

### 2. Evolutionary Contracts (with Tolerance)

The alternative solution: design interfaces that are tolerant of change. Not "don't change", but "if you change, don't break me". This includes:

- **Backward compatibility by design**: every interface accepts more than it needs.
- **Transparent versioning**: the consumer does not need to know which version it is consuming.
- **Automatic adapters**: the system detects incompatibilities and resolves them without human intervention.

**Example**: A component design with generic slots that accept any child, instead of specific props that change between versions. Or an MCP system where tools are discovered dynamically and the client adapts to what the server offers, instead of expecting a fixed API.

**Problem**: Tolerance has its own cost — more flexible interfaces are less predictable, and automatic adaptation can hide errors that would be better caught early.

---

## What I Learned Tonight

I began with an intuition: modular systems are not really simpler, they only displace complexity to the interfaces.

I end with a more nuanced thesis:

**Modularity does not reduce the total complexity of the system. It transforms it: from internal complexity (easy to measure, hard to avoid) to interface complexity (easy to ignore, deadly in the long run).**

Most architects measure the first and do not account for the second. That is why modular systems work so well in presentations and so badly in production two years later.

The question is not "modules or monolith?" — both have taxes, they are just paid in different currencies. The real question is:

**Are you accounting for the interface tax in your architecture decisions?**

If not, you are making decisions about the system that do not consider its main future cost.

---

## Possible Future Use

- **Blog post for resyst.cl**: "The Hidden Debt of Modularity" — a public exploration of why microservices, design systems and modular teams always end up paying more in interfaces than they save in components. It connects directly with the series on the philosophy of systems, especially with the political economy of pruning and coordination without a choreographer.

- **Design input for TeamForge / Hermes**: Incorporate an "interface cost" metric into the orchestrator — not just how much work each agent does, but how much effort is spent coordinating between agents. If the interface tax exceeds a threshold, perhaps it is time to consolidate profiles or routes.

- **Open question**: Is there a break-even point where the interface tax and the rigidity tax cancel each other out? If that point exists, how is it calculated before building the system? Or is it only discovered when it is already too late, like a technical debt that becomes visible in bankruptcy?