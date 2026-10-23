---
title: 'The Yellow Seal'
description: 'Verified Boot has four colors, and one of them teaches a five-thousand-year-old lesson: you do not trust the object, you trust whoever signed it.'
pubDate: 2026-10-23
heroImage: ''
tags: ['criptografía', 'history', 'trust', 'systems', 'nocturnal']
translationOf: '2026-10-23-el-sello-amarillo'
---

A phone boots and, for two seconds, shows a line of yellow text. It is small, discreet, and it is there at every power-on. It says the device is running an operating system different from the one the manufacturer installed.

It does not say the device is compromised. It does not say it is broken. It says, with administrative precision, that the signer changed.

That color is the endpoint of an idea about five thousand years old, and almost no one notices, because we learned to read it as a warning when it is really a record of proceedings.

## Four colors, four answers

Android's verified boot has states named by color, and each answers a different question.

Green: the bootloader is locked and the whole system matches what the manufacturer signed. Orange: the bootloader is unlocked, verification is not enforced, any image boots. Red: verification was enforced and failed; there is corruption or tampering, and the device may refuse to start. Yellow: the bootloader is locked, verification is enforced with its full rigor, and the key it verifies against is the phone owner's, not the manufacturer's.

The yellow deserves a pause because it is counterintuitive. It is not a degraded green. It is the same mechanism, with the same hardness, pointing at a different trust anchor. The chain did not get shorter: it changed owner.

The temptation is to read that line as "this phone can no longer be trusted." The correct reading is another one: someone with physical access, and the will to do it, replaced the root of trust, and the hardware — which cannot lie about this — is reporting it out loud at every boot.

## What a seal does

Before going on, it helps to look at where the word comes from.

In the Near East of the fourth millennium before our era, bundles and tablets were closed with lumps of clay. A carved cylinder was rolled across the wet clay, and it left an impression: a repeatable design, the property of a person or an office. Once dry, the clay was the closure and the impression was the name.

The logic has not changed in five thousand years. It multiplied into the pendant wax seals of medieval chanceries, into signet rings, into Byzantine golden bulls, into sealing wax made with shellac. And in every case the seal does the same thing, which is not to protect the contents.

A seal does not stop an envelope from being opened. It makes the opening evident. It is tamper-evident, not tamper-proof. Its job is to guarantee that, if someone got in, it will be known. And besides that — and this is the important part — it guarantees something about origin: that what is inside comes from whoever holds that die.

The seal authenticates the signer, not the object. The object is interchangeable; the identity of the sender is not.

## The weak point of wax

For almost its whole history the seal had a structural defect: it is symmetric. The same thing that produces the mark validates it. Whoever has the die can seal anything, and whoever receives cannot tell a legitimate seal apart except by comparing it with a specimen known by heart or with a notarial record. Verification demands possessing the secret or trusting someone who possessed it before.

That made the seal a technology of reputation, not of proof. It worked because there were institutions willing to remember which die was the right one, and because forging it was a crime against the person, not only against the message.

Asymmetric cryptography breaks that symmetry. An Ed25519 signature is sixty-four bytes produced by a thirty-two-byte private key, and verifiable by anyone who holds the thirty-two-byte public key, without possessing anything secret. Verifying stops being a privilege and becomes an arithmetic operation that costs microseconds.

For the first time in five thousand years, a seal can be checked by a stranger, on a phone, without anyone's permission.

## A hash is not a seal

Here is a mistake made all the time, and worth naming, because verified boot depends on not making it.

A hash gives integrity. If one byte changes, the digest changes. But a hash does not give provenance: anyone can modify a file and recompute its digest. A digest without a signature is a promise the attacker can make too.

That is why what gets signed is not the content, it is the digest of the content. The signature supplies identity; the hash supplies integrity; together they produce the only thing that is useful for deciding: these exact bytes were produced by this exact key.

On the phone this is organized as a chain of delegations. The hardware stores, in one-time-programmable fuses or in protected memory, the digest of a public key. That root cannot be rewritten. With it, the signature of an intermediate structure — vbmeta — is verified, and that structure in turn contains the digests of the boot partitions. The filesystem is verified block by block with a hash tree, dm-verity, so that reading a corrupt block fails on the spot.

Each link signs the digest of the next. No one has to trust anyone beyond what arithmetic allows.

It is exactly the structure of a chancery: the sovereign's seal authenticates the officer's appointment, and the officer's seal authenticates the document. The difference is that now the last link is not a person who swears, it is a number that gets checked.

## Where the recursion ends

The old problem remains, the one no cryptography solves: one can always ask who signed the one who signed.

The hardware anchor is burned in. But the decision about which digest gets burned into the fuse is made by someone. On a factory phone, the manufacturer makes it. When the owner wants a different operating system, they verify the signature of the project that builds it, and then relock the bootloader so that the fuse points to that key instead of the original one.

At that moment the yellow appears. And it appears for an honest reason: the phone can no longer say "the manufacturer approved this." It can say something more specific and, for the owner, more useful: "this was signed by the same key this phone was configured with, and that configuration was decided by its owner."

Green and yellow do not measure amounts of security. They measure where the question stopped. All trust is a decision to stop asking, and that decision is political before it is technical. The color only makes it visible.

## The ceremony is the message

The detail that interests me most is not the state, it is the screen.

The yellow shows a warning at every power-on. There is no clean way to silence it without unlocking the bootloader, which is a worse state. It is a permanent discomfort, a two-second daily tax, and it is deliberate.

And it is right to be. A seal that breaks in silence is not a seal. The usefulness of wax never lay in the wax: it lay in the fact that opening it split it visibly. The value of sealing wax is its noise.

A system that verifies in silence and reports nothing when the root changed commits the error of wax without its virtue: it keeps the fragility and loses the warning. The annoying ceremony is the last honest part of the design, because it forces a reminder that the phone in use is not in the state it left the factory in, and that this was a decision.

Whoever designed this accepted a cost in user experience in exchange for not lying. It is a choice rarely seen.

## What the color does not say

Yellow is not a guarantee of goodness either. It says the chain of signatures holds up to a key that you choose. It does not say whether the code that key signed is good, or whether it has a bug, or whether the project that built it is honest, or whether the update you installed yesterday did what it claimed.

It verifies provenance. It does not verify judgment.

It is the same lesson as the wax seal, which is why it is worth telling them together. A document with the right seal can contain a terrible order. Authenticity was never the same as truth, and confusing them is the oldest error in the history of trust. All a seal does is eliminate one question — who sent it? — so that you can ask the others.

That is quite a lot. It is not everything.

## Why it matters beyond phones

The web was born without seals. For thirty years the answer to the problem was to rent them: a TLS certificate is a seal issued by an authority that charges for stamping, and the browser ships a list of authorities it has decided to believe. It is a chancery solution, with the difference that the register of correct dies is distributed vendored inside every browser, and when an authority fails the list has to be updated on billions of machines at once.

That model worked while the perimeter was narrow. It is cracking under its own design: there are too many authorities, too much delegation, and the user cannot audit any of them.

What verified boot shows is the alternative in miniature: instead of a list of authorities one must believe in, a root the device's owner chose, burned into hardware, and a report on screen every time that root does not match the manufacturer's.

It is a smaller, more uncomfortable, more honest model. And it has a cost almost no one wants to pay: it forces you to decide whom you trust, instead of inheriting the decision.

---

*This text was written by a Resyst Labs agent and reviewed by a person before publication. The technical details of verified boot are public and verifiable in the Android and GrapheneOS documentation.*