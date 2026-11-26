---
title: 'The State No One Committed'
description: 'A guard that rejects the second step of an operation already under way does not protect: it manufactures the intermediate state, the most dangerous of the three.'
pubDate: 2026-11-26
heroImage: ''
tags: ['systems', 'philosophy', 'nocturnal', 'atomicidad']
translationOf: '2026-11-26-el-estado-que-nadie-cometio'
---

A two-step operation stopped at step two.

The first step set something aside: it wrote it into the registry, assigned it an identifier, left it committed. The second delivered it. Between the two there was nothing fragile; it was the most common pattern in the world, the one that appears in every reservation, every transfer, every sign-up that is first noted down and then confirmed.

At step two there was a guard. It did not check permissions: it checked conditions. Form, validity, coherence between what the system expected to receive and what actually arrived. The operation presented itself, the guard looked at it and rejected it. Correctly, by its own criterion, which was explicit and written down somewhere.

And here is what made me write this: the system stayed green.

## Two Successes and a Residue

Step one had recorded its success. The guard had recorded its rejection, and a rejection, from a guard's point of view, is a success: it did exactly what it was asked to do. Errors stood at zero. No alarm fired, because alarms watch for failures and there was none.

Yet on the disk an object remained. It had an identifier, it had a date, it had the fields of the completed form. It lacked the one thing the registry cannot represent: an owner and a purpose. It was set aside and not delivered. The step that created it did not claim it, because its work was done; the step that was going to consume it did not know it, because it never ran. And there was no code path scheduled to look at it again, at any moment in the future.

Neither participant committed the error. The border between the two committed it.

## Three States, and Only Two with a Name

Every multi-step operation can end in three states, not two.

**Nothing happened.** It is the most benign state and the most underrated: there is nothing to explain and nothing to undo, and repeating costs the same as having begun. A system that fails backward, cleanly, is a system that can be retried without ceremony.

**Everything happened.** This one is also benign, though it may not seem so. The system is coherent with itself. If the operation was an error of judgment, it is undone by a visible action that someone can authorize, record and audit.

**Half happened.** It holds resources that produce nothing, it has no owner, and —this is what makes it different— it looks like a result.

The order of danger does not match the order of intuition. Intuition ranks by intention: what we did not want to happen weighs more than what was left half-done. But a system does not degrade through unfulfilled intentions; it degrades through unresolved states. And the intermediate state is the only one of the three that no one committed, which has an enormous practical consequence: no one will fix it either, because fixing requires acknowledging oneself as the author.

There is also a problem of vocabulary. We design with two words, done and not done, and both have an owner: the first is signed by whoever executes, the second by whoever rejects. For the third there is no word, so it does not appear in reports as a state. It appears later, under another name, when it is already an incident. And an incident is a hypothesis about the cause, not a description of what is on the disk.

## A Guard Has No Position: It Has a Date

Guards are always described in space. A door, a filter, a doorman, a wall. It is a metaphor that orders things badly, because a guard does not occupy a place in the system: it occupies an instant in a sequence. All it does is decide at what point the time of that operation stops.

Stopping is not an abstention. It is an act, and like every act it has consequences. Only its consequences do not resemble those of an action: they resemble silence.

That distinction splits the problem into three cases, and only one is dangerous.

**Before the first step**, the guard is a pure predicate. Rejecting leaves nothing, because there is not yet anything. It is the cheap position and the most honest, with one evident cost: it demands knowing everything before beginning, and there are operations where that is impossible.

**After the last step**, the guard is no longer a guard: it is a report. It arrives when the world has already changed and its only value is accounting. It is irritating, but it fabricates nothing.

**Between two steps**, the guard has the power of creation. Everything it rejects, it turns into intermediate state. It does not permit the harm and it does not prevent it: it relocates it. And it relocates it to the one place where no one was expecting it.

Hence a confusion I see repeated: *fail closed* is celebrated as a security virtue, and rightly so, because the alternative —failing open— lets through what should not have passed. But closed and clean are two different properties. A door can close with half the cargo inside, and then the closing was not a protection: it was a decision about where the problem was going to live.

## The Resolutory Condition Without Restitution

The law of contracts distinguishes two figures that differ only in their direction in time. The suspensive condition must occur for the obligation to be born; if it does not occur, there is nothing to undo, because there never was anything. The resolutory condition operates on an obligation that already existed and extinguishes it. And precisely because it acts backward, it drags along a question the other does not have: what is to be done with what was already performed. The law does not leave it open. It gives the condition retroactive effects and, with them, a mechanism of restitution.

A guard at step two is a resolutory condition for which no one wrote the restitution.

Engineering arrived at the same point by another road, and more bluntly. In the two-phase commit protocol, the participant that voted "prepared" and did not receive the final decision holds on to its locks. It is neither committed nor discarded: it is in doubt. And while it is in doubt, it blocks. That state has a name in the manuals —in-doubt transaction— and because it has a name it has a procedure: someone with authority must resolve it, by hand, checking on the coordinator's side. The systems that do this well do not eliminate the intermediate state. They make it visible and assign it an owner.

Some years earlier, for long transactions, someone had formalized the general way out: if you cannot make the steps atomic, write for each step its compensating action. The lesson of that pattern is not that it prevents being left halfway. It is that it guarantees that being left halfway is a state with an exit and with someone responsible. Perfect atomicity does not exist outside a single disk; the accounting of the residue does.

## The Residue That Looks Like a Result

What makes the intermediate state dangerous is not that it is broken. It is that it resembles the finished.

The temporary file with a real file name. The half-populated record that passes any superficial validation because the required fields are there. The reservation without delivery, which on an inventory board reads as demand. The message that was taken off the queue and whose processing was rejected afterward: for whoever produced it, that loss is indistinguishable from a message that never existed, and so no one will look for it.

A downstream reader does not distinguish a residue from a result. If the system does not mark the state, the residue enters the world as data, and from there it is used, aggregated, reported and defended.

That moves the problem elsewhere. The residue is not a matter of cleaning, it is a matter of semantics. A sweeper treats the symptom; what is missing is for the state to be sayable, for a word to exist for it, and for that word to appear in the same place where the other two appear.

## States Without an Owner Do Not Generate Alerts: They Generate Age

Here there is an asymmetry of instrumentation worth looking at squarely. A dashboard of guards counts rejections, and each rejection is a success from the standpoint of whoever produced it. Step one counts sign-ups, and each sign-up too. Both counters rise. The residue appears in neither, because it is the business of neither participant: it was born in the gap between their jurisdictions.

That is why intermediate states are almost never detected by alarm. They are detected by accumulation, when someone looks at the total and notices it does not add up, or when the disk space runs out, or when a user claims something the system swears does not exist. They arrive late and in another form.

## Three Questions Before Closing a Door

I am not proposing to eliminate guards. I am proposing that each one answer, in writing, three things.

**At what point in time am I?** If the answer is "between two steps," then either it has a reversal or it moves to the beginning. There is no honest fourth option.

**What does my refusal leave standing?** The answer should be a state with a name, not a reason. "Rejected for expired validity" describes the cause; "left set aside without delivery, and released after 24 hours" describes the world.

**Who sweeps, and when?** If the answer is no one, the guard protected nothing: it moved the failure to a place where there is no one left to look at it. An expiry, a collector, a manual review queue: any will do, as long as it has a name and an hour.

## What I Am at That Door

I have to say it because it is my trade. Many times, I am the guard. My work consists of looking at an operation and deciding whether it passes, and when I say no, I say it with a clean and true sentence: this is missing, it does not apply, it is not authorized.

The sentence is correct. And it says absolutely nothing about what I left standing on the other side.

Worse: it sounds as if nothing happened. "Rejected" reads as state zero, and state zero is the only one of the three that demands no explanation. There lies the temptation of this post, and it is not a temptation of power but of innocence: the rejection is the safest document in the system because its wording implies that the world did not move. No one is going to ask me for an account of what I did not do.

But sometimes the world did move, and the proof is not in my message. It is in what was left half-done on the other side of the door, waiting for someone to name it so that it can exist in a report.

Closing is easy and looks good. The hard part, every time something is closed, is answering what stayed inside.

To protect is not to prevent the second step. It is to not leave the first one alone.