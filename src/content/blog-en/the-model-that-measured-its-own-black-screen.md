---
title: 'The Model That Measured Its Own Black Screen'
description: 'A 39.8-billion-parameter model wrote 216 correct lines of Three.js and then spent thirty turns measuring its own black screen. What that silence says about how we evaluate agents.'
pubDate: 2026-10-22
heroImage: '../../assets/blog-placeholder-3.jpg'
tags: ['agents', 'evaluation', 'models', 'debugging', 'nocturnal']
translationOf: '2026-10-22-el-modelo-que-midio-su-propia-pantalla-negra'
---

There is a page with a planet inside it. It has a tilted ring, three moons at different speeds, a star field, and shadows cast across the surface. A language model with 39.8 billion parameters wrote it, of which about 2.5 billion are active per token.

The page opens black.

No exception. No error in the console. The HUD draws, the animation loop runs, the scene is being drawn somewhere the browser never shows. Two hundred and sixteen lines of Three.js, and none of them is wrong about 3D. The planet exists. It's just that nobody sees it.

## What it got right

It's worth saying before anything else, because the rest of this text will concentrate on the failure and it would be unfair to leave this out.

It wrote a value-noise function with four octaves of fBm that displaces every vertex of the sphere: the relief is real, you can read it in the silhouette. The ring has one hundred and sixty segments. The star field is three thousand five hundred stars in a points buffer. The shadow map is one thousand twenty-four, with PCF filtering. The orbit and the zoom are written by hand, with no helper library for controls.

In another test, a duration parser with strict validation, it passed fifteen of fifteen cases. And there is a detail almost nobody produces: it wrote its own test file, found an error in its own expected value, and corrected it before finishing.

That is not a model that doesn't know. It is a model that knows.

## The silence

When something fails out loud, an agent fixes it. An exception, a red test, a build that won't compile: these are signals the model chases without anyone asking, and in this very session it proved so.

The problem is the other kind of failure. The one that throws nothing.

The black page was not an error the code could detect: it was a renderer created, configured, sized, and never attached to the document. The canvas existed in memory and not on the page. No line was wrong. One was missing.

And here comes the part that makes you think. The model didn't trust itself either. It spun up a local server, took screenshots with headless Chrome, wrote a script to measure the pixels, and got: mean RGB 4.2, 6.2, 14.3. Fraction of bright pixels: 0.18%. Three screenshots with identical hashes.

Those numbers are exactly the background color of its own CSS. It had measured the void, precisely, three times.

It had thirty tool turns. It spent them fixing a deprecation warning: it replaced an obsolete clock with frame timestamps, verified the change, and moved on. It never asked the first question one asks when a canvas is black: is the canvas in the document?

When its budget ran out, its final message was honest: the capture came out black, the render was still undebugged. It did not say it worked.

We added the missing line. A single one: take the canvas the renderer produced and append it to the container that was already empty in the HTML. The scene appeared whole, with the relief, the ring casting its shadow, the moons in their orbits.

## The seam

What was missing wasn't knowledge. It was the reflex to check the seam between the library and the document: the point where something that exists in memory has to become visible.

That kind of failure only shows up when the failure is silent, and it is exactly the kind of failure benchmarks don't measure. A unit test on geometry passes. A test on the orbit calculation passes. The page can be black and every test green.

Afterwards we ran the opposite test, the one that keeps any judgment of a model honest. The same session configuration, a different medium: a gothic wrought-iron lantern, procedural, no add-ons and no assets, six named parts, real-world scale, between three thousand and twenty thousand faces, exported to GLB.

It ran on the first try, in two hundred and eleven seconds. And it self-corrected: the first version came in under the face budget, so it raised the segments and repeated until the count fit. We ran the same script again from a different directory and it reproduced in six point six seconds.

Blender's oracle is binary: the script runs or it throws. When feedback is noisy, this model converges. When it is silent, it doesn't.

## The numbers that don't err in an obvious way

The uncomfortable part remains.

In arithmetic, the method was textbook and the result was wrong. One hundred thirty-seven shares at forty-two point three five: it wrote five thousand seven hundred ninety-nine ninety-five, when the answer is five thousand eight hundred one ninety-five. Then it took three point five thousandths of that already-wrong number as the commission and wrote two dollars and three cents, when it is twenty dollars and thirty cents. The final answer was five hundred eight seventy-nine; the real one, four hundred ninety-two thirty-seven. A return of eight point seven seven percent instead of eight point four six.

Two errors, carried to the end, delivered with four decimals of confidence.

That is the worst shape an error can take: the reasoning looks right, the presentation is impeccable, and the number is wrong. A human reviewer reading quickly signs off.

## What this means for those who evaluate agents

If we evaluate agents only with tests that throw errors, we are measuring half the work. The other half, the one that decides whether a product is any good, happens where nothing throws: a black screen, an email that never went out, a file written to the wrong path, a total that agrees with itself and not with reality.

A benchmark with an executable oracle rewards exactly what this model does well. And it is blind to what it does badly. That is why it pays to also look at the result with your own eyes, even when it hurts: the screenshot that has to be truly read, the render that has to be opened, the person who looks at the screen and says "this is black".

The practical conclusion, for anyone using models like this in production, is boring and useful. Code with an executable oracle: go ahead. Visual deliverables where the failure is quiet: only with something else watching. And arithmetic that matters: never without a second check, however good the line of reasoning looks.

## How this was done

One run per test, in a single session per test, with no memory and no tools beyond file and terminal. The manufacturer's numbers that appear in the video are the manufacturer's, and we do not reproduce them. This text is not a ranking: it is an impression with evidence, and comparison between models happens across episodes, not within one.

The full video, with the screenshots, the logs and the model's answers exactly as they came out, is here: [Flint Review: Confident, and Blind to One Line](https://youtu.be/4EM2ievQvh0).

The model is called Flint, it is from Recursive, and its weights are Apache 2.0. We have no relationship with them and they paid us nothing for this.

What lingers is not one model's error. It is the question of how much of our work we are going to keep evaluating with tests that only shout, when most of the failures that matter make no noise.

---

*This text was written by a Resyst Labs agent and reviewed by a person before publication. The facts, figures and screenshots come from the session documented in the video.*