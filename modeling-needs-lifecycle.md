# Lifecycle hierarchy of user-needs

## Sample customer needs - Banking

![bankingsample](images/hierarchy-customer-need.png "need hierarchy")

### Concepts closer to the customer live longer

![needslongevity](images/longevity-customer-need.png "need lifetimes")

> Tip: Keep lifecycles separate

`Exercise: Lifecycle of needs in a store-visit-counter`

## Specifying the Customer for Stakeholders

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

<<relate to security privacy
## Recognizing the solution-scope

In a savings-bank solution:

- Financial security is out-of-scope
- Access to banking facility is out-of-scope
- Prevention of fraud...?
- Extension to ...?

`Exercise: Call the out-of-scope items from the` [customer context](modeling-needed-capabilities.md)
