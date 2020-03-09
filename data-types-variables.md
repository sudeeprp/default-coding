# Data types and Variables

A data-type determines the kind of operations that are possible on the data.
Different languages treat data-types differently. Let's explore.

`2 + 2` evaluates to `4`. The data-types involved are integers.

However, `"2" + "2"` evaluates to `"22"`,
since the data-types involved are strings.

## C and C++

In C and C++, we fix the type of the variable before using it.
For example, `unsigned short int` says that we have an integer that's
expected to take only positive values.
On most computers, a variable of this type will occupy 16 bits.

This statement declares a variable of this type and initializes it to zero:

```C
unsigned short int i = 0;
```

Just for fun, let's decrement `i` after the above initialization?

```C
i--;
```

Decrementing `0` gives `-1`, but `i` is unsigned, so what may happen?
Try it out and see!

See [here](https://www.tutorialspoint.com/cplusplus/cpp_data_types.htm)
for an introduction to the data types provided by C++.

## C\#

The C# syntax treats variables and their types similar to C++.
However, that's where the similarity ends.
C# data-types determine if their variables are Values or References.

Types like `int`, `float`, `double` are value types. Their value gets copied on assignment.

Types like `string` are reference types.
Their variables simply hold a reference to the real thing.
So assigning them does not copy the actual value, it only copies the reference.

See [this article](https://medium.com/omarelgabrys-blog/understanding-data-types-in-c-7ccf4547d639)
for a discussion about values and references.

## Java

Java treats variables similarly with Value and Reference types.
There is a subtle difference - in C#, everything is an object,
while that's not the case in Java.

## The problem of Equality

The equality operator often leads to un-intentional mistakes.
In this section, we look at equality-checks of strings and floating-point decimals.

### Comparison of String objects in Java

Consider the following piece of code:

```Java
String s1 = "12345";
String s2 = "123";
s2 += "45";
if(s1 == s2) {
    System.out.println(s1 + " equals " + s2);
} else {
    System.out.println(s1 + " does NOT equal " + s2);
}
```

Strangely, this code reports that the strings are not equal:

`12345 does NOT equal 12345`

Why is that? How do we fix this?

Notice the fix in the equality check below (`==` isn't used).

```Java
String s1 = "12345";
String s2 = "123";
s2 += "45";
if(s1.equals(s2)) {
    System.out.println(s1 + " equals " + s2);
} else {
    System.out.println(s1 + " does NOT equal " + s2);
}
```

Now it looks ok:

`12345 equals 12345`

The behavior in C# is similar. See [this article](https://www.c-sharpcorner.com/UploadFile/3d39b4/difference-between-operator-and-equals-method-in-C-Sharp/)
for an illustration.

### Floating point equality

Another frequent source of mistakes is to test for floating-point equality.
For example:

```C#
float f1 = 6.0 / 4.0;
float f2 = 12.0 / 8.0;
if(f1 == f2) {
    Console.WriteLine("Floating points are equal!");
}
```

Here's the funny thing: it may or may not pass the equality!
The reason is in the representation of floating point numbers
in a computer. Depending on how the floating point is computed,
there can be small differences in the values, which is not
significant for calculations, but can fail the equality check.

See [this article](https://floating-point-gui.de/errors/comparison/)
for more details.
