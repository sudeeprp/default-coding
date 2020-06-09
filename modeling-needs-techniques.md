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
3. Field engineer uses tools for installation
4. Field engineer completes hardware installation and power-on
5. Field engineer performs initial test after power-on
6. Field engineer sets up the profile / configuration
7. Backend system sends success notification to Field Engineer and Store-owner

**Extensions**:

2a. the kit is not available

3a. Field engineer doesn't have enough tools for a particular site

5a. Field engineer notes Initial test failure on power-on

`Field engineer looks up logging`

5b. Improper wiring to camera/backup

5b. There is no backup power



**Variations**:

Field engineer has to perform Steps 3-6 multiple times

Backend system sends a single notification for the entire installation

---

### What is missing in use-cases?

Use-cases may-or-may-not specify the qualities required for acceptance.

## User Stories

User stories capture the user-goal and **Acceptance Criteria**
to distinguish the scope of the solution.

### Example

As Field Engineer, I need installation interface/GUI to comission the visit-counter software in a store so that the customer has a full functioning solution.

[**Acceptance Criteria**](modeling-needs-acceptance-criteria.md):

The installation interface shall

- the app shall provide configuration of the software on android & ios
- the app interfaces with hardware to provide test results - no false postives and false negatives
- the app shall provide for manual entry of local wifi configuration, provided power and wifi router are present
- the system shall automatically connect to the backend
- the app shall indicate a successful or unsuccessful connection



---

Acceptance Criteria can be expressed in terms of
[rules or examples](modeling-needs-acceptance-criteria.md)

`Exercise:`
[Accpetance Critique](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAY-7brxUM1E3STBTRFlHWUNUVEM4MVkzWDFZTjhYWi4u)

> 'Good' acceptance criteria = lower
[transaction costs](modeling-real-agile.md)

`Exercise:`
[Acceptance Authoring](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAY-7brxUM0RGVTBQUlhCSlZDOUFBTTkyODM5WEFNVi4u)

## Behavior Specification

The Acceptance Criteria can be specified as Scenarios:

```BDD
Given a store with an address
When a store-owner requests installation
Then the installation is scheduled
 And operations is notified
```

```BDD
Given a store with an entrance
 And the pre-installed hardware
When field engineer completes installation
Then ....
```

```BDD
Given an installed system
When a customer visits the store
Then the visit is recorded
```

### Downstream effects of Scenarios

- Scenarios can also be used to fine-grain and separate lifecycles.
- The level of fine-graining contributes to the
[real agile practices](modeling-real-agile.md)
in the project
