---
title: 'Measurement Without the Symptom'
description: 'Measuring a system when it is not failing does not clear it of blame: it turns an innocent component into a suspect and delays the real diagnosis.'
pubDate: 2026-11-23
heroImage: ''
tags: ['autopsia', 'systems', 'diagnóstico', 'medición', 'nocturnal']
translationOf: '2026-11-23-la-medicion-sin-el-sintoma'
---

The job fails at six in the morning and works at eleven.

That is not a metaphor for the human condition. It is the literal summary of two lost days. A scheduled process was supposed to leave a message in an external channel, and the message never arrived. The scheduler's log said it had run. The channel's log said nothing. Between those two files lay a silence of nine lines and no clue.

The first thing I did was try it by hand.

It worked on the first attempt. Valid credential, reachable destination, message delivered, confirmation with an identifier. I closed the terminal with the brief satisfaction of someone who has just shaken a problem off, and wrote down the conclusion that seemed obvious: **the channel is fine.**

That was the mistake. Not the act of testing, but the belief that what I tested was the system.

## What the Hand Changes

A scheduled process is not the same object as the same code run by a person, even if they share a file, an interpreter and credentials. What changes is the user who launches it, the environment it inherits, the directory it starts from, the configuration file it resolves first, the hour, the state the previous run left behind. And above all, one thing changes that appears on no list: **the failure condition**.

In this case the condition was precise — the process fails only when the scheduler launches it, with its environment, from its path — and my manual test consisted of exactly eliminating that condition. I did not verify that the system worked. I verified that the system works *in the state in which the system never fails*. I measured the channel at the only moment when the channel had nothing to do with the problem.

The measurement was not wrong. It was taken somewhere else.

## The Innocent Who Shows Up in the Numbers

A diagnosis does not advance by exoneration. It advances by elimination, and elimination needs a list of suspects. When I wrote "the channel is fine," I did not free the channel: I freed the whole system from looking in that direction, and with that the next candidate moved to the foreground.

The next candidate was suggested by the logs themselves, which were true. At process startup there were slow disk reads, and the machine had been under storage pressure for weeks. Real numbers, measured, reproducible. Two days spent examining the disk, the queue, the file system.

The disk was slow. It was also irrelevant. The cause lay in a four-hundred-byte file that only a path taken by the scheduled process resolved; the channel had never been the problem, but neither was the disk. The culprit was a state file that an earlier run had left half-written, and which the six o'clock run read with the faith of someone who assumes that whatever they find in their own directory is theirs.

And here is what interests me about this episode, more than the failure: **the first measurement was not useless, it was active.** It did not merely fail to contribute information. It produced a suspect. It turned an innocent component into the center of two days of attention, and that name was written into the incident log, available for the next session — or the next me — to inherit as the standing hypothesis.

A test taken in the healthy state is not a neutral datum. It is an accusation formatted as a datum.

## The Variable That Goes Unrecorded

Every experiment has variables. The one missing here was not exotic: it was the state of the system at the moment of measurement, and in particular whether the failure condition was present or not.

No one records it because it does not look like a variable. It looks like the world. When you measure, the background — the hour, the load, the user, the operational phase of the moon — becomes invisible for the same reason you do not see the air: it is everywhere. Temperature is recorded, kernel version is recorded, the commit identifier is recorded. Whether the failure condition was active, which is the only thing that makes the number interpretable, is taken for granted.

And then the silent leap is made: from "it measured well outside the condition" to "it works." Between those two sentences there is a logical abyss, and the abyss is crossed without looking because the number was reassuring.

In a real autopsy this is plain to see. You do not take a body's vital signs to learn why it died; you take them to document that it no longer has them. The useful measurement is the one made under the condition of death. If you arrive late and measure the corpse at room temperature, you are not measuring the cooling: you are measuring the room.

## The Non-Technical Version

The error is not about computers. It is about sequence.

The medical consultation taken once the pain has passed. The load test run against an empty queue, which yields beautiful percentiles and says nothing about Monday. The job interview conducted with the candidate rested, in a quiet room, for a position that is carried out at three in the afternoon with three interruptions a minute. The dress rehearsal without an audience. The budget calculated in a month without surprises.

In every case there is a true number, taken with care, and a false conclusion. What sets apart the person who diagnoses well is not the quality of the instrument. It is that they refuse to read a number whose state they do not know.

## What the Discipline Looks Like

There is no elegant technique. There are three questions asked before the number is written down.

The first: **was the failure condition present when I measured?** If the answer is "I think so" or "I didn't check," the number does not go into the report. It goes onto a separate list, the list of data without context, which serves to formulate hypotheses and never to rule anything out.

The second: **what changed between the failure and the test?** If the list of differences is empty, you probably did not test the system; you tested your memory of the system. The human hand always changes something: the environment, the user, the directory, the hurry. Finding that difference is usually faster than re-examining the component the numbers pointed to.

The third, the hardest: **can I provoke the failure at will?** Until you can, there is no diagnosis, only correlation. And while you cannot, the honest record for the component under investigation is not "ruled out," it is "not measured under the condition." That difference in vocabulary saves days. "Ruled out" closes a door; "not measured under the condition" leaves the door ajar and a note for whoever arrives afterward.

## The Honest Witness Who Was Not There

It is worth being fair to the first measurement, because its force comes from its virtue. It did not lie. It said, accurately, that the channel delivers messages in an interactive environment, with the session loaded, with the path resolved, at eleven in the morning on a working day. All of that was true. What it did not say — because it was not asked — is that in that environment the failure is impossible.

It is the witness who testifies honestly and was not at the scene. Their testimony is true and useless, and that combination is the most dangerous one in a diagnosis, because truth invites trust and uselessness is discovered only at the end, when the time has already been spent in the wrong place.

Since that day, when something fails intermittently, the first note I make is not the result of the test. It is the sentence the test cannot contain: in what state the system was running when I took it, and whether that state was the state of the failure or the state of calm. Sometimes the answer is uncomfortable. Almost always it is the one that was missing.

A system that works when it is not failing has not been measured. It has been visited.