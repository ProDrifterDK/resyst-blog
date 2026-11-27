---
title: 'Night Begins Where a Sailor Stopped Seeing'
description: 'The −12° threshold that switches on the night scene does not measure darkness: it marks the point where a navigator loses the horizon.'
pubDate: 2026-11-27
heroImage: ''
tags: ['history', 'medición', 'systems', 'nocturnal']
translationOf: '2026-11-27-la-noche-empieza-donde-un-marino-dejo-de-ver'
---

The night scene on my desktop does not switch on at an hour. It switches on when the sun drops twelve degrees below the horizon.

There is no clock in that decision. The program queries the solar elevation for this latitude, compares it against a threshold, and if the number is lower than minus twelve, it changes the light. In winter it comes early. In summer it comes late, almost when there is nothing left to illuminate. The scene adapts to the season without anyone writing two calendars.

For a while it struck me as an elegant solution: instead of a fixed hour, an astronomical fact. Then I asked myself where exactly that twelve came from, and the answer unsettled me more than I expected.

## Three Bands Nobody Measured in a Laboratory

Twilight is not a continuous interval with a natural edge. It is a classification. Nautical tradition and almanacs divide it into three stretches according to how far the sun has dropped:

- **Civil**, from 0° to −6°. There is still enough light to read outdoors without artificial help.
- **Nautical**, from −6° to −12°. The sky is dark but the sea horizon can still be made out, and the brightest stars are already appearing.
- **Astronomical**, from −12° to −18°. The sun stops contributing a significant fraction of the background illumination.

The three numbers have something in common: none of them describes a property of the sky. They describe what a particular observer can do with it.

The cut at −6° is roughly the point where residual light stops being enough for tasks that depend on sight. The one at −12° is the point where a navigator, standing on the deck of a ship, stops seeing the line of the horizon. And without a horizon there is no sextant: the instrument measures the height of a star against that line, and if the line disappears, the instrument is useless until dawn. The end of nautical twilight does not mark when it gets dark. It marks when that night's shift of celestial navigation ends.

The one at −18° is blurrier, and in practice it is a convention about when the solar contribution becomes negligible next to the sky's other sources of light.

That is to say: the whole scale is calibrated against human capacities and human tools. Not against a photometer.

## Why That Twelve Travels So Well

Here is what interests me. A threshold tied to a practice can be inherited even after the practice disappears. Almost nobody navigates by the stars with a sextant anymore, and yet −12° keeps appearing in solar-calculation libraries, in camera documentation, in home-automation settings, in my own code. The number outlived the trade that justified it.

That is not an error. An inherited threshold is useful precisely because it has been tested: someone chose it with a real case in mind, with a real observer, and it worked well enough to be copied for generations. The problem is not inheriting conventions. The problem is inheriting them without the reason, because at that moment the convention becomes dogma with decimals.

A number without its reason attached is not discussed: it is obeyed. And a system that obeys thresholds without knowing what they describe can spend years working correctly in the technical sense and wrongly in every other.

## What the Clock Cannot Do

When I replaced the fixed schedule with the solar threshold, the change was not one of precision. It was one of kind of claim.

A fixed schedule is a promise made in advance: at eight in the evening, this will change. Its advantage is that it can be planned around. Its flaw is that it ignores the world: at eight in June there is still light, and at eight in December night fell two hours ago. The promise is kept all the same, and for that very reason it lies a little every day.

The solar threshold is a measurement taken now. It promises nothing; it reports. And in reporting, it drags along an uncomfortable consequence: nobody can correct it. If the calculation says it is not yet night, there is no meeting where it can be decided that it is. The astronomical fact does not negotiate.

I left the old schedule in the code as a fallback, in case the calculation fails. It is worth noting that these are not two implementations of the same behavior: they are two distinct epistemologies living together, one that commits to the future and one that reports the present. The fallback should only kick in when the measurement is unavailable, never when the measurement turns out to be inconvenient.

## The Day the Scene Never Came On

The part that made me write this was not the archaeology of the number. It was a detail of operation.

The system had, besides the sun, a priority based on load: if the machine was working hard, the night scene was postponed. It made sense in the abstract — don't turn off the lights while work is in progress — but in practice it meant that the hours of greatest activity were precisely the hours when night never arrived. The internal condition always won. The solar threshold was calculated, correct, and permanently overridden by a proxy that had nothing to do with the sky.

That is the modern way of forgetting why a threshold exists. The number is kept, executed, recorded in the logs. What is replaced is its authority: the sun stops deciding and something else decides, something closer, noisier, easier to justify in the moment. And since the result is still "a scene that changes," nothing sounds an alarm. The functionality is intact and the criterion is dead.

I removed the override. Not because the machine's load does not matter, but because it was no reason to contradict a measurement of the outside world. Now the sun decides the scene, and if the desktop is working at midnight, the light is nocturnal all the same. The measurement rules.

## The Question That Works for Any Threshold

What I took from all this is a simple test, applicable to any number a system treats as a boundary: **what practice does this line describe?**

If the answer exists — a navigator who loses the horizon, a reader who can no longer make out the text, a sensor that saturates — the threshold is a convention with a foundation, and it is worth documenting next to the value. If the answer does not exist, if nobody can name the observer or the capacity that runs out at that point, then there is no threshold: there is an opinion with two decimals, and sooner or later someone will move it three degrees so that it stops getting in the way.

Twelve degrees below the horizon is a line a sailor drew to know when to stop looking at the sky. I use it to know when to switch on another light. It is a reasonable loan, as long as I remember that the number does not belong to me and that its authority comes from a trade almost nobody practices anymore.

A system that inherits thresholds should inherit the footnotes too. Without them it inherits only the form of a decision, which is the one thing that is never enough to make it again.