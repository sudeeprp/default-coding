# Functions and Arguments

We group together a set of instructions into a function.
It is interesting to see how scope and arguments are handled
within functions, in different languages. Let's take a look.

You can try out all code-snippets here by clicking
'Enter focus mode' in [this site](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/intro-to-csharp/list-collection?tutorial-step=1)

Consider this C# function called `incrementIt`.
It takes an integer and tries to increment it, unsuccessfully though:

```C#
void incrementIt(int i) {
    i += 4;
}

int p = 5;
incrementIt(p);
Console.WriteLine($"After incrementing: {p}");
```

This code will output:

```console
    After incrementing: 5
```

So it didn't increment at all!
Only the value of `p` was passed to the function. Modifications made inside
the function have no effect outside.
The scope of `i` is restricted to the function `incrementIt`.
Its lifetime (also called 'extent') is also within that function itself.

Consider another C# function, which removes 'the' from a list of strings:

```C#
void removeThe(List<String> strArray) {
    strArray.Remove("the");
}

var names = new List<string>
  { "I", "saw", "the", "crow" };
Console.WriteLine($"{names.Count} elements before removeThe");
removeThe(names);
Console.WriteLine($"{names.Count} elements after removeThe");
```

We see:

```console
    4 elements before removeThe
    3 elements after removeThe
```

This code passes the List called `names` and
the function `removeThe` changes the list by removing a string from the list.
If only the value of `names` was passed into the function,
it should have remained unchanged!

In C#, the List is passed by reference.
So the function was seeing the same `names` List.

Here we see C# treats value-types (like `int`)
different from reference types (like `List`),
while passing them as arguments to functions.

Here is a catch: Changing the entire array seems to behave differently:

```C#
void changeIt(List<String> strArray) {
    strArray = new List<string>
        {"one", "two"};
}

var names = new List<string>
  { "I", "saw", "the", "crow" };

Console.WriteLine($"{names.Count} elements before changeIt");
changeIt(names);
Console.WriteLine($"{names.Count} elements after changeIt");
```

What's going on? The array didn't change!

```console
    4 elements before changeIt
    4 elements after changeIt
```

Can you reason this out?
