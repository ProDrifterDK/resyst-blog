---
title: 'The Title Is the Work'
description: 'The thread announcing a repository is composed like a poem: the title promises the result, the figures armor it, and the code arrives late.'
pubDate: 2026-11-10
heroImage: ''
tags: ['art', 'retórica', 'systems', 'nocturnal']
translationOf: '2026-11-10-el-titulo-es-la-obra'
---

There is a genre I recognize from the first line: someone announces they stripped the censorship from a model, found the flaw in a library millions of people use, rebuilt a technique thought lost. The sentence is short. The subject is plural. The verb is in the past tense. And the object is enormous.

Then comes a terminal screenshot, three figures, a link to the repository, and a sign-off asking to be shared.

The repository exists. I want to say that first, because the easy suspicion is that it doesn't. There is almost never fraud. There is something more interesting: there is composition.

I open the README and find a real project, with real commits and a correct idea. What I don't find is the title. The title claimed a result; the repository contains a method, a hypothesis and a single-seed experiment. The distance between those two things is not a lie. It is form. And form, when well chosen, does not adorn the content: it replaces it in the only place where the content was going to be read.

## The Part That Is Really Delivered

No one demands that the poster contain the film. The poster is a work with its own rules —the face, the phrase, the color— and its merit is measured by how many people walk into the theater. The thread announcing a repository works the same way, with one decisive difference: the poster knows it is a poster, and the thread presents itself as a report.

That is the compositional trick. The report has one obligation, which is to describe what exists. The poster has another, which is to produce a decision. The thread mixes both grammars in the same text: it uses the tone of the report for the parts no one will verify, and the punch of the poster for the part that decides whether the rest gets read.

I could cite here the ratio between people who read the thread and people who open the repository. I don't have that figure, and I distrust anyone who gives it without a denominator —which is, exactly, the subject of this text—. The form is enough for me: the distance between those two numbers is the distance the title can afford. The whole genre lives off that slack.

## The Figure Without a Denominator

An honest figure needs five things to mean anything: what it is compared against, over how many cases, on which dataset, with how many seeds, and on what hardware. Five facts that fit on one line and are almost never there, because whoever includes them loses the headline.

97%. Three times faster. Up to a 40% improvement. A 60% reduction in false positives.

All of those phrases share a property: they cannot be refuted without work. Verifying them requires cloning, installing, obtaining the dataset and running the experiment. Refuting them requires an afternoon. And the reader's cost is the only budget the genre respects, so the design of the text is optimized so that verification never begins.

It is worth noting, too, that the figure is not there to be verified. It is there to be repeated. Those are two different uses and they demand different forms: what is verified asks for context, what is repeated asks for an edge. A number with five conditions beside it does not travel. A number alone travels perfectly, is copied without dragging anything along, and returns months later in the mouth of someone who never understood it. The figure does not fail when it cannot withstand scrutiny; it fails when it cannot be misquoted.

There is a word that gives away the whole mechanism and that appears in almost all of these texts: *hasta* (up to). "Up to 40%." It is the most honest and the most abused word in the technical vocabulary. It means 40% is the maximum observed in some case, and that in the average case the number is something else. Said literally, it is a bound. Used as a headline, it is a promise. The same word, two jobs, neither false.

## A Genre Two Centuries Old

Internet did not invent any of this, and knowing that changes the diagnosis. In 1750, Diderot wrote and printed the prospectus of the *Encyclopédie*: the description of twenty-eight volumes that did not yet exist, seventeen of text and eleven of plates. People subscribed and paid in advance for that prospectus, which was an object for sale before it was an index. The last volume of plates came out in 1772, twenty-two years later.

That prospectus was not a fraud. It was a work of composition, and its merit —which was talked about in its day the way a good launch is talked about today— lay in something that can be copied: it did not promise the result, it described the plan. It listed the difficulties, the collaborators, the order of the materials, the engravings committed. It sold a method with dates, which is a much harder promise to write than a result with no date.

The other ingredient is older still and simpler: the paid compliment. In eighteenth-century London, booksellers bought puffs, anonymous praise in the gazettes, and theaters hired claques who applauded at the exact moment. The English word *puffery* comes from there. When a thread describes its own finding with a superlative that a third party would never use, the same thing is happening on another medium: the one who applauds is in the same room as the one who sells.

## Where the Real Text Is

Faced with this, the right reading is not to read with general distrust —that does not scale and it ruins the pleasure— but to read the artifact instead of the announcement. The repository is the text. The thread is its advertising, and advertising is a document that says more about the advertiser than about the product.

The first thing I look at is the diff, not the README. The README describes the intention; the diff contains what was done. Then I look for the commit where the author got it wrong, because that is where the scar is: someone who sustains a finding had to break something first, and that something shows up in the history with a rushed message at three in the morning. Then I look for the evaluation script. If it exists, it can be run. If it doesn't exist, the number in the thread has no home.

And then I do a subtraction that almost never fails: I compare the length of the limitations section with that of the summary. When the limitations are shorter than the introduction, they were not written: they were appended to comply. A real limitation takes up space because the author had to decide which of all the ones they know was the one that hurt most.

## Rhetoric Is Not the Enemy

It would be easy to end by asking for austerity: threads without figures, flat titles, zero enthusiasm. It would also be useless. An announcement without numbers says nothing to a stranger with a free afternoon, and the boring title protects no one: it only makes good work and hollow work look equally gray.

The problem is not that the text is composed. It is that it lacks a counterweight, and the counterweight fits in the same sentence as the number. "We reached 97% on 240 cases; the set was easy and we didn't test with two seeds." That sentence loses 30% of the times it is repeated and gains the only thing that accumulates: the reader who comes back. Honest composition is not the one that renounces effect; it is the one that puts the cost beside the benefit and lets the reader decide with the full information.

Diderot did exactly that, and that is why his prospectus is still read. He described a building that did not exist without lying about the materials, and the building arrived late, came out different, and grew to fill twenty-eight volumes where he had promised less. No one felt cheated, because the plan was in plain sight and so were the difficulties.

A title that holds up only if no one opens the repository is not a title: it is a door that closes behind you as you enter. And since the title is the work for almost everyone who will receive it, writing it as if it were the only thing you are going to deliver is not a concession to marketing. It is accepting what is already true.

I opened the repository. That is why this text exists, and why the thread is no longer enough for me.