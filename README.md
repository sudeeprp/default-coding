# Code without bounds

'Coding is about computer-languages' - is that true?
It's like saying 'Communication is about spelling and grammar'

The origin of the word 'code' suggests a 'systematic representation'
to reduce ambiguity. Like a 'code of conduct'.
Coding is about the attitude of reducing ambiguity, more than 'knowing a language'.

Even when we talk to humans, an intention to bring clarity is more important
than knowing the complete dictionary.
In fact, simple and un-ambiguous communication requires
deep understanding and heavy persistence.

Simple and un-ambiguous? For who?

Let's explore code written for computers.
It turns out that computers are so dumb,
their languages have severely restricted vocabularies.

Code written for a computer looks like this:

`10000100101101010001101`
<<check binary

It's a piece of code that adds two to something,
when it's run on an Intel processor.
No matter what language we used,
it needs to be translated to this kind of binary in order to run.

For a human seeing this code, it's hard to know what this piece is doing,
so there is a better vocabulary:

`a += 2` does the job in most languages like C, C#, Java, Python, etc.
A translation-chain ultimately makes this into binary.
##### The binary is for the computer. Anything else is for human consumption.

Now you can see why `a += 2` still misses the point -
it does not convey the significance of what's being incremented.
How about a better name?

`count += 2`

Good. So we are counting something. But what are we counting? How about:

`customers += 2`

Ok, we are counting customers. Maybe they are entering a store.
But why `2`? How about:

    COUPLE = 2
    customers += COUPLE

While this is python code,
it ultimately translates to the same binary and does the same job.
It's a little clearer now, that the `2` is to count a couple as two people.

Notice how it's bridging our intention
and the binary that 'runs' that intention.
When the code is close to our intention,
the chances of mistakes are minimized.

[Again, what was our intention?](intention-vs-implementation.md)
