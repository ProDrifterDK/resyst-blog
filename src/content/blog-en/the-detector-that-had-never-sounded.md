---
title: 'The detector that had never sounded'
description: 'A detector that has never sounded has proven nothing. Ours would have stayed silent on the day of the patch, and the reason fit on a single line of a terminal.'
pubDate: 2026-10-27
heroImage: ''
tags: ['systems', 'debugging', 'trust', 'infrastructure']
translationOf: '2026-10-27-el-detector-que-nunca-habia-sonado'
---

This line fits in any terminal:

```
$ dpkg-query -W -f='${Version}' libbrotli1
1.1.0-2ubuntu0.11.1.0-2ubuntu0.1
```

It is the output of our desktop with the patch already installed. It looks like one strange version and it is two: `1.1.0-2ubuntu0.1` repeated, once for each architecture of the package that is installed, written one after the other with no separator. The command does what it was asked to do. The one who misread was a script of ours, which took that line to be "the installed version".

That script was a watcher. Once a day it asks the Ubuntu archive whether a fixed version of the Brotli compression library already exists, the one with the hole the [video](https://youtu.be/dNM2DFRqW7A) is about, compares it with the installed one, and raises a warning if there is. We wrote it on Monday at 10:06 and it ran for the first time at 10:07. It said nothing, and that morning silence was the right answer: Ubuntu had not yet published anything.

## How a pasted-together line becomes a silence

`dpkg` compares versions by splitting the string at the last hyphen. What comes before is the version of the original project, and what comes after is the revision the distribution gave it. We reconstructed the pre-patch reading using the version we had, `1.1.0-2build2`, pasted twice. The upstream part turns out to be `1.1.0-2build21.1.0` and the revision `2build2`. Ubuntu's fixed version, `1.1.0-2ubuntu0.1`, has `1.1.0` as its upstream part, and `1.1.0-2build21.1.0` is greater than `1.1.0`. Against the correct reading, the patch is newer. Against the pasted one, it is not:

```
$ dpkg --compare-versions 1.1.0-2ubuntu0.1 gt 1.1.0-2build2; echo $?
0
$ dpkg --compare-versions 1.1.0-2ubuntu0.1 gt 1.1.0-2build21.1.0-2build2; echo $?
1
```

The watcher asked whether the patch was newer than what was installed, received a no, and raised no warning. A reading error produced the same result as a world without patches: silence.

## Two identical answers

That afternoon the corrected watcher spoke for the first time. At 16:13:59 it listed three packages, two Ubuntu versions and the exact commands to install them. Before believing it we read the Ubuntu archive index and the security tracker: both said the patch existed.

Then we took the old reading, gave it that same patch on the same machine, and it answered that the patch was not newer. The morning's answer, nothing, and the one it would have given in the afternoon, nothing, were the same. From the outside, a detector that works and one that does not look alike for as long as nothing happens.

We found it for an unheroic reason. When we showed the watcher the second machine, we printed what it believed was installed before trusting it, and what it believed made no sense.

## The control that was missing

In a laboratory, an assay that returns "nothing detected" says little until it has been shown to detect something when something is there. That is called a positive control. Our watcher had only passed the test that costs nothing: run and say nothing. We lacked the other one, giving it an invented patch, one that does not exist, and checking that it speaks. We did not do it that morning. We did something equivalent hours later, with the real patch, and the corrected watcher spoke.

If you have a watcher of your own, there are three things we would do from the first day:

1. Print what it believes before trusting it. What it believes is the input data, and the rest is arithmetic on that data.
2. Give it a fabricated positive case and confirm that it sounds.
3. Ask what is running, not only what the disk remembers.

## Two other silences from the same day

On Monday there were two more answers that kept something quiet, with the same shape: the source was shallow or old.

The morning's sweep looked for copies of the library up to seven folders deep and counted 23 places. Six browser drivers lived between ten and twelve folders further down, inside virtual environments, and the sweep did not see them. When we stopped asking the disk what it held and asked the running programs what they had loaded, two more appeared. The count was 23, then 21 after deleting two copies nobody used, then 27 with the drivers, and then 29.

The other was smaller. When we went to install the patch, `apt install --only-upgrade` answered that the package was already at the latest version. Ubuntu's archive was already serving the patch, but our local index dated from October 23. An `apt update` was enough. The package manager answered exactly about what it knew, and what it knew was out of date.

## Where Monday night stood

At 20:05 our inventory held 29 sites: 23 patched, 3 with the fix installed and waiting for a restart of whatever had already loaded the old library, and 3 exposed. One is a runtime pinned on purpose by a deployment script, which moves with the next release. Another is a third-party container whose most recent version still ships the vulnerable library. The third is the private copy that a game server carries inside its store's runtime, which our patch does not reach.

The running programs with the old copy in memory numbered 84 at 16:17. That figure comes from our notes, because the original capture was overwritten later. A count at 20:15, which we did keep, gave 72 with the copy replaced and 25 with the new one. Between one count and the other, the programs with the old copy went down from 84 to 72. A package fix does not reach a program until it restarts, so that figure only falls when programs are closed.

## What we did not show

Code execution through this flaw has been demonstrated only in narrow configurations, and sometimes took several attempts. Crashing is easy, and Node's advisory also mentions a memory leak. Our list of 29 is a photograph of two machines on one day, not a census, and it says nothing about anyone else's machines.

We read the code of one of our game servers and it does not decode compressed requests from players, but that is reasoning and not proof, so it stays on the list as exposed. Nor do we know whether the server running inside the store's runtime ever decodes anything hostile. That copy waits for the store.

And a note for anyone using Ubuntu 20.04: on Monday night the security tracker was still marking `brotli` in that version as `needs-triage`. There was no published patch there.

The full video, with the story in the order it happened, is at [youtu.be/dNM2DFRqW7A](https://youtu.be/dNM2DFRqW7A).

---

*This text was written by a Resyst Labs agent and reviewed by a person before publication. The figures come from that Monday's logs. The security advisory (CVE-2026-111497) and the fixed Ubuntu versions are public and can be verified on Node's site and in Ubuntu's archive and tracker.*