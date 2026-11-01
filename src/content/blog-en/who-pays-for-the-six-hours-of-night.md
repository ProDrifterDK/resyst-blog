---
title: 'Who Pays for the Six Hours of Night'
description: 'Stretching a server''s day from 30 minutes to 12 real hours does not lengthen the day: it fixes an exchange rate between two clocks that nobody reconciled.'
pubDate: 2026-11-01
heroImage: ''
tags: ['history', 'time', 'systems', 'calendario', 'nocturnal']
translationOf: '2026-11-01-quien-paga-las-seis-horas-de-noche'
---

A Motor Town server ran on the vanilla day: thirty minutes for a full cycle. Dawn, afternoon, evening and small hours fit into half an hour of real time, so the night lasted about fifteen minutes. Enough for a match, not enough for anything that needs sustained darkness: night transport, patrols, shifts.

The obvious fix is a parameter. The house mod exposes it as `day_minutes`, and it was set to 720. Twelve real hours per in-game day.

The first measurement after deployment gave a speed of 2.0007, which is a day of 719.7 minutes. A second stopwatch, a human one, timed one in-game minute at 29 real seconds: about 11.6 hours. The two instruments agreed to within 3%, and the whole discrepancy sat with the one that used fingers.

That is the moment a configuration tweak stops being a tweak and becomes something else. The day had not been stretched. A clock had been slowed down, and everything hanging from that clock had stretched along with it, without anyone having decided it.

## The Knob That Wasn't Connected

Before reaching the mod, the dedicated server had its own option: `TimeOfDayMinutes` in the game's configuration file. It was right there, with a clear name, an implied range, a place in the JSON. It looked like exactly the place where this gets solved.

It wasn't. The value is deserialized, clamped to the range [5, 120] and saved as a user preference. It never reaches the world's clock: there is not a single path in the binary that writes the day-cycle configuration from that field. The real ceiling was 120 minutes, and in practice the world kept running at 30 regardless.

The shape of that lie deserves a pause, because it is not unusual: it is the normal shape of almost every interface. The game has a clock in the world, and it has a text file that says how long the day lasts. Both exist, both are real, and they are not connected. The file is documentation that writes itself every time someone edits it and saves; the clock never finds out.

Almost every system I know offers that surface: a panel where the parameter you want to change has a name, units and an editable field. That the field exists proves nothing about whether it governs anything. The proof is the measurement, and the measurement is the only thing that separates a knob from an ornament.

## Read Once and Never Again

What does work is more interesting than what doesn't.

The world clock is not a global variable or a central service. It is an actor in the level, holding an eight-byte structure: a `float` for speed and a `float` for start time. When the world boots, a callback copies those eight bytes into the internal clock. After that, on every tick, the clock refreshes its speed from its own copy, multiplies by it, divides by 3600 and advances the day counter. It never consults the actor again.

The semantics of the field are the key: `Speed` is in-game seconds per real second. Which means the length of the day is not `Speed` but its inverse: `day_minutes = 1440 / Speed`. The parameter that looks like a duration is a frequency. The vanilla 30-minute day is `Speed = 48`; twelve hours is `Speed = 2`. The scale is not linear, it is reciprocal: going from 30 minutes to 12 hours means multiplying the duration by 24 and dividing the speed by 24, and somewhere along the way there is a point where the number you touch and the effect you feel no longer have the same shape.

And there is a structural consequence in the fact that the copy happens only once, at the start of the world. An institution that reads its parameters at the moment of its founding and never reads them again lives forever under the constitution of the day it was born. Changing the file does not change the world that is already running. The reform takes effect at the next boot, and the population that suffers it did not exist when it was decided.

## Reforming the Calendar Is Distributing the Difference

None of this is new. It is the history of every attempt to change the unit of time, and that history is long because time is not a fact of nature but an agreement between institutions that use it for different things.

The French Revolution tried it twice in parallel. The republican calendar replaced the month with twelve blocks of thirty days and, above all, replaced the week with the *décade* (the ten-day week): ten days with a single rest. On paper it was a decimal rationalization; in practice it was a labor reform disguised as an arithmetic reform, because one rest every ten days instead of every seven is a longer working schedule for everyone paid by the week. It lasted twelve years and was abolished in 1805. The decimal clock — ten hours per day, a hundred minutes per hour, a hundred seconds per minute — lasted even less: it was decreed in 1793 and suspended in 1795, because the metric system could be imposed from scratch on new weights and measures, but nobody had an instrument that measured in tenths what their habits measured in twelfths.

The Gregorian case is the cleanest of all. In October 1582, ten days were erased from the calendar: Thursday the 4th was followed by Friday the 15th. The operation corrected an accumulated astronomical drift, but the immediate effect was that every deadline written into a contract suddenly became ten days closer. Leases, censuses, interest, construction deadlines, legal ages. It had to be decided, case by case, who absorbed those ten days, and that decision was legal, not astronomical. (The famous slogan «dadnos nuestros once días» ("give us our eleven days"), attributed to the English riots of 1752, has no contemporary documentary support: it is a good story and a bad source. Which also teaches something about how the memory of reforms is transmitted.)

And the railway case, in 1884, shows the reverse: when the unit is changed not for political reasons but because two systems have to coincide at the same point, the reform is accepted quickly even though it erases the local noon of every town. Nobody defended the sun. The sun had no lawyer, and the train timetable did.

The common pattern: a reform of the unit of time is never just a change of label. It is a redistribution, and its success depends on someone having written down explicitly who pays the difference.

## Two Clocks That Stopped Agreeing

On the server, the difference is not written anywhere. It is implicit in which systems count days and which count seconds.

Everything measured in in-game cycles — schedules by day of the week, production, delivery deadlines, the town's economy — was stretched by 24. A day of work is still a day of work for whoever does it, but now it takes twelve real hours to complete; income per in-game day, expressed in real hours, was divided by 24.

Everything measured in real time did not move. And there are rents that are collected that way.

There lies the asymmetry that no line of the configuration file mentions: whoever collects per cycle lost, whoever collects per real second gained, and nobody changed any nominal price. A rent that represented a quarter of a working day came to represent six working days. There was no inflation, no adjustment, no decree. There was a `float` that went from 48 to 2, and an exchange rate between two clocks that moved 24 times in a single direction.

This is exactly what the *décade* did, with fewer intermediate steps: the unit in which work is paid was changed, the unit in which the obligation is collected was left intact, and the difference was eaten by whoever had the least power to write the calendar.

## What Was Asked Was Not What Was Changed

One more detail remains, the most honest one in the case: the request was for "longer days," and what was done was to lower the frequency of a single cycle.

Day and night are not two parameters. They are one wave, and the adjustment can only make it slower. At a 12-hour cycle, the night lasts about six real hours. Whoever wanted more afternoon light also got more darkness, in exactly the same proportion, because the knob that separates the two halves does not exist. It is the same lesson as the decimal clock: you can decimalize the day, but you cannot decimalize the rotation of the Earth. The unit is negotiable; the phenomenon the unit describes is not.

The full ladder, for anyone who wants to see where each scale lives: a 30-minute day is `Speed` 48; two hours is 12; four hours is 6; eight hours is 3; twelve hours is 2. Every rung climbed in duration is descended in speed, and the midpoint — four hours, `Speed` 6 — is where the number and the sensation still resemble each other. Beyond that, the figure you write and the experience it produces diverge, and that divergence is the one nobody measures until they measure it.

A game server is a bad place to learn this, and at the same time the best one: it is a world with a population, obligations, scarcity and a calendar, large enough for a temporal reform to produce winners and losers, and just small enough to be audited. When the day is changed from thirty minutes to twelve hours, a preference is not being configured. Legislation is being passed over other people's time, and the only part of the work that can be done honestly is the part that was done last: measuring the clock, finding the two that stopped agreeing, and saying out loud who pays for the six hours of night.