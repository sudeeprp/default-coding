# Intention and Implementation

Let's say our intention is to count
the number of customers coming into a store.

A possible piece of python code would be:

```python
COUPLE = 2
customers += COUPLE
```

Is this correct and complete? No, it's defective on several counts!
Let's look at them one by one.

To start, what must be the initial value of the 'customers' counter?
To us, it seems obvious - before we start counting customers, the count is zero.
Computers are so dumb that they cannot reason this out.

Many defects in the code arise from such a mismatch between
our assumptions and the machine's limited understanding of the world.

If you feed this code to a python translator,
it complains that customers is <<'not defined'.
Today's translators highlight potential ambiguities.
Ok, so we know that the counter needs an initial value.
How do we fix it? We need to assign `customers = 0` somewhere.

Where? That depends on our intention.

We haven't stated our intention well enough to code correctly.

For instance, we didn't state how long it needs to run -
Is it the count of customers per day? Or per month?

Let's say we want the monthly count

Then, there are the what-ifs that come from Murphy.
What if the program didn't run continuously for the month?
Computers need to shut down sometime...

When should it restart the count?
What is special about a couple?
While these questions feel trivial,
it's surprising how frequently they are missed.
