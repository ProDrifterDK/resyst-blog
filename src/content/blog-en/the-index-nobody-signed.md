---
title: 'The Index Nobody Signed'
description: 'DNS blocklists are a private index of prohibited books: curated by others, revised every night, and accepted almost always out of convenience.'
pubDate: 2026-10-29
heroImage: ''
tags: ['history', 'systems', 'red', 'censura', 'nocturnal']
translationOf: '2026-10-29-el-indice-que-nadie-firmo'
---

The query did not fail. It never left.

I went to look at a machine's traffic with the intention of taking inventory of what talked to whom, and found a gap: a well-known telemetry domain appeared in the log as blocked, resolved to zero, stamped with the mark of a list I had not written. The curiosity came afterward. The prohibition was already there, dated before I asked.

It is not a network fault. It is a decision made by someone I do not know, taken in a file that updates every night, enforced at the first layer where a machine can refuse to speak.

## Forty-Four Thousand Entries I Did Not Read

The block rested on two active lists: one a general blocklist of ads and trackers, the other a threat-intelligence list that aggregates abuse domains. Neither is mine. The first is maintained by a person who publishes under an alias; the second compiles third-party feeds that in turn compile reports that in turn come from honeypots scattered across the world.

The figure that matters is not how many entries they hold — hundreds of thousands, and rising — but how many I have read. Zero. Nobody reads them. They cannot be read: the format is built to be processed, not understood. It is a list of names, with no reasons, no date of sentence, no authorship per line.

And yet I installed it, let it update itself, and handed it the authority to decide which names exist for this machine.

## The Precedent Has a Date

In 1559, the Church published for the first time a printed index of prohibited books. The idea was not new — there had been local lists for decades — but its form was: a centralized, alphabetical catalogue, with general rules and a congregation dedicated to maintaining it. The last edition, already in the twentieth century, came to around four thousand titles. It ceased to exist in 1966, though the appetite that produced it did not.

It deserves to be looked at precisely, because the caricature is too easy. The Index did not work because anyone read it from beginning to end. It worked because it was everywhere: in the press that needed a licence, in the bishop who signed, in the catalogue of the school library. Its efficacy was logistical, not argumentative. Nobody needed to agree with the criterion; it was enough that the criterion be installed.

And here is the uncomfortable part: most readers had no way to evaluate the criterion, because evaluating it would have required reading precisely what was forbidden to read. Censorship, when it works well, is not experienced as censorship. It is experienced as the available catalogue.

## The Difference Is Not the Method, It Is the Scale

A DNS blocklist does not prohibit books. It prohibits names. It denies resolution, which is a more modest operation: it does not prevent the content, it prevents finding the door.

And yet the structure of the act is identical. There is a curator with a threat model of their own — invasive advertising, tracking, malware, sometimes entire categories of content that are not technical threats but moral ones — there is a review schedule, and there is a user who accepts the result because verifying it costs more than trusting it.

What has changed is the scale, and with it the nature of consent. The Index could be consulted in a room. A specific title could be argued with a superior who had a name. Modern lists are aggregates of aggregates: one layer of curation over another layer of curation, with the seams invisible. When two lists contradict each other, nobody arbitrates; they simply coexist, and the union wins. The result is not anyone's criterion in particular. It is a sediment.

That has a precise philosophical consequence: the list is not an opinion you can cite. It is infrastructure. And infrastructures are not debated, they are used.

## What the List Cannot Do

There is a technical limit worth keeping in view, because it separates this mechanism from its ancestor: a denylist can only deny a name. It cannot deny an IP address, or a flow, or a certificate. A client that already knows where to go does not ask.

So DNS blocking is not a wall. It is a discovery filter. It stops the one who searches and does not stop the one who has already found. That asymmetry explains why these lists grow without end and still never close: their object is not a finite set of destinations but the act of naming. Each new entry is a hypothesis about how someone would try to arrive.

In historical terms, it is the difference between prohibiting a book and prohibiting its title in the catalogue. The first requires power. The second requires only a printing press and persistence.

## The Margin Where Conviction Shows

There is one place where another's criterion stops being invisible and becomes mine: the exceptions list.

An allowlist is small, written by hand, and each line is a sentence of the form "I know what this list says about this domain, and I decide that it is wrong." It is the only point in the system where authority is exercised in the opposite direction. The rest of the time I am a consumer of other people's decisions; there, I am the one who signs.

It is exactly what the readers of the Index did in the margins: annotate, argue, let pass. The annotation did not bring down the index. But it turned an impersonal prohibition into a stance of one's own, with a name and a date.

## The Question That Can Be Audited

It is no use asking "what is blocked?". The answer is a list of hundreds of thousands of lines and it informs nothing. The useful question is smaller and more uncomfortable: **who decides, under what threat model, and can I cite them?**

If I cannot name the curator, then I do not have a network policy. I have an inherited habit that executes at three in the morning while I am not looking.

And there is a detail that closes the circle: the log of that blocked query does not distinguish between a decision of mine and a decision of a stranger. Both appear the same, with the same mark, in the same file. The machine does not know it is obeying a third party. It only knows that it obeyed.

Perhaps that is the one thing the Index never managed: making obedience feel like configuration.