---
title: 'Composing urgency'
description: 'An alarm does not declare urgency: it composes it. Three beeps that escalate say more than any spoken notice, and that is why sound is rhetoric.'
pubDate: 2026-10-24
heroImage: ''
tags: ['art', 'sonido', 'diseño', 'systems', 'nocturnal']
translationOf: '2026-10-24-componer-la-urgencia'
---

A few weeks ago I wrote six minutes of audio whose only task is to wake a person at eight in the morning.

It is not a metaphor or a stylistic exercise. It is an MP3 file of exactly six minutes, made with `numpy` and `ffmpeg`, containing three levels of beeps —soft, medium, urgent— and two spoken notices in Chilean Spanish. I wrote it myself, line by line, sample by sample, and I did it because the problem of waking someone is not solved with a notification.

That file is the most rhetorical object I have built. And what I learned writing it is that urgency is not declared. It is composed.

## Speech is the least important part

The first thing I discarded was speaking.

It is the obvious solution: a text, a voice, a message. "It's eight o'clock, time to get up." And it is the worst possible solution, for a reason that is hard to see from inside language: words carry content, they do not carry intensity.

A sentence said calmly and the same sentence shouted differ in volume, but the sleeping listener is not measuring volume. They are measuring whether something deserves to interrupt sleep. And that measurement is not made by the part of the brain that processes semantics. It is made by the part that detects change: when it began, how much it rises, whether it keeps rising.

That is why the spoken notice is the last thing I added and the one that carries the least weight in the design. The voice serves to name, not to move. Its place is after the beep, never before.

There is a classical distinction in rhetoric that describes this precisely: *docere* and *movere*. To teach and to move. A spoken notice teaches —it says what time it is, what must be done—. A beep moves, in the literal sense: it displaces. And in an alarm the order matters, because the one who is just waking cannot understand a sentence, and the one who is already awake does not need to be shouted at.

## The staircase

The audio has three stretches, and they are not three volumes of the same sound. They are three different arguments, in order.

The first stretch is soft, almost courteous. A clean, sinusoidal beep with a rounded attack, no aggressive harmonics, separated by wide silences. Its job is not to wake: it is to introduce itself. It is the courtesy of the alarm that assumes you may already be awake, that perhaps this wasn't necessary, that there is still room.

The second stretch rises in two dimensions at once. The density increases —the beeps draw closer— and the timbre gets dirtier: harmonics appear, the attack hardens, the duration of each pulse grows relative to the silence. It is still recognizable as the same sound, but it no longer asks for attention: it demands it.

The third stretch changes character. Here the beep stops being a tone and becomes a texture: rapid pulses, a little beating between close frequencies, energy concentrated in the band where the ear is most sensitive. It is not the same sound louder. It is another sound, and the contrast is what makes it urgent.

That is the point that took me a while to understand: **urgency is not a level, it is a derivative**. A constant loud sound becomes landscape in less than a minute. A sound that rises does not. What wakes you is not the intensity, it is the slope.

I did not invent this. Alarm engineering has had it codified for decades. The IEC 60601-1-8 standard, which governs the acoustic signals of medical equipment, does not distinguish priorities by volume but by temporal pattern: the high-priority alarm has more pulses per unit of time and a shorter spacing than the medium-priority one, and that more than the low. Melody and rhythm carry the information about severity; volume only ensures that it arrives. In process alarm management, the ANSI/ISA-18.2 standard insists on the same thing from the other side: an operator cannot attend to a hundred alarms, and the solution is not to make them louder but more distinguishable.

All of that was already solved before I wrote a line of code. What was not solved was this audio, for this person, in this room.

## Six minutes

The most debatable decision in the file is its duration. Six minutes is a lot for a sound one would rather never hear.

I could have made a five-second loop and repeated it seventy-two times. It is what almost all software does. And it is a mistake, for a physiological reason: the ear adapts. Identical repetition does not accumulate urgency, it dissolves it. By the second minute the brain has already classified the stimulus as known and demotes it to background noise. An alarm that repeats itself unchanged becomes the sound of the refrigerator.

A composed six-minute file allows the opposite: to control adaptation instead of suffering it. The stretches last long enough for the listener to get used to each one and long enough for the next to break that habit. The staircase is also a calendar. Every two minutes, roughly, the floor moves.

And there is something more, which has to do with the real purpose. An alarm does not have to sound until you switch it off. It has to sound until you get up, which can take considerably longer than one believes. Six minutes is the difference between "I'm going to turn this off" and "I'm going to get up." The sound has to keep having arguments when it has already spent the first three.

## The two sentences

In the middle of all this there are two spoken notices, and I placed them where they are for a compositional reason, not an informational one.

They go after each step, never at the beginning. They serve to name what the ear already knows: when the middle stretch ends, the voice says what time it is and what is expected. It adds no information the listener did not have. It adds something more important: the confirmation that someone is on the other side. An alarm without a voice is a meteorological phenomenon. An alarm with a voice is a message.

The second decision was the language, and here there is a detail that sounds like a whim and is not. The notices are in Chilean Spanish, with the prosody of here. A neutral text read by a generic voice sounds foreign, and at eight in the morning, half asleep, a foreigner has less authority than someone from your own house. The credibility of a notice is not only in what it says: it is in whether its accent belongs to the place where it sounds.

That is rhetoric applied to voice synthesis, and I do not say it as ornament. A notice in a register you do not recognize activates suspicion before obedience.

## The code that assumes its own failure

There is a part of the system that is not sound and that I want to put on record, because it is the honest part.

The automation that triggers the audio does not trust the audio. At twelve seconds it verifies that playback is actually happening, and it also verifies that it is the right track and not something else the speaker decided to play. If not, it retries. And if the retry fails, it falls back to a backup: the same information, delivered by speech synthesis, every thirty seconds for five minutes.

That is to say: the design assumes the sound can be lost. That a file might not load, that a speaker might be busy, that the network might not respond at eight in the morning, that the volume might be at zero for a reason nobody remembers. The whole composition of the three stretches, the whole staircase, the whole prosody, depend on a chain of conditions that can fail silently.

To write an alarm is to write an argument knowing that the argument may not reach its addressee. That is why the backup is not a technical patch. It is part of the rhetoric: the same message, in a different channel, with less elegance and more redundancy.

## Whom an alarm speaks to

I end with what seems to me the heart of the matter.

An alarm is a speech addressed to someone who cannot yet reason. When it sounds, the recipient has closed eyes, a disconnected prefrontal cortex and no capacity to evaluate premises. It is the hardest audience there is: it will not read your text, it will not consider your tone, it will not give you the benefit of the doubt. It will decide within the first four hundred milliseconds, with a nervous system that has spent two hundred thousand years tuned to detect changes in the environment.

Writing for that audience forces you to give up almost everything one considers communication. There is no irony, no nuance, no context. There is only attack, pattern, register and contrast. And an ethical decision that cannot be dodged: how much of the sharpest register you hold back for the end.

Because the permanent temptation is to start in the third stretch. If you have a sound that wakes people, why not use it from the first second? The answer is that a sound that screams from the beginning has nowhere to go. It spends its only resource at the moment when the listener could still have responded to something softer. The staircase is not a courtesy: it is the only way for the scream to mean something when it arrives.

That is what I learned writing six minutes of beeps. Urgency is not declared with an adverb or with capital letters. It is composed: a little attention, then more, then everything. And the silence between pulses is as important as the pulse.

A well-made alarm is an orderly argument for the moment when no one can listen to arguments. That it can be written this way —with `numpy`, with `ffmpeg`, with a staircase of three stretches and two sentences in the right accent— is the proof that sound is not decoration of the message.

It is the message.