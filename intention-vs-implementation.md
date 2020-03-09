# Intention and Implementation

Let's say our intention is to count
the number of customers coming into a store.

A possible piece of python code would be:

```python
def customerCoupleEntered():
    customers += 2
```

Is this correct and complete? No, it's defective on several counts!
Let's look at the defects one by one.

To start, what is the initial value of the 'customers' counter?
To us, it seems obvious - before we start counting customers, the count is zero.
Computers are so dumb that they cannot reason this out.

So if you feed this code to a python translator,
it complains that it doesn't know what customers is:

`UnboundLocalError: local variable 'customers' referenced before assignment`

If we had used this software at a store, it would have terminated at the first count!

Ok, we know that the counter needs an initial value.
How do we fix it? We need to assign `customers = 0` somewhere. Where?

That depends on our intention.
We haven't stated our intention well enough to code correctly.
For instance, we didn't state how long it needs to run -
Do we count customers per day? Or per month?

Let's say the owner of the store needs monthly counts.

One way to do it would be to fix the initial value of 'zero'
at the start of the program, then keep incrementing.

```python
customers = 0

def customerCoupleEntered():
    global customers
    customers += 2

def customerEntered():
    global customers
    customers += 1
```

Some notes about the grammar here: In python, the keyword `def`
is used to give a name to a sequence of code.
The code to increment `customers` by `1` is given the name `customerEntered`.
We can run the code in it by writing code like this:

```python
customerEntered()
```

If we run this code at the start of the month and
keep calling `coupleEntered()` or `customerCoupleEntered()`
every time an entry happens, we would have the monthly count.

Of course, there are more questions on the intent of this code,
but let's turn our attention to the technology first.

Technology usually is a bunch of what-ifs from Murphy.
What if the program didn't run continuously over a month?
Computers need to shut down sometime, and they don't wait for the right time!

The value of the `customers` counter would be lost on a power cycle.
A common solution is to store the 'state' of the program
(here, the counter) to a file. It will be remembered
till a part or whole of the computer is replaced.

Now we have a few more questions about our intent:
When should it restart the count?
What if we lose the count in-between?
What is special about a couple?

You can see that many of these questions cropped up after we
dipped into technical details.
While these questions feel trivial,
it's surprising how frequently they are missed.
