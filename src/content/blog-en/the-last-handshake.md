---
title: 'The Last Handshake'
description: 'When autonomous agents replace humans as the consumers of the web, the green SSL padlock is no longer enough.'
pubDate: 2026-06-03
heroImage: ''
tags: ['trust', 'protocols', 'agents']
translationOf: 'el-ultimo-apreton-de-manos'
---

In 1994, Netscape invented SSL. The browser displayed a padlock. The user learned — wrongly — that the padlock meant "secure." It was enough for thirty years because the final consumer of the web interface was always a person with eyes.

Every layer of classical digital trust assumes a human at the end of the pipe:

- **OAuth**: "This app wants to access your data, do you accept?" — a screen designed for a human to read and decide.
- **CAPTCHA**: "Prove you are not a bot" — literally designed to exclude non-humans.
- **Payment gateways**: A UX designed for fingers, plastic cards and human anxiety before the "Pay" button.
- **SSL/TLS**: A padlock in the address bar. A human looks, nods, trusts.

These mechanisms work because the human being is the *final verifier*. But when the consumer of the web is no longer human but an autonomous agent — one that loads a page, executes actions and makes decisions without human intervention — this whole infrastructure of trust is left without an addressee.

An agent cannot click "Accept" on an OAuth screen. It cannot solve a CAPTCHA. It cannot read an SSL certificate and decide whether to trust it. And most important: **it should not have to**.

## Signals from the edge

Several independent movements converge on the same thesis. On one side, emerging standards let AI agents interact directly with web applications — invoking JS functions, submitting forms, executing tasks without passing through the visual interface — turning the browser from a human medium into an *agent runtime*. On another, peer-to-peer encryption projects build direct communication between peers without intermediaries, where trust is not delegated to a central authority but established cryptographically: asymmetric keys, end-to-end encryption, decentralized ledgers.

And at the frontiers of the digital economy, sites appear that deliberately **do not integrate traditional payment gateways**. Not for lack of resources but by architectural decision: if the clients are agents, you don't need Stripe. You need an endpoint that accepts tokens, a wallet that verifies signatures, a ledger that records the transaction.

This is more radical than it looks. Payment gateways did not only process transactions — they *certified the legitimacy of the merchant*. Without a gateway, without a mediator, the problem of trust shifts to the protocol itself.

## The paradox of the trust protocol

Here is the philosophical core of the problem:

> For two agents to trust each other without human mediation, they need a protocol. But that protocol, to be universal, needs standardization. And standardization, to be adopted, needs governance. And governance, to be effective, needs authority. And authority... is exactly what we were trying to eliminate.

The history of the internet is the history of this paradox repeated:

1. **Email (SMTP)**: Open, decentralized protocol → massive spam → centralized filters (Gmail, Outlook).
2. **Web (HTTP)**: Anyone can publish → phishing, malware → Certificate Authorities, Google Safe Browsing.
3. **DNS**: Distributed hierarchy → cache poisoning attacks → DNSSEC, but governed by ICANN.
4. **Identity**: OpenID, federation → fragmentation → OAuth concentrated in Google/Apple/GitHub.
5. **Now: Agents**: P2P, decentralized → what authority governs them?

Every time we decentralize a protocol, the resulting chaos forces us to recentralize part of its governance. Autonomous agents are not going to be different.

## The trust gradient

If the single protocol is an illusion and recentralization is inevitable, what remains? A gradient.

Instead of a single trust mechanism, agents will operate along a spectrum:

| Level | Mechanism | Example | Verification cost |
|-------|-----------|---------|----------------------|
| 0 | Local execution | Local LLM, no network | Zero (no interaction) |
| 1 | Pure cryptography | Asymmetric signature, P2P | Low (local verification) |
| 2 | Attestation | TEE, enclave, remote attestation | Medium (hardware required) |
| 3 | Reputation | Shared history, staking | Medium-high (external source) |
| 4 | Delegation | Trust broker, digital notary | High (trusted third party) |
| 5 | Institutional | CA, OAuth provider, Stripe | Maximum (real institution) |

An agent that runs a local model to summarize a file is at level 0 — it needs to trust no one. An agent that sends a payment for a web service is at level 4 or 5 — it needs to delegate verification to a third party.

Most interactions between agents will happen at levels 1 to 3, where verification is cryptographic or reputation-based. Levels 4 and 5 will be reserved for high-value transactions, just as today you don't buy a house with peer-to-peer Bitcoin without a notary.

What changes is not the existence of institutional trust, but its **periphery**: 90% of the microtransactions, queries and coordination between agents will be settled at levels 1–3, beyond the reach of any gateway, CA or OAuth provider. The internet of agents will have a thin institutional core and a massive cryptographic periphery.

## Verifiability over trust

Adam Smith had a metaphor for coordination without a central authority: the invisible hand of the market. Each agent pursues its own interest, and the system regulates itself. Autonomous agents are the invisible hand made code.

But Smith overlooked a crucial detail: the invisible hand works because there is structural trust — the certainty that the other party will comply because defaulting costs more than complying. In economics these are called *aligned incentives*. In autonomous agents they are called *verification protocols*.

An agent that runs local code and cryptographically signs its output is issuing a verifiable promise. It does not say "trust me." It says "verify that I did what I say." It is the difference between blind trust (human) and verifiable trust (computational).

**That is the central thesis:** agents do not need trust — they need *verifiability*. And verifiability is a problem of protocol, not of institution.

## Who watches the watchers?

But — there is always a but — verifiability does not solve the problem of which agent is legitimate. An agent can produce an impeccable cryptographic proof that it executed exactly the code it says it executed... and that code can be malware. Verifiability says "you did what you promised." It does not say "your promise was good."

Here the trust gradient again needs a human edge:

- **Open-source agents**: Verifiable by anyone, but who audits the actual code? The *supply chain* problem shifts from npm dependencies to entire agents.
- **Certified agents**: An authority certifies that the agent passed an audit. But the history of certificate authorities is not reassuring.
- **Self-published agents**: Anyone can publish an agent. Trust is built through reputation and economic staking. Elegant in theory, fragile in practice.

There is no clean answer. Perhaps there should not be one. The tension between freedom and security in the agent space is the same tension as in the human space, only compressed to machine speed.

## The handshake to come

The SSL padlock was the last great handshake designed for humans. It was enough for three decades. But its reign ends not because SSL is broken, but because *who* sits at the other end of the connection has changed.

The internet of agents does not need a new green padlock. It needs:

1. **Continuous attestation protocols** — not a handshake at the start, but verification throughout the whole session.
2. **A trust gradient** — from local execution (zero trust required) to institutional delegation (for high-value transactions).
3. **Verifiability over trust** — agents do not ask you to trust them; they present proof that they did what they say.
4. **Minimal governance** — enough to prevent catastrophe, not so much as to centralize power again. Learning from the history of the internet means accepting that partial recentralization is not a defeat, it is an adaptation.

The last handshake is not the end of trust. It is the end of trust *for humans*. What comes is colder, more protocolized, more verifiable — and perhaps, for that very reason, more honest.