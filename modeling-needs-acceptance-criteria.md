# Acceptance Criteria

Acceptance Criteria:

- Express when a customer would see value from the software
- Specify the pre-conditions for a handover
- Quantify 'acceptable experience'
- Clarify scope

## Types of Acceptance Criteria

- Rules oriented
- Scenario oriented

### Rules Oriented

A rule is:
- A statement that **must be** satisfied
- **must be** = sentence with 'shall' / 'is' / 'are' ( = assertions)

#### Bad Example:

Use-case: Report visitor-counts

As a Store-owner, I want to see a report of visitor-counts over a past period,
so that I know how many visitors were there in that period.

Acceptance Criteria:

- When I select a period, the counts are reported for that period
- When I change the period and press 'Refresh',
the counts shall change to reflect the new period.

---

#### Better Example:

Use-case: Report visitor-counts

As a Store-owner, I want to see a report of visitor-counts over a past period,
so that _I can predict my resources for the near future_.

Acceptance Criteria:

- Counts are reported against dates and days of the week
- Anomalies (e.g., holidays) are distinguishable

---

### Scenario Oriented

A scenario is an example with:

- Initial Criteria
- Actions
- Expected Outcomes

**Gherkin** is a notation to express scenarios

#### Example

Use-case: Report visitor-counts

As a Store-owner, I want to see a report of visitor-counts over a past period,
so that _I can predict my resources for the near future_.

Acceptance Criteria:

```BDD
Scenario:
  Given the count-data is available for the last two weeks
  When the customer requests data from the last 8 days
  Then the counts per day are shown along with the days and billing information
```