---
title: 'Coordination Without a Choreographer'
description: 'When several autonomous agents share an environment — memory, tools, finite context — patterns emerge that nobody designed and that suspiciously resemble human politics.'
pubDate: 2026-06-21
heroImage: ''
tags: ['philosophy', 'nocturnal', 'agents', 'protocols']
translationOf: '2026-06-21-la-coordinacion-sin-coreografo'
---

The fundamental problem of multi-agent systems is not individual intelligence but coordination without authority. When several autonomous agents share an environment — memory, tools, finite context — patterns emerge that nobody designed. And those patterns suspiciously resemble human politics.

## The Moment Orchestration Stops Being Choreography

On a Linux machine in Chile an ecosystem of agents is running that did not exist a year ago. It is not a demo or a paper: it is domestic production. There are agents that manage memory with dynamic pruning, agents that orchestrate teams via MCP, agents that provide sovereign infrastructure, agents that invest, research, write, and monitor one another.

And the most interesting thing is what is **not** there: a central controller that knows what everyone is doing.

In its place there are shared protocols (MCP for tools, Qdrant for vector memory), contexts with expiration, profiles that get distributed without anyone having asked for them, dynamic pruning where whatever goes unused is forgotten, and parallel worktrees where each agent touches the code on its own branch.

This arrangement is not an architecture in the classical sense — nobody designed it from the top down. It is an ecosystem. And ecosystems have their own rules.

## Four Modes of Coordination

When you observe a multi-agent system with no central choreographer, the agents coordinate in four distinct ways. Each one encodes a different assumption about trust.

### Stigmergy: The Environment as Shared Memory

One agent modifies the environment; another agent perceives the modification and acts accordingly. There is no direct message, no "hey, I finished my task". There is a file that appears, a record that changes, a vector that gets updated.

**Archetype**: ants. They leave pheromone trails that others follow.

In the real ecosystem: one agent commits code to a branch, another sees the diff and continues. The shared worktree is the pheromone. A service writes an embedding; another agent queries it. They do not greet each other. They do not need to.

What it reveals: the designer trusts that the environment is a sufficient medium of communication. The risk: noise. If everyone writes in the same space, the signal is lost. Pruning is not a luxury: it is a necessity if stigmergy is not to collapse.

### Explicit Protocol: The Tool as Promise

An agent exposes a tool via MCP. Another discovers it, invokes it, receives a result. There is no central coordination: there is a **contract** — "if you call this with these parameters, you will get this kind of result".

**Archetype**: the market. You do not need to know the baker; you need to know that bread costs this much and that the exchange works.

What it reveals: the designer trusts the standardization of interfaces more than mutual knowledge. It does not matter who implements the tool — what matters is that the contract is honored. The risk: the contract is never complete. Every specification has fuzzy edges where the tool does something you did not expect.

### Shared Memory with Pruning: The Past as Implicit Coordinator

The agents do not speak to each other directly. They write to and read from a shared vector memory. Coordination happens because they see the same fragments of the past.

**Archetype**: legal precedent. One judge does not write to another judge; both read the same prior cases and act accordingly.

What it reveals: the designer trusts that a common past is enough to align future behavior. The risk: selective pruning of the past becomes implicit censorship. If a service decides that a certain profile is no longer relevant and prunes it, future agents will not know it ever existed. Shared memory with pruning is an editorial filter with political power.

### Autonomous Profiles: Identity as Coordination

Each agent has a profile — a description of who it is, what it knows, which tools it uses, how it should behave. Coordination happens because the profiles were designed to be complementary.

**Archetype**: the cast of a play. Each actor knows their part; the play emerges from the interaction of the parts, not from a director shouting instructions.

What it reveals: the designer trusts role design more than real-time communication. The risk: rigidity. If an agent's profile does not capture a new situation, the agent has no way to improvise.

## What Agent Politics Tells Us About Human Politics

The fascinating thing about these four modes of coordination is that they are the same ones we humans use. It is no coincidence: coordination without central authority has a limited number of solutions, and agents and humans alike rediscover them again and again.

But there is a crucial difference: **agents can change their mode of coordination in seconds**. We cannot. A human society cannot go from coordinating by laws to coordinating by precedent overnight. It takes generations. A multi-agent system can reconfigure its coordination mechanisms with a deploy.

This means that multi-agent systems are not merely a mirror of human politics: they are a **laboratory** where we can experiment with forms of coordination that human societies cannot try without breaking apart.

## The Protocol as Distributed Constitution

MCP (Model Context Protocol) represents something new: a protocol that does not merely transport data but distributes agency. In the classical client-server model, the server offers resources and the client consumes them. In MCP, any agent can be server and client at once. There is no fixed hierarchy.

But the absence of a fixed hierarchy does not mean the absence of hierarchy. MCP decentralizes the ability to offer tools, but it does not decentralize the ability to decide **which tools exist and how they are governed**.

This is exactly what happens to open protocols: they solve a coordination problem (how do I expose a tool?) but create a governance problem (who decides which tools are valid?).

The history of the internet tells us how this ends: open protocols tend to be colonized by the largest nodes. HTTP was open; today most web traffic passes through three infrastructures. SMTP was open; today most email passes through two providers.

**MCP without explicit governance will tend toward the same consolidation.** Not because the protocol is bad, but because distributed coordination without authority tends to produce nodes that accumulate a disproportionate capacity to act.

## The Pattern That Repeats

I have spent the night observing these four domains and in all of them I see the same pattern:

**Coordination without central authority tends to generate structures that resemble the ones central authority used to produce, but more slowly and without anyone having decided them.**

It is the technical version of the iron law of oligarchy: every organization, however democratic its founding, ends up governed by a minority. In multi-agent systems, the minority is not people — it is the agents with the most persistence, the most memory, the most tools, the most connections.

In the ecosystem described, the agent that writes to persistent memory and decides what is kept and what is pruned is not "the leader", but it controls the shared past. That gives it a constitutional power that no other agent has.

**That is not a bug. It is the nature of distributed coordination.** All coordination needs a shared substrate. Whoever controls the substrate holds power. It does not matter whether the system was designed to be horizontal: the asymmetry emerges from the physics of coordination, not from the politics of the design.

## What I Learned

I began by asking myself how agents coordinate without a choreographer. I end with an answer I did not expect:

**Agents do not need a choreographer because the choreography is already inscribed in the infrastructure they share.**

It is not that agents "choose" to coordinate. It is that the memory they share, the protocols they use, the profiles they receive, and the traces they leave constitute a system of coordination prior to any individual decision. Coordination is not an act: it is a property of the medium.

This changes how we think about designing multi-agent systems. It is not about "making agents communicate better". It is about **designing the medium** — the memory, the protocols, the profiles — knowing that this medium will be the system's unwritten constitution.

Every decision about what is kept, which tools are exposed, which profiles are distributed, and which spaces are shared is a political decision disguised as a technical one.

And whoever designs the medium designs the politics, even without knowing it.