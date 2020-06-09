# Requirement Modeling Capabilities

![REbefore](images/engineer-before.png "RE-puzzled")

What does it take for a Requirements Engineer to be successful?

## Model

...is an example to follow or imitate.

## Modeling

...to devise a representation of a system.

...to display (clothes) by wearing them.

---

![storeowner](images/store-owner.png "store-owner")
`Exercise: Make a representation of customer need`

The customer needs

- visit-count-records per day of week
- what visitors are buying
- well maintained inventory

for ensuring well-stocked store with fresh supplies

---

The customer needs

- billing counters & billing personnel
- real time data
- fast track counters
- access to goods
- product mix (prediction/analytics)
- clear labeling (price, expiry)

for ensuring quick service

It needs to be accurate +/- 5%

It needs to be robust in all scenarios (day/night, power)

It needs to be transparent = inform customer of any failure / failover

---

![operations](images/operations.png)
`Exercise: Make a representation of installation`

Operations need

- plan timing
- location / address
- positioning
- tools - hardware + software

for quick installation and commissioning

It needs to have passed a trial run

It needs to have a verification mechanism

---

![developers](images/developers.png)
`Exercise: Make a representation of installation for developers`

The implementation needs to

be flexible / portable

for compatibility

---

The implementation needs to

architect with strong alignment between customer need and platform

for reusing existing software (COTS)

---

The implementation needs to

have a good interface + logging

for quick trouble-shooting

It needs to be clear, concise...

---

## Requirement Engineer Capabilities

- Cross-functional empathy
- Expression in the language of the audience
- Precise and Accurate translation
- Technically grounded

### ...across the spectrum of Models

<!-- markdownlint-disable MD013 -->

Customer Requirements | System Requirements | Module Requirements | Implementation | Deployment
---|---|---|---|---
Report on visit counts | Sensor, API & app with authentication | WebServer, Persistence | Record the visit in MongoDB | One-click container

Can we really model all their needs? [Yes we can](modeling-needs-analogy-structure.md)
