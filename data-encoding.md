# Data Encoding

Encoding is about representing something unambiguously.
Given that processors understand only `1` and `0`,
how do we represent characters?

The ASCII standard assigns numbers to characters
and encodes those numbers in 7 bits.
Commonly, a byte is used to hold those bits.

For example, ASCII uses the number `65` to represent the character `A`.

Here's some Java code to check this out:

```java
char c1 = 65;
System.out.println(c1);
```

Will print the character A.

However, a byte can have only 256 values.
That's not enough for characters of all languages.

That's where UNICODE comes in.
It assigns numbers ('code points') to represent characters
in all known scripts, and to represent symbols and emoticons as well.

Modern compilers and Operating Systems are aware of Unicode characters.

Here's code to print the 'Rupee' symbol. It is assigned the number `8377` in Unicode.

```java
char c1 = 8377;
System.out.println(c1);
```

Will print the symbol &#8377;
