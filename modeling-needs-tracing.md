# Tracing Stakeholder Needs

## Dive-and-Resurface

![value-chain](images/value-chain.png "value chain")

The [client needs framework](https://evolytics.com/blog/hierarchy-client-needs-framework-analysts/)
relates to how it would look from a client's perspective.

## Questions

- **How** is this implemented? Dive!
- **What if** I change this? Dive!
- **Why** is this implementation? Resurface

## Tracing Dimensions

'Detailing' can happen at the same level of lifecycle:
Such as 'Safety' being quantified in 'Safe access to savings'

![lifecycle](images/hierarchy-customer-need.png "customer needs")

## Difficulty in Bidirectional Tracing

`Exercise: Dive and Resurface- why is logging there?`

**Business goal**: Higher AMC, More installations, Valuation

**Project goal**: Develop log-export functionality

**User goal**: Quick diagnosis and fixing (CRS)

**Technical Responsibility**: Files in some format, easy to read (SyRS)

**Interfaces**: Upload via API (auto) / download on request (manual)

**Implementation**: Export log-files from equipment

---

### Relationships

Requirement | Relationships | Requirement
---|---|---
Investment grade | **quantifies** | Safe access to savings
Create-account | **details** | Enroll
Build | **depends on** | Compile
Development Environment | **uses** | Auto-complete
Send SMS | **implements** | Notify user
