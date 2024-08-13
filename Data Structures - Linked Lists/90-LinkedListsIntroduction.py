"""
We are going to see two types of Linked Lists: singly and doubly Linked Lists.

What problem do we encounter with arrays?
With static arrays, we only have a certain amount of data (or memory) that can be allocated next to each other in memory.

But then, both dynamic arrays and static arrays can increase their memory once it hits a certain limit and double up that
memory in another location. But that operation every once in a while of doubling up the array in order to create more memory,
had a performance implication and it cost us O(n).

Additionally, arrays also had bad performance for any sort of operations like insert and delete that had to shift indexes over,
especially when you inserted or deleted anywhere that wasn't the end of the array.

And then came hash tables. They were great. We pretty much store things wherever we wanted and memory and hash tables would just take care
of it for us and know where to place it in memory. We didn't have to worry about some problems that came with the arrays.

Life was good, but unfortunately they weren't really ordered. So how can we solve this problem?
Linked Lists is the answer!

So does this mean we all should just be using link lists all the time and disregard arrays and hash tables because Linked Lists are
the best data structures?

Nope. As always, there are trade offs when it comes to data structures.
"""