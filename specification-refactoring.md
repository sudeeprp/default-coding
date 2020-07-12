# Specification and Refactoring

Specification is the art of writing without ambiguity - being 'specific'.

Think of software code as a way of writing a requirement.
A precise way, which doesn't have ambiguity - because
[computers cannot tolerate ambiguity](README.md).

Software code - doesn't matter which language - doesn't really run,
of course. It needs to be translated into machine code.

## When compilers see something wrong

When a compiler or an interpreter finds it impossible to translate,
we get an error.

Sometimes it is possible to translate, but it's likely to turn out
ambiguous.
For example, the code we saw in the above link is translate-able:

```python
count += 2
```

...however, the result is likely to be wrong,
unless we fix the initial value of the `count` variable.

Depending on the language and compiler, this type of construct
could either be reported as an error or a warning.

> Warnings convey ambiguity in the code, recognized from vast experience
and built into the translator.

Given that a warning indicates an issue either now or in future,
it pays to write code without warnings.

## When specifics bring complexity

Sometimes, avoiding ambiguity makes for a lot of specification.
This can make for complex code too.

For instance, the requirement
'count the number of people who entered the store'
can do with some specification.

What about: 'keep an hourly count of customers,
aggregated monthly for statistics,
with capability to ignore mistaken counts,
recovering from the last known count in case of hardware restarts'

Often, our code 'speaks' like this. Different requirements are digested
and written together in code. When the specification of 'mistaken counts'
becomes precise, we would need to change the data (to mark mistakes)
and potentially every counting method.

This is not avoidable. Requirements start simple.
As the software is used in the real world,
additional needs are realized and mistake-proofing becomes important.

## Keeping things simple

Specification is hard. Even the 'simple' ones are hard.
[See here for an illustration](form-fit-function.md).

It's important to specify one small piece at a time,
while still keeping it meaningful.

In the above example, once we realize that it's getting complex,
it would be good to take a step back and re-word the problem:

1. Keep a time-stamp and permitted demographics of visiting customers
1. When a particular entry turns out to be a mistake, be able to mark it so.
1. When requested, extract hourly counts
1. Every night, extract statistics and publish
1. Retain past records up until 90 days

This would be a good start for Behavior Driven Development.

> BDD is about specifying in bits - in a way that's
understandable to a user of the software

A BDD specification is testable. That means - we always know how to recognize
if the code will work for the user.

This is a valuable tool to 'step back and look', before refactoring.
By the time a piece of code needs to be refactored, it is likely that
customer needs and technology offerings would have progressed.
Taking a step back would help in leveraging the changes as well.

## Duplicate specification

In the above example, take the two behaviors that may deal with counting:

- ...extract hourly counts, _ignoring mistaken counts_
- ...extract statistics, _ignoring mistaken counts_

On the face of it, 'ignoring mistaken counts' seems to be duplicate.
It's a good idea to define it once, instead of twice.
We need to be aware of the context, to realize the duplicate.

If we start the BDD for the duplicated piece, perhaps we would land up with:

- When hourly counts are requested, ignore the mistaken counts
- When statistics are requested, count the mistakes separately

Apparently, the 'ignoring' part is context-specific. However,
'recognizing' mistaken counts is common.

How do we recognize mistaken counts?
Usually, we would mark the mistakes in some way.
While such a mechanism is required, it is not directly recognizable by a user.

Even in this case, it is good to specify the
storage and retrieval mechanism, along with the interfaces to access it -
before writing the code.

Such a specification could be used to test the code. That is TDD.

> TDD is to specify a piece of code before writing it.

Specifying before coding helps in recognizing completion.
Without that, whatever the code does feels correct.
