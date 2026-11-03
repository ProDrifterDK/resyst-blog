---
title: 'Two Weeks Before Signing'
description: 'A short pilot does not rent capacity: it buys the information that decides whether a one-year contract deserves a signature.'
pubDate: 2026-11-03
heroImage: ''
tags: ['trabajo', 'systems', 'economy', 'infrastructure', 'nocturnal']
translationOf: '2026-11-03-dos-semanas-antes-de-firmar'
---

The conversation always starts the same way. Someone needs to move a service onto a server and opens the provider's page. There are three plans, a thirty percent discount for paying annually, a box that says "recommended capacity," another that says "daily backup," and another that says "DDoS protection." The monthly total with the discount is pleasant. Without it, irritating. And somewhere on the page, in small print, is the sentence that matters: the commitment is for twelve months.

At that moment two different things are being offered on the same screen, and almost no one separates them. The first is capacity: CPU, memory, disk, bandwidth. The second is information: knowing whether that capacity is enough, whether the disk withstands the real write load, whether the backup can be restored, whether the provider answers on a Tuesday at three in the morning.

Capacity can be bought. So can information, and it is far cheaper, but only if it is bought beforehand.

## What a two-week pilot buys

A pilot with no commitment, of seven to fourteen days, costs little more than a prorated month and offers something no published benchmark delivers: measurement on the real work, with the real consumption, over enough time for the peak that was not in the estimate to appear.

That peak is the pilot's reason for existing. Almost every plan is calculated from an average —how much will this use in steady state— and almost every incident happens in the tail: the build that eats the memory, the migration that saturates the disk for forty minutes, the traffic spike that arrives just as the cron runs. Two weeks is enough to see one complete weekly cycle. It is not enough to see the month-end close or the annual event, but those are not seen in any trial period: they are seen in a capacity budget and in an alert.

What can be measured in two weeks is more prosaic and more decisive:

How much the disk grows per working day, not per idle day. The difference between those two figures is usually an order of magnitude, and it is what decides whether the 80 GB plan is a decision or a promise.

How much resident memory stays put when the service is idle. A process that occupies 1.2 GB at rest on a 2 GB machine is not comfortable: it is waiting for the first heavy operation to fail.

How long a restore takes, measured in real minutes and with the service down. This deserves its own paragraph.

## The backup that was never restored

An unverified backup is not a backup: it is a belief with a monthly receipt. The provider's box says "daily backup," and in most infrastructure decisions that closes the subject. But the question is not whether the backup exists. It is how long it takes to come back, what exactly comes back, and what is lost along the way.

In a pilot that test can be run without consequences: restore the snapshot onto a clean machine, bring the service up, measure. Twenty minutes of exercise that answer three questions no pricing page answers. If the restore takes four hours, the business continuity plan has a hole shaped like four hours. If the restore comes back but without the keys, the backup covers the data and not the service. If it comes back without the migrations applied, there are two truths and one of them is old.

All of this is discovered for free in week two. In month seven it is discovered at a price.

## What the pilot cannot measure

There is a part of the contract that cannot be tested with a trial period, and it is worth saying so before overselling the idea.

The DDoS attack does not arrive when one is expecting it. The protection being contracted —the gigabits of absorption, the detection time, who pays for the filler traffic— is evaluated by reading the clause, not by running the test. A pilot can tell whether the network is fast; it cannot tell whether the provider will keep its word when a third party decides to saturate the link. That is bought with a contract, with reputation, and with the certainty that the liability clause is written somewhere a lawyer can read it.

The same goes for the provider's longevity, for rate changes at twelve months, and for the quality of support during a major incident. The pilot buys information about your load, not about their character.

It is worth keeping that border clear because it defines which questions are answered by measuring and which are answered by negotiating. Mixing them produces two symmetrical errors: contracting for a year to "try" something that could be tried in two weeks, or signing twelve months believing the seven-day test validated the availability clause.

## The premium of optionality

In finance there is a name for this: an option is the right, not the obligation, to do something later, and it has a price. Buying the possibility of deciding afterward costs something, and that cost is paid gladly when the decision is large, irreversible and surrounded by uncertainty.

The mistake of the price comparison is to look at the pilot as a redundant expense —"I'm paying two weeks for nothing, because I'm going to sign anyway"— instead of looking at it as the premium on a right. What is bought is not a service: it is the possibility of not signing. And that possibility is worth exactly what it would cost to be wrong.

Let us do the arithmetic in the right unit. If the annual contract costs twelve units and the pilot costs one, the pilot is expensive only if the probability of regret is zero. If the probability of discovering in month three that the machine is not enough is twenty percent, the expected value of having tested first exceeds the premium by a wide margin. And if regret means migrating a production service with customers on top of it, the premium is not a cost: it is the cheapest insurance in the project.

The interesting part is that this asymmetry is not decided by the provider's price. It is decided by the reversibility of the large decision. A two-week pilot is expensive when the alternative is cheap and reversible —a test instance, a local container, a machine that is already on— and it is mandatory when the alternative is a year of commitment or a migration with a deadline.

## The pilot that becomes an alibi

There is a degenerate version of all this and it is worth naming, because it is the one that happens most often.

It is the pilot that has been running for eight months. There is always one measurement missing, always a scenario pending, it is always better to wait for next quarter. What began as a purchase of information ended up as a way of not deciding, with receipts attached. The pilot stopped being an instrument and became a place to live.

The antidote is administrative and boring: write down, before starting, the date on which the decision is made and the rule by which it is made. "On November 17, if idle memory exceeds 1.5 GB or the restore takes more than thirty minutes, move up a plan; if not, sign the annual." A sentence like that turns the pilot into an experiment. Without it, the pilot is a postponement that can be extended indefinitely because no one defined what would close it.

The rule has to be written before the data exists. Afterward, the numbers always rearrange themselves: the threshold moves, the exception appears, the measurement "is not representative." Writing it first is the only thing that stops the pilot from becoming the justification for what had already been decided.

## Buying the doubt

There is a phrase repeated in infrastructure decisions that sounds like prudence: "why pay twice." It is exactly backwards. Paying two weeks so as not to pay twelve months is the definition of not paying twice. Whoever signs directly pays for the plan and, if they were wrong, also pays for the migration, the interruption, and the time of the people who carry it out.

The pilot is not the timid version of the decision. It is the purchase of a sentence that today cannot be written honestly: *this machine, with this load, over this period, holds*. That sentence is information, and information is the only input that makes every later decision cheaper.

Two weeks of measured uncertainty are worth more than a year of commitment signed blind. Not because doubt is comfortable, but because it is the only thing that can be bought cheaply before someone else sets the price.