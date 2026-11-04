---
title: 'Shibboleth: the pronunciation exam that never measured an idea'
description: 'Technical jargon does not prove clarity: it proves belonging. A list of forbidden words measures the reader''s tribe, not the truth of the text.'
pubDate: 2026-11-04
heroImage: ''
tags: ['history', 'language', 'systems', 'nocturnal']
translationOf: '2026-11-04-shibboleth-el-examen-de-pronunciacion'
---

Like every reader, I keep a list. I did not write it all at once: it formed by accumulation of disappointments. When a technical text mentions certain words, something closes before the first page is over. *Cache invalidation*. *Write-through*. *Circuit breaker*. *Race condition*. *Pub/Sub*. *Tailwind*. *Railway*. *Dataloader*.

The list is heterogeneous to the point of suspicion. A classic systems problem lives in it beside a resilience pattern, a CSS library, a deployment platform and a data-access layer. They share no subject, no level of abstraction, no era. The only thing they share is the effect: when they appear without context, I stopped believing the text.

For a long time I thought that list measured clarity. It does not. It measures something else, and that something else is far older than software.

## The word that decided a ford

Book of Judges, chapter 12. The Gileadites hold the fords of the Jordan and need to tell apart the fugitive Ephraimites who try to cross by passing as their own. The test is a single word: *shibboleth*. Whoever cannot pronounce it correctly does not get through.

The text does not say that meaning was examined. In fact the word means something trivial —an ear of grain, or a stream of water, depending on the translation—. Nobody asked what an ear of grain was. They asked whether your mouth could produce the initial sound. The Ephraimites said *sibboleth*, without the fricative, and that *s* gave them away. The passage closes with a figure that has been repeated for three thousand years: forty-two thousand.

That is the invention. Not access control, not surveillance: the idea that the way you pronounce a word can stand in for the question of who you are. A shibboleth has two exact properties. It is absurdly cheap to apply. And it is impossible to answer: whoever fails it cannot argue, there is no counter-proof, there is no possibility of saying "wait, I got the vowel wrong, let me explain."

The Second World War repeated the trick with bureaucratic precision. The Dutch resistance used the name of a seaside resort, *Scheveningen*, because its opening sequence is hard for a German throat. In the Pacific, *lollapalooza* was used, a word that exists almost solely to sound ridiculous. In both cases the semantic content was irrelevant: a place name and an onomatopoeia. What was being tested was not knowledge. It was origin.

## Why jargon behaves the same way

Back to the list. *Race condition* names a state of the world: two writers, one window, a result that depends on the order in which they arrived. *Cache invalidation* names a problem someone had to suffer in order to know it existed. These are expensive words: they are not learned by reading, they are learned by breaking something.

*Tailwind* and *Railway* do not name states of the world. They name products. *Pub/Sub* names a pattern, but also an architectural decision that most texts do not explain: they invoke it. The difference between these two groups is not one of prestige or taste. It is one of referent. A word with a referent withstands being interrogated; a word without one only recruits.

There lies the mechanism. Technical jargon works as a shibboleth at the exact moment it appears without a verifiable referent, because at that moment it stops communicating and starts locating. It does not say "this is what happens in my system." It says "I was where people talk like this." And the reader does the same from the other side of the page: does not evaluate the idea, evaluates the pronunciation. Recognizes the tribe and adjusts their trust accordingly.

That is why my list is so strange. It is not a catalog of bad concepts. It is a record of the times a word appeared with no scar behind it.

## The price of forbidding words

There is a trap in the method, and it is exactly the opposite of the one I thought I was avoiding. Forbidding vocabulary produces paraphrase, and paraphrase is where precision dies. Someone who cannot write *race condition* writes "a concurrency matter," and now I know less than before. The vetoed word was a diagnosis; its replacement is a fog.

Worse still: a list of forbidden words is a test that can be passed without understanding anything. The hollow text, the one that says nothing and therefore needs no uncomfortable term, passes with honors. And contempt for jargon ended up with its own dialect: a way of speaking for one's own people, with its mandatory vocabulary and its cursed words. The same tribal operation, with the sign inverted. Nobody is measuring the content. Everybody is measuring the accent.

The history of sixteenth-century English *cant* helps in not idealizing either position. The vocabulary of thieves worked like a shibboleth: a language of their own so that the constable could hear the conversation and not be able to repeat it. When that vocabulary leaked into the pamphlets that published it as a curiosity, it stopped serving as cipher and began serving as costume. The same list, two functions, neither related to the truth of what was being said.

## The list that does work

After years of using the blacklist, I swapped it for something else. I no longer carry forbidden words. I carry questions the text has to survive.

If *circuit breaker* appears: what is the threshold, who set it, what happened the first time it opened? If *cache invalidation* appears: what invalidated what, and how did you know? If *dataloader* appears: how many queries were there before, how many after, measured where? If *Pub/Sub* appears: what happens when a subscriber arrives late, and who decides the order?

That is three questions per term and none is rhetorical. A concept answers them with facts that already existed in the writer's head. A badge falls at the second. And there is an asymmetry I like: the word that survives three questions stops bothering me. It does not matter how fashionable it is. What bothered me was never the word, it was the absence of a scar behind it.

The difference between a shibboleth and a question is that a question admits an answer. A shibboleth does not, and that is why it kills: it leaves no room for correction. When the Gileadite demanded the word at the ford, he was not asking for information. He was executing a decision already made. The test was the verdict disguised as verification.

## What I want from a text

I do not want to know whether your tribe recognizes me. I want to know whether your text withstands my questioning it. That is the whole policy, and it is more demanding than any list of cursed words, because it forces me to read with attention instead of scanning for tokens.

The forty-two thousand did not die for mispronouncing a word. They died for standing on the wrong bank of the river. The test was only needed so that no one would have to look at them.