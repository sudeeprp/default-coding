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
3. Field engineer ensures prerequisites: stable power, internet connection
4. Field engineer travels to the site
5. Field engineer takes measurements
6. Field engineer agrees the position and accessibility with store owner
7. Field engineer records owner-permission to commission, with passwords for internet connection
8. Field engineer installs the hardware and does a power-on
9. Field engineer installs the software
10. Field engineer performs startup checks
11. Backend offers a test-mode to the Field engineer
11. Field engineer signs off test results with store owner
13. Field engineer switches backend to production mode

**Extensions**:

2 a. the kit is not available

8 a. Power on unsuccessful

11 a. Test mode is not required

...

**Variations**:

Field engineer has to perform steps 8, 9, 10 multiple times

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

- We need an app on the playstore that the Field Engineers can install on their own mobile
- Anyone should not have access to configure the system/device: Only Field engineers with valid credentials can configure
- Proper error response with correction suggestions ( if *misconfigured *etc ) in *GUI/log-file/popup...
- DEFOA: The instlalation kit shall *notify the Field Engineer when it is powered-on and there is a defect.
- The system shall provide a *notification to Field Engineer , customer and the seller company/person when installation process is done including connection to backend


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
