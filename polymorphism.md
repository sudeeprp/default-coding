# Polymorphism

It means 'occurring in different forms'.
Often, we need 'one logic' to work
with different types of things in the real world.

For example, an army would have different types of equipment
from different manufacturers. Yet, they need one application
to keep track of them.
While operating machinery remotely in a battle,
you don't want to worry about the company that provided each equipment.

Let's take a case and dive into polymorphism.

Suppose our job is to write a program
that fires a row of different types of artillery machines.

![artillery range](images/artillery.png "artillery range")

They look alike, but are made by different companies.
Each company has provided its own function to fire the projectile.
For example, the Howitzer equipment has a function called 'howitzer_v1_fire',
while Dhanush provides a function called 'dhanush_fire' and so on.

All these functions accept an equipment-identifier
to distinguish the one to be fired,
since we may have multiple equipment from the same company.

A piece of code that fires them in quick succession may look like this:

```C
void synchronized_fire() {
  howitzer_v1_fire("GUN_ID1");
  dhanush_fire("GUN_ID2");
  bofors_v2_fire("GUN_ID3");
  howitzer_v2_fire("GUN_ID4");
  dhanush_fire("GUN_ID5");
}
```

This is a function in C, which
returns nothing (so the `void`) and accepts nothing (so the `()`).
It has a series of instructions, firing different guns.
Firing is a very quick action, so this sequence fires all of them
almost simultaneously.

Notice that we have two versions of Howitzer (v1 and v2),
only the new Bofors (v2) and two Dhanush instances.
We have provided an ID to each function, so it knows which one to fire.

> It works, so what's the problem?

The function needs to be modified every time a gun is added. Is that an issue?

The issue becomes clear if we consider one more method of firing,
rather than just the plain sequence.
What about firing alternate guns at a time?
Let's say we want to fire guns in odd-positions first,
then the ones in even-positions.
The commanders decides what they want, based on the situation.

The code to fire guns in odd-positions looks like this:

```C
void fire_odd_positions() {
  howitzer_v1_fire("GUN_ID1");

  bofors_v2_fire("GUN_ID3");

  dhanush_fire("GUN_ID5");
}
```

And to fire those in even-positions:

```C
void fire_even_positions() {
  dhanush_fire("GUN_ID2");

  howitzer_v2_fire("GUN_ID4");
}
```

Now you can see what happens if we purchase a new type of gun:
We need to change three functions:
`synchronized_fire` to fire simultaneously,
`fire_odd_positions` and `fire_even_positions` as illustrated above.

As they purchase more guns and add more firing patterns, the effort
keeps increasing. This could even give a competitive edge to the enemy!

How do we make the logic of 'fire all', 'fire odd' and 'fire even'
work on different arrangement of guns?
Can we keep these functions unchanged on future purchases too?
The same logic needs to take place in different forms of gun-arrangement.

Function pointers in C provide a method to achieve polymorphism.
In fact, they are one of the ingredients in the C++ object model as well.
See [here](https://www.learn-c.org/en/Function_Pointers)
for a quick refresher on C function pointers.

What we need is 'a function to fire the guns one by one'.
Let's first outline the function that fires all guns:

```C
void synchronized_fire(/* accept array of guns here */) {

   //iterate through the array
   //and fire each element in there

}
```

The `synchronized_fire` function now takes an array of different types of guns.
The caller determines the type and sequence.
The function just fires all of them. With this, we've removed the logic
of 'which gun' and 'how to fire' from this function.

Then where do we put the logic of firing each gun? Let's try a struct:

```C
struct Gun
{
  char gun_id[32];
  void (*fire)(int);
}
```

Observe that the struct `Gun` has two members.
One is a noun (the gun identification)
and another is a verb (the activity of firing), which is a
[pointer to a function](https://www.learn-c.org/en/Function_Pointers).
It could be made to point to any function that accepts an `int`
and returns nothing.

Let's now write the `synchronized_fire` function, which we outlined above.
Remember that an array in C always needs to be accompanied by its length:

```C
void synchronized_fire(struct Gun[] guns, unsigned int n_guns) {
   for(int i = 0; i < n_guns; i++) {
      guns[i].fire(guns[i].gun_id);
   }
}
```

As you can see, this function now doesn't care about the types of guns,
as long as the structure is constructed properly.

How about the functions to fire guns in odd- and even-positions?

```C
void fire_odd_positions() {
   for(int i = 1; i < n_guns; i += 2) {
      guns[i].fire(guns[i].gun_id);
   }
}

void fire_even_positions() {
   for(int i = 0; i < n_guns; i += 2) {
      guns[i].fire(guns[i].gun_id);
   }
}
```

None of these functions need to be re-written when we get a new gun.

That is the strength of polymorphism!
It comes from the ability of the 'fire' function-pointer
to point to different functions in different structures-
it takes on 'different forms' in different contexts.

To complete the story:
All this is fine only if we fill an array of `Gun` structures.
Here's one way to construct the array.

```C
struct Gun guns[] = {
  { .gun_id = GUN_ID1, .fire = howitzer_v1_fire },
  { .gun_id = GUN_ID2, .fire = dhanush_fire },
  { .gun_id = GUN_ID3, .fire = bofors_v2_fire },
  { .gun_id = GUN_ID4, .fire = howitzer_v2_fire },
  { .gun_id = GUN_ID5, .fire = dhanush_fire }
};
```

This is a structure-array initializer written as per the C99 standard.
It's ok if you don't recognize the syntax.
The important point is that the type and IDs of the guns
need to be known at initialization time.

What did we achieve?
We've isolated the impact of adding a new type of gun to the
initialization part of the program, leaving all other functions untouched.

That's a great way to separate concerns, which is vital in large projects
with many development teams.
