# Relating to Stakeholders

## Stakeholder

...a person with an interest or concern in something, especially a business.

> In your project, you are a stakeholder!

`Exercise: List the stakeholders in your project`

## Mapping Stakeholders

<<Value chain

## Stakeholders Evolve

People change:

- After using the product, goals become clearer
- After using another product, expectations change

[The requirements are alive!](modeling-live-requirements.md)

## Obstacles to Evolution

<<if-else -to- goals
<<contradictions

Try [functional decomposition of business flows](modeling-business-flows.md)
to overcome these obstacles.

## Specifying for Stakeholders

Use a story or a context

<!-- markdownlint-disable MD013 -->
Requirement | Context | Specification
---|---|---
No memory leaks | Mobile Ultrasound, continuous operation for 2 days max | X no. of cycles without deterioration of performance, stable working-set and commit-charge not exceeding 3.5GB
No training required | ATM front-end | Start-screen same as previous version
X-ray latency <1s | Used during surgery | One in 20 measurements can go above 1s, with max not exceeding 2.5s

How about regulatory requirements?

Regulation | Context | Specification
---|---|---
Data Privacy in car entertainment systems | Consequence of misuse: Loss of branding & trust | Hardware-level encryption
