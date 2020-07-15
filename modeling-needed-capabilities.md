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

- Transportation, supply
- Suppliers of grocery
- Forecast of visitors
- Inventory / Stock that is already present
- Hygene in store / cleaning
- Vendor management
- analysis of product sales vs future demand
- Live tracking
- Connectivity to all stakeholders

for ensuring well-stocked store with fresh supplies

---

The customer needs

- Live display of count
- ability to staff billing stations

for ensuring quick service

Count needs to differentiate between visitors and staff

Accuracy: 100 visitors will be reported between 95 and 105, in a period of 3 hours

Valid = visitors ; Invalid = staff

It needs to be `what?`

It needs to be `what?`

---

![operations](images/operations.png)
`Exercise: Make a representation of installation`

Operations need

- easy configuration

for quick (< 1 hour) commissioning (=connect and train / signoff)

It needs to be simple

- anybody can do it
- minimize site dependency
- user manual for reference: for installation and for use
- adaptible installation (power adapter, wifi / 4G...)

It needs to be `what?`

It needs to be `what?`

---

![developers](images/developers.png)
`Exercise: Make a representation of installation for developers`

The implementation needs to have a workflow according to 'this' mockup

---

The implementation needs to be like Chromecast / home automation

---

The implementation needs to ...

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
