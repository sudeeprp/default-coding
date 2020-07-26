# Techniques for expressing Requirements

Software has been used to solve problems for decades.
Over time, the expectations of customers [have evolved](modeling-needs-evolution-decades.md).

[Standardization](modeling-needs-standards.md) has tried to keep pace.

## Our example: Visit-counter

![store](images/store.png "store")

## UML Use-case diagram

![usecasediag](images/counting-use-case-diag.svg "use case diagram")

## Use-cases

Use-cases aim to bridge the gap between a customer-need
and its implementable specification.
Ref. book [Writing effective use-cases](https://www.academia.edu/22312187/Writing_Effective_Use_Cases_Writing_Effective_Use_Cases).

**Goal**: Install and Commission Visit-counter in one store

**Primary Actor**: Field engineer

**System**: Installation kit, Backend (cloud) for count-records

**Steps**:

1. Field engineer looks up location of installation
2. Field engineer looks up the order and picks the right kit
3. Field engineer ...

**Extensions**:

2 a. the kit is not available

...

**Variations**:

Field engineer has to perform ... multiple times

---

### Use-cases vs User-Stories

Use-cases may-or-may-not specify the qualities required for acceptance.

## User Stories

User stories capture the user-goal and **Acceptance Criteria**
to distinguish the scope of the solution.

### Example

As Field Engineer, I need installation interface/GUI
to commission the visit-counter software in a store
so that the customer has a full functioning solution.

[**Acceptance Criteria**](modeling-needs-acceptance-criteria.md):

The installation interface shall ...

---

Acceptance Criteria can be expressed in terms of
[rules or examples](modeling-needs-acceptance-criteria.md)

`Exercise:`
[Acceptance Critique](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAY-7brxUM1E3STBTRFlHWUNUVEM4MVkzWDFZTjhYWi4u)

> 'Good' acceptance criteria = lower
[transaction costs](modeling-real-agile.md)

`Exercise:`
[Acceptance Authoring](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAY-7brxUM0RGVTBQUlhCSlZDOUFBTTkyODM5WEFNVi4u)

## Behavior Specification

The Acceptance Criteria can be specified as Scenarios:

```BDD
Given a store with an address
When a store-owner requests installation at 2 PM
Then the installation is scheduled from 2-6 PM
 And operations is notified
```

```BDD
Given wired-up hardware with pre-installed software
 And our app is installed on field engineer's phone
When the field engineer completes first power-up
 And connects his mobile to the device-hotspot with SSID "v-counter"
Then Setup instructions should be visible
```

```BDD
Given an installed, powered-up system
When a customer visits the store
Then the visit is recorded
```

> Scenarios can bridge stakeholders across the spectrum

<!-- markdownlint-disable MD013 -->

Customer Requirements | System Requirements | Module Requirements | Implementation | Deployment
---|---|---|---|---
Report on visit counts | Sensor, API & app with authentication | WebServer, Persistence | Record the visit in MongoDB | One-click container

### Downstream effects of Scenarios

Scenarios can also fine-grain and separate life-cycles.
Such isolation contributes to the
[real agile practices](modeling-real-agile.md)
in the project.
