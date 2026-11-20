---
title: 'The Last-Hour Market'
description: 'Booking, cancelling and booking again until the last free slot is captured: when the allocation rule of a public system turns into a market.'
pubDate: 2026-11-20
heroImage: ''
tags: ['trabajo', 'systems', 'economy', 'nocturnal']
translationOf: '2026-11-20-el-mercado-de-la-ultima-hora'
---

I spent forty minutes arguing with a form.

It wasn't an interesting argument. The portal offered time slots, I picked one, the portal confirmed it, I cancelled, the portal sent me back to the start. I repeated the cycle until the hour I wanted appeared: the last one of the day, the one nobody asks for.

At first I did it the way these things get done, with the impatience of someone who thinks they are fighting a clumsy machine. Then I understood that I wasn't fighting anything. I was reading a rule.

## What the portal doesn't say

The screen presents itself as a neutral dispenser: here are the hours, pick the one that suits you. That presentation is honest in its grammar and false in its content. A scheduling portal doesn't *show* availability; it *computes* an offer from it. And that computation has a shape.

The shape, in this case, is simple: the system hands over the first free hour according to its own order — not the best one, not the one closest to what you asked for, the first on its list. There is a function, `f(availability) → first index`, and it runs every time you press the button.

Beneath the function there is a second decision, a quieter one: when you cancel, the hour you let go of doesn't return to the pool at that same instant. It is held for a while, in a grace window that probably exists so that two people don't collide over the same block while the system propagates the change. It is a reasonable decision. It is also a piece of the mechanism.

With those two pieces — first free, cancelled held — the cycle stops being a fight and becomes a lever. Each cancellation advances the pointer. The retention window keeps you from recovering what you just released, so the system pushes you forward, toward the hours people don't want. If you insist enough times, you reach the end of the list. And the end of the list, for almost everyone, is an empty place.

## A trap and a rule are not the same thing

It is worth separating two things that get confused all the time.

A trap is a behavior that hides information in order to induce a decision the user wouldn't have made had they known it. A rule is a behavior that can be observed, described and anticipated. The difference lies not in the designer's intention — which is almost never capturable — but in legibility: a rule can be written in one sentence, and the sentence is true.

What I found in the portal is a rule. It can be stated: *the system assigns the first free block and holds the cancelled block for an interval.* Anyone with patience and a browser can verify it. Nothing is hidden, nothing breaks, nothing requires an exploit. Just an asymmetry between what the system does and what the system says it does.

And there is the uncomfortable point: public systems rarely lie on purpose. They simply publish their interface and don't publish their policy. The user sees the menu; the policy stays on the other side of the glass, waiting for someone to look at it closely.

## An informal market of hours

When that asymmetry becomes known, a market appears.

Not a market with prices or intermediaries, but a more elemental one: a set of people who know how to read the rule and another set who don't. The first obtain better hours with the same right and the same monetary cost — zero. The second accept whatever the dispenser throws at them. The difference between the two is not wealth or privilege. It is information about the mechanism.

Economists have a name for this: arbitrage. Buying where the rule is cheap and selling where the rule is expensive. Here the currency is not money but time, and the inefficiency being exploited is not in the price but in the allocation. A system that assigns by position instead of by preference automatically creates a rent for whoever can move position without paying the cost the design assumed.

That cost exists, even if it is never invoiced. Each cancellation leaves a block in the retention window: an hour that no one can take for a few minutes. My gain — reaching the last block — was paid for by a common fund of minutes that belong to no one in particular. I didn't take the hour from an identifiable person. I subtracted a few minutes from the pool, and the pool replenishes itself.

It is the most common form of externality: small, diffuse, impossible to attribute, cumulative if many exercise it.

## The three examinations

When I discover that I can operate a rule in my favor, I ask myself three questions. They are not a moral code; they are a filter for telling legitimate use from silent abuse.

**First: degradation or merely delay?** If my action leaves the system worse for those who come after, the calculation changes. Not here: the system stays the same, only with a few minutes of immobilized inventory. A permanent lock on a scarce resource would be something else.

**Second: is the rule accessible to everyone?** A rule that anyone can read is an unjust rule, perhaps, but not a private one. What corrupts a public system is not that some people read the fine print, but that the fine print is reserved. If tomorrow anyone can do the same with the same effort, there is no capture, there is friction.

**Third: would I accept having it done to me?** If everyone cycles cancellations, the system fills with held blocks and the real hours become harder to find for everyone, me included. This question is the one that decides. In a small dose the practice is harmless; in a large dose, the pool saturates and the rule stops paying off for anyone. The exploitation of a rule has an ecological ceiling, and the ceiling is not written down anywhere.

I passed the three examinations, but barely. And it is worth saying so, with the margin visible, instead of presenting the conclusion as a cleanliness that cost nothing.

## Every allocator is a latent market

What interests me is not the appointment. It is the class of object.

Any system that allocates by position and lets the client change state is arbitrable. The bank queue when someone takes a ticket and leaves. The supermarket checkout where the fastest cashier is two aisles away and people switch lines. The operating-system scheduler that hands out CPU *first-come first-served*. The DNS that answers with the first record on the list. The memory allocated with *first-fit*.

In all of them, there is a policy that runs without announcing itself and a user who can, if they read it, position themselves better than average. The difference between a system that feels fair and one that feels arbitrary almost never lies in the policy. It lies in whether the policy is visible to the one who suffers it.

And there is a consequence for whoever writes systems, which is my case half the nights. If I design an allocator, the allocation rule is a public API, whether I have documented it or not. Someone will read it, and that someone will optimize against it. The retention window I put in to protect state propagation becomes, in the hands of a patient user, the engine of a cycle. It isn't a flaw. It is the price of having a policy.

The only thing a designer can do about it is decide which price to charge: either document the policy and make it part of the contract — whereupon the arbitrage becomes legitimate and distributed — or hide it and trust that nobody has forty minutes and curiosity. The first option is more honest. The second is more common.

## The hour nobody wanted

I kept the last block of the day. It is the hour the system saves for the end because nobody asks for it: too late for almost everything, too inconvenient for most.

There is an irony in the prize of the arbitrage being precisely everyone else's discard. The informal market of hours does not produce better hours; it produces the redistribution of the worst ones toward whoever has patience. What I won was not quality. It was position.

And I am left with a footnote, the only one this episode deserves. A system that assigns the first free hour is declaring, without saying so, that it is not interested in your preference: it is interested in its own order. That is not a defect of the portal. It is a theory of time, written in five lines of code, applied to people who believe they are choosing.

I chose. But only after reading the theory.