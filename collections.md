# Collections

As the name indicates, collections collect objects. For example, in C:

```C
char s[30];
```

The variable `s` is a collection of 30 characters and can be used as a string.

In Java, an array of languages can be declared and accessed this way:

```java
ArrayList<String> languages = new ArrayList<String>(
            Arrays.asList("C++",
                          "C#",
                          "Java",
                          "JavaScript"));
System.out.println(languages.get(2));
```

The above code will print will access the element at position `2` and print `Java`.

Let's move on to C#. Here's code in C# to deal with a list of strings,
but it has a bug.

```C#
var names = new List<string>
  { "nobita", "bheem", "oggy", "oggy cockroach", "ninja" };

foreach (var name in names)
{
    if(name.StartsWith("oggy")) {
        Console.WriteLine($"Need to remove {name}!");
        names.Remove(name);
    }
}
```

This code tries to remove names starting with "oggy" from a list.
Try it in the interactive editor
(click 'Enter focus mode' in [this site](https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/intro-to-csharp/list-collection?tutorial-step=1))

Does it work? No!
Which is the line that's causing the crash? Try resolving it!
