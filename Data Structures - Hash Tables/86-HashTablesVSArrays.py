"""
Why Hash Tables?
Hash Tables are great when you want quick access to certain values. We remember that searching through an array for
an item takes a really long time. We have to loop through every item and see if a certain string or a certain number
is in an array. With Hash Tables that's really, really fast.

And that's why you see Hash Tables in places like databases. We want to search for something in a database, and it
gives it back to us right away.

Similarly, inserting items in a Hash Table, unlike an array that might shift indexes, is typically O(1). You just simply
have to Hash and create the key. Although we have those cases of collision most of the time, that's something that we
don't need to worry about too much, and we can assume an insert of O(1).

Then there's other aspects that are quite similar between the two.
Arrays let you quickly look up the value for a given key. Keys are called indexes in an array, and we don't get to pick
them, it's always 0 1 2 3... In Hash Tables we can pick them.

So Hash Tables is kind of like a hack on top of an array to let us use flexible keys instead of being stuck with
0 1 2 3...

A problem with Hash Tables that we discussed was the idea of no concept of order. In arrays each item was placed next
to each other on a shelf in memory. Hash Tables are kind of placed all over the place.

Now that we have an idea of the differences between the two, I think it's time for us to actually work on some
exercises and interview questions that will use Hash Tables in their answers.
"""
