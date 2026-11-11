---
title: 'Ten Remote Controls and a Single Lock'
description: 'Many copies of a credential are not redundancy: if replacing one means calling a person during office hours, what you have is inventory.'
pubDate: 2026-11-11
heroImage: ''
tags: ['systems', 'autopsia', 'philosophy', 'nocturnal']
translationOf: '2026-11-11-diez-controles-remotos-y-una-sola-cerradura'
---

For months, the access to a building ran on a form of redundancy nobody had designed. Several remote controls, one per unit, a few extra. If one failed, there was another. If someone was left outside, they borrowed one and that was that. The word people used was "backup" (*respaldo*), and for a good while the word worked.

Then a unit was lost. Access wasn't lost: what was lost was the ability to replace it.

The receiver that authorizes the opening keeps a list of codes. Adding a new one requires a device, a person and a window of time. That is to say: the system had many copies and a single path of issuance. That asymmetry was there all along, invisible, until someone was left outside at eleven-thirty at night with two neighbors, three remotes and none of them reachable.

The improvised solution had the dignity of the obvious: lower a remote out the window, in a bag, on a rope. Open. Send it back. Repeat the next day with another neighbor, because the first was traveling. After three loans nobody knew for certain who held what, and the last holder had become the de facto guardian of a key they had never asked to keep.

## Copies Are Not Failure Domains

Redundancy is counted in independent failure domains, not in units. Ten copies of the same code, issued by the same device, managed by the same person, with the same replacement path, are a single system. And a system with ten more surfaces on which to lose something.

The arithmetic deceives because it is easy to write and hard to honor. If the availability of one unit is _p_, and the units fail independently, then _N_ copies give 1 − (1 − _p_)ⁿ. The formula is correct and almost never applies: it assumes the copies share nothing. The moment they share the issuance mechanism, total availability is not the product of the copies but that of the common bottleneck. And that bottleneck, here, was one person with a programmer and a schedule.

That leaves a more honest definition, and a more useful one than any percentage: the redundancy of a system is the shortest route back to a copy that works. Not how many there are. How long it takes for there to be one again. If the answer includes "call someone" and "during business hours," the redundancy is lexical. What exists is inventory.

## Lending Does Not Duplicate: It Relocates

A borrowed remote adds no capacity. It moves it.

When someone hands over their remote, they are not creating a second key: they are accepting being left without their own. The backup does not appear, it is transferred, and the transfer carries a cost that appears on no spreadsheet: the lender takes on the risk of needing it at exactly that moment. In a small group this holds, because trust cushions it. In a large group it degrades along a familiar logic: the one who lends first lends too much, the one who always lends ends up with nothing, and the one who never lends discovers they can keep getting in anyway.

That is where the real cost appears. Asking for a remote is paying a tax in the currency of relationships, and the system collects it at the worst possible hour. Nobody designs that. It happens by accumulation: each individual loan is reasonable, the sum is an informal arrangement with no record, no revocation and no one responsible. A shared keyring is a permissions system administered by social memory, and social memory has no audit.

## The Migration That Looked Like a Step Backward

The fix ended in a centralized control: a single point of administration, additions and removals through one path. Told like that, it sounds like regression. We went from ten distributed devices to one central controller, exactly the opposite of what any manual recommends.

But the manual measures the wrong thing. What was centralized was not availability: it was issuance. And issuance was, from the beginning, the only component that mattered. Distributing copies of a credential whose replacement is a bureaucratic errand is distributing the risk of loss without distributing the capacity for recovery. Centralizing the mechanism of enrollment, by contrast, allows what no copy ever allowed: deactivating a lost unit without going out to look for a replacement, and issuing another without summoning anyone.

There is the lesson the object left written in its own autopsy: a single point of failure with proven recovery is better than many copies with impossible replacement. Because the failure we fear is not that the device breaks. It is that we cannot issue again.

## The Same Error, in Software

I have seen this figure repeat so often that I now recognize it by its smell. Three replicas of a service, each healthy, all reading the same configuration from the same bucket, behind the same DNS, deployed by the same pipeline, authenticated with the same credential. The multiplication of availability looks splendid in the diagram. The correlated failure does not appear in the diagram because it is not a box: it is an arrow they all share.

The cluster with three nodes and a single etcd. The "highly available" system whose certificate expires once for everyone. The continuity plan whose restore procedure lives in the head of a person who happens to be on vacation that day. In each case there are replicas and no independence, and independence is exactly what costs: separate credentials, separate administration planes, separate on-call rotations, procedures that someone has run cold at least once.

Everything else is catalog. And the catalog looks the same as resilience until you need a part that is no longer manufactured.

## The Question That Matters

When redundancy is added, the intuitive question is how many copies there are. It is an inventory question, and that is why it is answered easily: you can always buy one more.

The question that decides is another: what is the shortest path back to a copy that works, at three in the morning, without calling anyone. If that path does not exist, adding units only enlarges the number of things that can go missing, and enlarges too the number of people who depend on the same bottleneck.

The ten remote controls were never a backup. They were a queue. And a queue looks a good deal like a cushion until it fills: then you discover that nobody was waiting for their turn to open the door, but for their turn to borrow.