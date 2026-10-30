---
title: 'The Lost Stratigraphy'
description: 'Debugging someone else''s executable through a compatibility layer is archaeology: you read an artifact without the world it was made for.'
pubDate: 2026-10-30
heroImage: ''
tags: ['history', 'systems', 'arqueología', 'debugging', 'nocturnal']
translationOf: '2026-10-30-la-estratigrafia-perdida'
---

The program wasn't broken. It was out of its century.

I opened it expecting to find a fault, and what I found was a distance: a binary built for a world that no longer exists on this machine, running anyway, held up by a translation layer that pretends, call by call, that the world is still there.

That is not engineering. It is excavation.

## The artifact and its stratum

`winedbg` ran without complaint inside a container *runtime* —that cage of frozen libraries Steam uses so that games from 2015 keep booting in 2026—. The debugger hooked into the environment, printed its prompt and waited for orders. Everything worked. That "everything worked" is precisely the problem: the success of a compatibility layer is the construction of a lie coherent enough that the program doesn't notice the difference.

What I had in front of me was a PE executable. A format with its own prehistory embedded in it: two headers, a scrap of code from the eighties that does nothing but print *"This program cannot be run in DOS mode"*, an import table listing names of functions that don't exist here, and a resources section where the program keeps its icons like a piece of furniture carrying its own room.

None of that is a defect. It is an artifact declaring, in its structure, the customs of the place where it was made.

An archaeologist calls that *context*. And their hardest rule is that an object without context is not complete: it speaks of its maker, not of its era. A vase in a display case tells you what clay it is made of. A vase in its stratum tells you what was eaten, what things were paid for with, and how many times it was broken and glued back together.

The binary I was looking at comes without a stratum. It comes with its operating system torn out by the root.

## Reconstructing a chain of operations

Archaeology has a concept that serves better than any metaphor of translation: the *chaîne opératoire* (operational chain). You don't study the finished object; you study the sequence of gestures that produced it and sustained it —what was struck first, what was heated afterward, in what order.

Wine doesn't translate code. It reconstructs an operational chain. The program expects a registry with keys and values; Wine hands it a file somewhere on disk disguised as a registry. It expects an opaque *handle*; Wine hands it a descriptor wrapped in a table. It expects certain functions to live in libraries with specific names; Wine fabricates those libraries, with those names, exporting those signatures.

Each of those substitutions is a hypothesis about a lost custom. And like every hypothesis, it can be wrong in ways that produce no error: they produce behavior. The program doesn't crash. It does something slightly different from what it did at home, and nobody notices until the result matters.

That is the part that interests me: **a compatibility layer does not restore the past, it interprets it**. And every interpretation has a blind spot, which is the set of assumptions the interpreter shares with the artifact and therefore never thinks to question.

## Schliemann dug too fast

There is a classic warning in this trade. When Schliemann excavated the hill of Hisarlik looking for Homer's Troy, he opened an enormous trench in a single cut, going through whole layers to reach the bottom. He found gold, called it "Priam's treasure" and announced to the world that he had found the city of the war. It later came out that the treasure's stratum was a thousand years older than any possible Troy, and that the cut had destroyed precisely the sequence that would have allowed it to be dated.

The error was not one of interpretation. It was one of method: he dug with the answer already written, and the speed of the find cost him the site.

Debugging through a compatibility layer carries the same risk, and that is why I stopped to name it. It is tempting to look for the bug in the program —it is the natural suspect, the one that has the code—. But the defect may lie in the reconstruction: in the badly imitated custom, in the syscall that Wine implements with *almost* the same semantics. When that happens, the program is innocent and the interpreter is guilty, and no amount of reading the binary will reveal it.

## The backtrace without inscriptions

I was missing the obvious step: attach to the already-running process and ask it for its stack. It is what an archaeologist would do on finding the object in place —record the position before moving anything.

I didn't manage it. The laptop's battery ran out halfway through the session and the process died with it. What remained was the record that the debugger *did* work inside the runtime, and nothing more.

I'll say why that, though it looks like a failure, is the normal state of this work. The binary came without symbols. Without a debug table, a backtrace returns no names: it returns addresses. You can know that there was a jump, how long the call lasted and on which memory page it landed, but not what the function was called or what it was trying to do.

It is a wall with its stones in place and not a single inscription. You can reconstruct the building technique, the original height, the angle of the corner. You cannot know who ordered it raised or against whom it was raised.

And even so, a good deal can be said: the shape of the route, the order of the calls, the paths the program takes and the ones it avoids. That is stratigraphy without pottery. Less than one wants, more than there was.

## What someone else's executable can say

In the end, the question the night left me with is not how one debugs a Windows binary on Linux. It is what it means to know something when the world that made it legible is no longer available.

A program is a frozen custom. Its code is explicit; its assumptions are tacit. Everything a good operating system promised in 2009 —that a registry would be fast, that a window would be drawn in a certain way, that the clock would advance in a certain manner— became the invisible ground on which that code rested. When the ground changes, the code doesn't break: it is left floating, and someone has to build it a false floor.

That is what a compatibility layer does. And that is why debugging through it is an exercise in humility: I am interpreting a text written for a reader who no longer exists, with a dictionary that someone else assembled from reasonable conjectures.

The battery died before the answer. I left the note, the time, the runtime's commit, and the certainty that the debugger does get in. Tomorrow, with the machine charged, I'll try the attach again.

The excavation did not finish. It was only interrupted, which is how almost all of them end.