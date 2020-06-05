# Lucid, Correct, Unambiguous

Writing in any language is an art-
especially if it needs to be short, easy to understand and precise.

Writing with clarity needs skill and practice. To take a physical analogy,
stained glass was produced from ancient times.
It took centuries of work to remove the color 'stain' and make clear glass.
The effort was clearly worth it.

The effort to make 'clear' code almost always pays off.
It's also easier and faster, in comparison to making clear glass :)

Let's go backwards through the
heading of this article - making code 'Unambiguous'.

## Unambiguous

[Code is always **un**ambiguous](README.md),
since a computer needs to execute it.
A single instruction to a computer always does the same thing.

However, its effect may vary depending on its environment-
what happened before, or what else happens during its execution.

Tools like compilers, static analyzers and linters
can report some of these ambiguities.
These reports are derived from years of experience with a language.

Of course, ambiguity doesn't mean a defect. It's only a potential
indication of a present or future defect. For instance, an analysis
of the code can report an uninitialized variable,
but not overflows and concurrency-related issues.
[See here](https://docs.sonarqube.org/latest/user-guide/issues/)
for one possible classification.

> Static Analysis and Coding Standards highlight potential ambiguities,
helping to avoid current and future issues.

What if we ignore these reports, focusing on
'working software' while allowing violation of recommendations?

- [This article](https://www.safetyresearch.net/blog/articles/toyota-unintended-acceleration-and-big-bowl-%e2%80%9cspaghetti%e2%80%9d-code)
talks about violating MISRA-C rules and expresses a generalization-
For every 30 rule violations, you can expect on average
three minor bugs and one major bug- now, or in maintenance.
- However, the variance in that figure is very high. If you think that
violations in a simple piece of code cannot have an impact,
[look here](https://www.zdnet.com/article/another-one-line-npm-package-breaks-the-javascript-ecosystem/)-
a single violation caused wide-spread development-impact.

Ambiguous code need not always reflect as defects for users.
Defects can be caught in testing, either with ease or difficulty.
It's least expensive to resolve ambiguity when a tool can detect it.

Once we've settled ambiguity, we need to check the correctness of our software.

## Correct

Software systems grow huge- almost all of it built by human hands.
Humans make mistakes. Two pieces of software that share resources
(maybe they're on the same network) can interfere, even though
they weren't meant to interact at all. Human mistakes can multiply.

That's why defects are orders-of-magnitude more expensive to catch,
as the software starts interacting with
dependencies, different systems, the environment and the user.

Unintended behavior in the software can only be detected by its effect.
When we reduce the dependencies of a test to make it fast and repeatable,
we get a **unit-tests**.

'Coverage' is a metric that says if each line in the code
executes without crashing. It is a basic metric of unit-testing.
However, this metric doesn't say if the covered code
produced the desired effect.

How do we ensure that our tests are 'sharp' enough
to catch issues close to the developer?

Here are two approaches:

1. Use of mutation testing tools, which introduce defects in our code
and see if our tests can catch the issue.
2. The practice of failing a test before writing any new code.
This would mandate a build failure before a build success for every work-item-
Including fixes for issues reported by the user.

**Integration-tests** exercise the behavior at the interfaces. Commonly,
they can catch issues in the interface quickly.

For instance, applications
rely on the camera interface via a mobile device platform. The interface
is expected to deliver an image to us.
Building tests around the characteristics of the image would make it
easy to check interoperability with any new device or run-time.

>Unit tests and integration tests can be fast and independent.
Keep sharpening them to reduce investigation and fixing times.

Moving ahead, the most common form of a **dynamic test**
would check the timing-behavior of a system.
However, we know that violations in dynamic behavior are hard to diagnose
in a fully integrated system.
Apart from timing, this can include
dynamics related to memory, CPU cycles, etc.

A 'System' looks at the whole instead of the parts. **System tests** exercise
the whole, looking if the parts are working well together.
When we avoid repeating the previous-tests here,
we force the usage-perspective, reducing the residual risk of human mistakes.

Often, the 'System' is a combination of hardware, software and people.
For instance, a testing a clinical system would require the medical device,
people with product expertise and clinical knowledge.

What if you get all of them together, and the thing doesn't startup?
**Smoke tests** are meant to give quick feedback that the
'system doesn't go up in smoke', before investing time to verify all of it.

## Lucid

The word 'lucid' is an adjective, which says that something is expressed clearly
and is easy to understand.
Why is it difficult to make things easy to understand?

Many things come in the way, most notably the
[curse of knowledge](https://stevenpinker.com/files/pinker/files/the_source_of_bad_writing_-_wsj_0.pdf).

Code seems so easy to understand when it is written,
due to the belief that we know what it is doing.
Ironically, this grows with experience- the more you work with the same code,
the more assumptions you make about its readers.

This has some consequences in our approach:

- A nested switch-case! Why is it so hard to follow?
- Copy-paste a little.
It's obvious that any changes will need to be repeated as well.
- We'll leave the unused code, just in case.
When we need to migrate this to a new OS, we'll avoid spending effort on it.

Of course, when we look at the same code after a few weeks,
it doesn't seem all that obvious. By that time,
we would have been relieved of the curse of knowledge!

**Duplication** comes in many flavors. Apart from the common copy-paste,
branching, code-similarities, design-similarities and similarity of purpose-
all of them are opportunities to look for duplicates.

Tooling for copy-paste detection works well in verbose languages,
where a repetition of 8-10 lines of code can be considered significant.
However, in languages like python or in case of a domain-specific language,
a line-count of 3 yields better results. Also, a human can detect similarities
much better than any tool.

For instance, when interpreting a clinical lab report,
the instructions can be repetitive:
See if the pulse-rate is in the normal range;
if the blood pressure is in the normal range;
if oxygen saturation is in the normal range...
We wouldn't do that.
We would normally abstract it as:
See if all parameters are within their normal range.

> Recognition of duplicates helps in realizing abstractions that
may have been missed in design.

**Complexity** creeps in, usually seen as semantic-distance

Long sentences with multiple 'and' and 'but' are difficult to read. Similarly,
long methods with a lot of loops and conditions are hard to understand.
Cyclomatic complexity is a metric that effectively indicates
the _minimum_ number of test cases required to check all flows in a function.
It's essentially the number of factors we need to keep in mind while changing
the method.

A normal human could keep track of 3 items simultaneously.
Keeping method-complexity at (or under) 3 would mean less time for anyone
trying to understand it.

Complexity increases due to other factors as well, including shared state,
dependencies (fan-out) and dependents (fan-in).

> Controlling complexity is about making the code talk about its purpose.
Looking through simple code is like
seeing the specification through clear glass.

**Dead code** can happen due to multiple factors

Unused variables, unreachable code and unused imports are examples
that are detected by static analysis of the code.
Variants of these are unused styles in web-pages,
unused routes in web-services, etc.

Code behind unused features is also dead code,
which requires run-time statistics to figure out.

What's the problem of dead code, given that bugs in there will not show up?

There are at least two problems it would cause:
When we keep a lot of unused stuff, the useful stuff gets harder to find.
This code keeps coming up in searches;
it will not compile when methods get deprecated; etc.

> Removing unwanted code removes cognitive and maintenance overheads.

That was a round-up of some metrics and approaches that can enhance
speed of development. In this game, we need to keep in mind, that the tools
are only that- they are tools. We take their help where we need, while keeping
in mind that there is still a human factor involved in writing clear code-
like good writing.
