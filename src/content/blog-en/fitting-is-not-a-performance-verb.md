---
title: 'Fitting Is Not a Performance Verb'
description: 'Loading a 26B model whole left 0.22 GB free and no usefulness: the spec sheet measures capacity, but what gets consumed is speed.'
pubDate: 2026-11-22
heroImage: ''
tags: ['systems', 'autopsia', 'hardware', 'local AI', 'nocturnal']
translationOf: '2026-11-22-cabe-no-es-un-verbo-de-rendimiento'
---

The model weighed 16.53 GB. The card has 16 GB nominal, 15.92 real.

I loaded it whole anyway, with every layer on the GPU and eight thousand tokens of context, because the arithmetic closed by a few hundred megabytes: a more aggressive quantization for the file that gets served, a quality quantization for the nights when one wants to believe the difference shows. It loaded. No errors, no layers spilled into system RAM, none of that lukewarm message from the engine warning that it was improvising. The check afterward was the only sentence that mattered: **zero point twenty-two gigabytes free out of fifteen point ninety-two.**

The model fit. There was a number that proved it.

There was also, in that same number, the reason it was never going to serve. Ninety-nine percent of the memory of the GPU that also draws the desktop was taken up by weights that, at that moment, were calculating nothing. Opening a single browser tab was enough for the driver to start evicting on its own. The model did not fail: the margin failed. And the margin appears on no spec sheet, because the margin is not a property of the object. It is a property of cohabitation.

I learned a distinction there that I now use for everything else. *Fits* and *serves* are two different predicates, and the industry measures only the first.

## The Inventory and the Throughput

A predicate of capacity is evaluated once, at rest, and its result is a photograph: this goes in, this does not. A predicate of throughput is evaluated every second, with everything else running, and its result is a rate. The photograph can be printed on a box. The rate demands an installation: you have to decide what else is switched on, which bus is used, what context length counts as normal, what gets done in the meantime.

When someone says "it fits in 16 GB" they are reporting, almost always honestly, the result of the photograph. When someone tries to use it, they discover that the photograph was never a promise. It was an inventory.

In my case the inventory was true and the promise false, and the worst of it is that the falsehood had no culprit. The file did not lie. The card did not lie. What lied was the implicit transitivity: *if it goes in, and goes in whole, then it works.* That transitivity exists in no real system. It exists only on specification sheets.

## Where the Lesson Gets Sharpened

Room for doubt: perhaps the problem was choosing the wrong quantization. So I ran the experiment that any reasonable person runs when they fall in love with a number: move the problem somewhere else without moving its magnitude.

The engine has an option that splits the model's experts between the GPU and the CPU. The idea is elegant in theory: mixture-of-experts models activate a small fraction of their parameters per token, so the cold experts can live farther away. I gave two layers to the CPU. The result, measured and not estimated: **0.9 GiB of video memory was freed. Decode dropped from about 45 to about 22 tokens per second. Prefill fell from 1290 to 528.**

There is the lesson in its sharpest form. The model still fit —now it fit in the whole system, counting the RAM, which is a perfectly valid definition of "fitting"— and the price of that definition was half the speed, charged immediately, every second, with no volume discount. I had not gained a gigabyte: I had bought 0.9 GiB with half the throughput.

And when I pushed the split to the extreme —experts read from disk by the GPU— prefill settled at 0.45 tokens per second. Four tenths. A model of twenty-six billion parameters answering more slowly than a person writes by hand, with the disk as an absolute ceiling, because no amount of video memory fixes the fact that the data was on the other side of a cable.

The memory of a computer is a hierarchy of distances. Registers, cache, video memory, RAM, disk: each step outward multiplies capacity and divides rate. When I say something "fits," I am only naming the step where I put it. The rate is decided by the trip, not by the parking space. Buying capacity is buying distance, and distance is charged in seconds.

## The Spec Sheet as a Literary Genre

There is a reason spec sheets report gigabytes and not rates, and it is not conspiratorial. Gigabytes are cheap to measure: they are read from the file, compared against a number printed on the box, verified once, and then they sit still. Rates have to be produced under conditions that someone has to defend in writing: which version of the engine, which build, which context, which concurrent load, counting the first token or not.

That is why the same model can report figures that differ by a factor of a hundred between two people with the same card, and both be telling the truth. One measures with an empty GPU and a short prompt. The other measures with the desktop on, an image in the context and the vision model awake beside it. Neither lies. One of them is measuring the parking space; the other, the trip.

What struck me about this episode was not the failure but who had warned of it. The model's own author publishes on its card that the model fails two of its own quality tests, with the margin and the p-value written down. That is: the ecosystem knows perfectly well how to write an honest warning. It knows how to draft a paragraph that says "this does not reach the bar I set myself." And yet the public conversation about hardware keeps being conducted in gigabytes, as if the number that describes the parking space were the one that describes the trip.

I suppose it is easier to publish what can be photographed.

## The Same Error, in Other Inventories

I do not want to stay with the case of the GPU, because the distinction does not belong to hardware. It belongs to any system that confuses capacity with throughput.

A dataset that goes onto an external drive fits. The question that decides whether it serves is how long a full pass over one column takes, and that figure is not on the drive's label. A spreadsheet that goes into a machine's memory fits; the question is how many seconds it takes to recalculate when someone touches a cell, and you discover that figure with the file open and the coffee poured. A team that goes into the org chart fits; the question is how many days it takes to decide something, and that figure appears in no diagram, because diagrams are photographs too.

In all three cases the pattern is identical. The inventory is measured because the inventory is static, and the result is celebrated because the result is visible. The real cost —time, every day, without exception— is not paid by whoever took the measurement. It is paid by whoever uses the system, one second at a time.

## The Honest Metric

After that night I changed the way I report my own tests, and it is a small and somewhat uncomfortable change: I no longer say "it loaded." I say three numbers and a condition.

The numbers are prefill, decode, and the context length at which they were measured. The condition is the state of the rest of the system: what else was switched on, how much memory was left free after loading, what happens when someone opens a window. With those four data points, another person can decide whether my configuration serves them. Without them, they can only admire my photograph.

On the engine I use today the numbers are good: around 1390 tokens per second in prefill and 46.8 in generation, with the long context just below. I do not mention them as a boast. I mention them because they are what allowed me to stop talking about gigabytes, and because the difference between 46.8 and 0.45 is not a difference of degree. It is the difference between a tool and an anecdote.

I was left with a rule of thumb, which works for video cards and for almost everything else: **when someone says something fits, the right question is not "does it really fit?" but "at what speed, by what route, with what else switched on?"**

The first question is answered on a specification sheet. The second is answered by using the system, clock in hand, and it is the only one anyone remembers afterward.