# Situations in Refactoring

What do you do with old software, which has become hard to understand and maintain?

Intuitively, it is not worth modifying it.
Nobody wants to spend money in development that yields nothing for a user.
More importantly, who knows if the modified code will be better?

On the other hand,
industry is rich in anecdotes about the cost of unclear code:

- For every 30 static-analysis rule violations, [you can expect on average
three minor bugs and one major bug.](https://www.safetyresearch.net/blog/articles/toyota-unintended-acceleration-and-big-bowl-%e2%80%9cspaghetti%e2%80%9d-code)
- The ratio of time spent reading versus writing is
[well over 10 to 1](https://www.goodreads.com/book/show/3735293-clean-code).
This true of new code, modifications, well-written prose or any other piece of craftsmanship.
That means if you spend twice, or even thrice the amount of time to make code readable,
it would be faster, even in the current development cycle.
- The [curse of knowledge](https://stevenpinker.com/files/pinker/files/the_source_of_bad_writing_-_wsj_0.pdf)
brings complexity (not only to code),
which drains vast sums of money from the economy.

Yet, we know there are difficulties. In the war between new investments vs clean-ups,
here are a few situations and frequent responses:

<!-- markdownlint-capture -->
<!-- markdownlint-disable line-length -->
Situation | Response #1 | Response #2
---|---|---
It's old code and we're not adding much | Anyway it's ugly, why beautify it? | Changes here don't get us high margins. Make them inexpensive.
This code is not business critical | If customers don't care, why should we? | It's low risk to change. Let's use this to build our capability and reputation.
Only small changes allowed | Unit test effort is higher than the code change. Skip it. | It will be revisited at least 10 times in its life. Let's safeguard the change.
We're scared to touch it. Hard to get good talent to work on it... | Let my successor bite the bullet | Let's see the code we fear; Let's prevent it from getting worse.
<!-- markdownlint-restore -->

If you feel for Response #2 in any of these situations, read on.

Given the objective of speed and reliability, have a look at
[this link, which explores Lucid, Correct and Unambiguous coding](investment-benefits.md),
while enabling future maintenance to do the same.

Here are a few approaches you can do right away.

## Making changes inexpensive

Any change made by a human is prone to error.

The least we can do is to remove mistakes in the new or changed code,
before it leaves our desk.
A possible approach is to always develop new code separately.
Pull out the logic into a separate method, unit-test it and then integrate.

With this, any remaining issues would be confined to a lack of understanding,
or interference with the system. This is a good place to be.
It is possible if you have confidence
that your unit tests are sharp enough to catch issues.

## Safeguarding the change

If the unit test is persisted and maintained,
it can be used when people make further changes to the software.
This way, we ensure that human mistakes are caught early.

## Confidence in integration

Today, code written for a feature
makes up less than 5% of the experience delivered to a user.
We build on top of language-runtimes, containers, operating systems, clouds...
all of which contribute to the user's experience.

None of them have built their software for our particular use.
Fixes, deprecation and obsolescence keep happening in the real world.
Confidence in integration can be built with integration tests
at the interface-points, in addition to unit-tests for our functionality.

## Prevent complexity from growing

Hard-to-read code gets harder when when features are added. Developers
take more effort to understand, which makes for higher deadline-pressure,
which makes for more haste, more short-cuts and complex code.

Placing hard limits on new code and freezing complexity limits on old methods
is a possible approach.
