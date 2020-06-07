# Techniques for expressing Requirements

Software has been used to solve problems for decades.
Over time, the expectations of customers [have evolved](modeling-needs-evolution-decades.md).


## Our example: Counting visits in a Store

![store](images/store.png "store")

## UML Use-case diagram

![usecasediag](images/counting-use-case-diag.svg "use case diagram")

## Use-cases

Ref. book [Writing effective use-cases](https://www.academia.edu/22312187/Writing_Effective_Use_Cases_Writing_Effective_Use_Cases)

**Goal**: Install and Commission Visit-counter in one store

**Primary Actor**:

**System**:

**Steps**:

**Extensions**:

**Variations**:

---

## Behavior Specification

```BDD
Given a store with an entrance
 And the pre-installed hardware
 And the installation store
When a store-owner requests installation
Then the installation is scheduled
 And operations is notified
```

```BDD
Given an installed system
When a customer visits the store
Then the visit is recorded
```
