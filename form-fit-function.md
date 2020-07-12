# Form FIT Function

... describe the characteristics of a part.

Such a description can be used in manufacturing or replacement scenarios.

Take this fastener, for example:

![fastener](images/blackenedscrew.jpg "fastener")

Its _form_ may be characterized by
shape, weight, volume, thread-pitch and so on - before and after fastening.

Its _fit_ would depend on the thread that receives it

Its _function_ would be to fasten something, of course.

Using these characteristics, we can replicate its usage wherever
'fastening' is required.
We can replace it too.

Or can we?

Consider the 'fit' part of the story.
Is it enough if it fits the receiver thread?
No, here is a bunch of other aspects to consider:

It may be part of a bigger system,
which needs to be assembled with limited tools.
So the type of the **screw head** is important.

It must neither corrode, nor pollute.
**Blackening** would be a cost-effective option.

What about the 'function'?
This part must function with certain load, heat, vibration and a lifetime...

This is where things get complex.
For instance, a full specification of 'vibration' is not possible,
due to its non-linear nature.

There is a limit to the ease of specification,
even while dealing with small parts.

> A _complete specification_ is too expensive.

## Software form-fit-function

Can we make software replaceable by characterizing it?

While Software doesn't have a physical form,
The resources consumed by a software may be considered its _form_.
As long as the resources of space and time are provided,
it can run.

However, software continuously deforms -
built with changing dependencies and runs in many different states.

For instance, a software that receives images over a network
may run out of memory if it receives too many of them too fast.
With interlinked resource requirements, which inevitably change
after the software has been made,
the 'form' of software is hard to characterize.
Maybe it doesn't have a fixed form.

> Dynamic analysis can recognize the effect of these changes early.

The software will _fit_ in an environment when
its interfaces are accessed as expected.
It also has to feel familiar to its users, maintainers, and ops .

> Reduce ambiguity; Measuring 'least surprise'

The software _functions_ according to what we tell it to do.
However, the functionality experienced is not only the code we write,
but also the behavior of all dependencies.

> Sometimes we code implicit behavior without our knowledge

For instance, take the class that increments the number of visits:

```python
class VisitCounter:
    visitCount = 0
    def oneMoreVisit(self):
        self.visitCount += 1

def afterTheFirstVisitTheCountMustBeOne():
    visits = VisitCounter()
    visits.oneMoreVisit()
    assert visits.visitCount == 1

afterTheFirstVisitTheCountMustBeOne()
```

It's a simple class with a test-function
that says `afterTheFirstVisitTheCountMustBeOne`.
Let's look at the functionality we missed specifying.

**How about overflows?**
If it's a 32 bit signed integer, it can count approximately two billion.
Not a problem to count customers in a neighborhood store,
maybe an issue to count visitors to a site.

Overflow is implicit behavior in this code with unspecified consequences.

**Who uses it? Which language?**
Does this need to get integrated into a mobile app, or a lambda?
By coding a python class, we've made that a bit tricky.

**When should it reset?**
Are we doing the counts per day or per month?
What if its needed per hour for billing, per month for analytics?
Here we just made it increment indefinitely.

**Should it remember across restarts?**
Computers always need restarts - yes, even those on the cloud.
We've not specified the behavior in that situation.

**How do we handle mistaken increments?**
What if almost all visits yesterday were fraudulent, maybe someone
tried an attack? How do we roll it back?

You can see what's going on... if we keep changing our class
for all these requirements, it will get complicated.
The class will get tied up to billing, analytics and so on.
Eventually, it will be hard to change it
without affecting something else.

> How do we avoid this complexity and keep things replaceable?

At every question above, let's rethink-
How do we design, so we _replace_ (not modify) the implementation?
What is a different way of doing it?
How would a non-programming person do it by hand?

Anyone thinking of storing visit-logs?

Let's say we store a visit log, which documents the time of each visit.
We could pick what we want from it: filters to remove fraudulent data;
billing that takes hourly counts; analytics that counts by month or seasons.

This is a flavor of _event sourcing_.

Each functionality is free to make its own view of the data,
without interfering with others.
There is no need of a common data-model, other than the visit-logs.
Each vertical (billing, analytics, etc) is separate.

This type of solution 'vertically slices' the problem.
