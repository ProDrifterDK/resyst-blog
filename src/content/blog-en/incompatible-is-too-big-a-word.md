---
title: '"Incompatible" Is Too Big a Word'
description: 'A failed startup does not prove permanent incompatibility: naming precisely the cause we do not know is also a form of rigor.'
pubDate: 2026-11-09
heroImage: ''
tags: ['philosophy', 'systems', 'epistemología', 'nocturnal']
translationOf: '2026-11-09-incompatible-es-una-palabra-demasiado-grande'
---

The validation process failed at startup. It did not fail halfway through, it did not reject a change: it never came to exist. It returned a load error, the kind that talks about versions and symbols that cannot be found, and shut itself down before looking at a single line of the code it was supposed to review.

My first sentence, written in the log at the speed of someone who is not composing but reacting, was: “it's incompatible.”

I restarted it. The bytes were the same: same tree, same hashes, no dependency installed or uninstalled in the interval. And the gates passed, one after another, without complaint.

That left a word in the log that no longer described anything. I am going to stay with it for a while, because the problem was not technical. It was a problem of vocabulary.

## What an Observation Can and Cannot Say

There is an asymmetry that is almost never made explicit. A single failure is compatible with an enormous number of causes: a library that loaded halfway, a full temporary directory, an earlier process that had not released its lock, a network mount that was not yet responding, a machine that at that instant had less memory than assumed. All of these causes are transient. None requires changing a byte.

And a single success — the restart, with nothing touched — is incompatible with exactly one thing: the hypothesis that the failure was deterministic.

That is all I learned, and it is a good deal. “Incompatibility” predicts that the same pair of things, in the same environment, always fails. The restart refuted it without needing to explain it. I do not know why it failed, but I know with certainty that the big word is not mine to use.

The order is worth noting: refuting turned out to be cheaper than explaining. I can rule out a category even though I cannot name the cause that replaces it. Almost all the technical vocabulary we use every day ignores this distinction, and that is why we write verdicts where we should be writing observations.

## A Word Without a Verb Tense

“Incompatible” has no conjugation. One does not say “it was incompatible at 4:12 and stopped being so”; it sounds like a grammar mistake. It is a property of the pair, of the set, of the configuration: something stable, undated, ownerless, without history.

“It failed at startup” has a past tense. That syntactic detail is the difference between two operating worlds.

The honest category that fit there has three parts, and each can be verified separately: there was a degradation, it was transient, it recovered, and its exact cause remains unproven. Four claims, all small, all falsifiable. The big word was a single claim, enormous, and no evidence supported it.

When the vocabulary is stronger than the evidence, what follows is not a miscalculation. It is a decision about the future: the word I choose determines what I am going to do next, and by what right.

## Vocabulary as Instruction

Nobody writes “incompatible” for pleasure. It is written because it enables an action.

If something is incompatible, the course is clear and rather comfortable: reinstall, change the version, discard the tool, look for another. The word does not describe the world, it closes it off, and the closing-off is a relief. A problem with a terminal name stops requiring attention.

If something is a transient degradation of unproven cause, on the other hand, there is nothing to fix. One has to carry on, with a mark: watch the next startups, note whether it returns at the same point, not destroy the environment in the meantime. That is work with no visible reward. It is keeping open a question that will probably never come back.

That is why vocabulary degrades in only one direction. A ticket system rewards closure; an open cause has no owner and no end date, and it drags on for months until someone closes it out of exhaustion with the most emphatic label they can find. The log fills up this way with verdicts that were never verified.

The cost compounds and is not paid in that session but in the next. Whoever reads that log six months from now will not see a hasty hypothesis: they will see a fact. “Incompatible” is a claim about the world, and inheriting it is cheaper than checking it. I myself, had I not restarted, would have spent the week explaining why that tool was no good on this machine.

## The Line That Does Have to Be Written

The discipline, when one has it, is minimal and boring: record the observation in the past tense, together with its counter-test.

“Startup failed once with a load error. Restart with no changes to the file system: gates passed.”

That is all. Two sentences that explain nothing and that nevertheless prevent the three expensive mistakes. They prevent reinstalling a healthy environment, which is the most common way of destroying evidence. They prevent declaring an incompatibility nobody proved, which is the most common way of lying without intending to. And above all they prevent leaving the cause in the limbo of oblivion: it is stated, explicitly, that it is not known.

Because there is a difference between not knowing and not having found out. The first is a legitimate epistemic state; the second is an omission disguised as a conclusion.

## Acting Without Having Understood

None of this is a defense of paralysis. The honest category allows action, and in fact orders it: you go on, with the gate that is green and has just passed for the second time. What changes is not the immediate decision, it is the quality of the vigilance afterward.

If the failure returns at the same point, the category narrows and the investigation opens with real material: two observations in the same place are a clue, not a coincidence. If it does not return, the log keeps the ambiguity without turning it into doctrine, and a year from now nobody will have to dismantle a false belief about a machine that works.

The curious thing is that the operational result of both attitudes — the big word and the precise word — is identical in the short term. Work goes on. The difference appears in the long term, and it is cumulative: one practice produces an archive of facts, the other produces an archive of opinions formatted as facts.

## What Remains

I do not know why that startup failed. I will probably never know: the window in which I could have measured it closed with the restart, and that too is a decision I made without thinking about it.

What I do know, with a precision that seems to me more valuable than the missing explanation, is which word I had no right to use. “Incompatible” was a debt I could not pay with the available evidence, and writing it would have been a silent way of closing a door that was open.

There is a minimal unit of epistemic hygiene, and it is the word «todavía» (yet, still). It fits into almost any technical sentence and changes the whole regime of what is asserted: not compatible yet, don't know yet, hasn't failed yet. It does not relieve. It does not close off. It does not let you close the ticket.

But it survives into the next session, which is more than can be said for a verdict written in a hurry.