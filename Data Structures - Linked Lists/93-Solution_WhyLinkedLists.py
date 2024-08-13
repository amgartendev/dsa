"""
I hope you are able to think about why Linked Lists might be good or bad in this lesson.

Let's discuss the answer.

One key thing that you may have seen is that length lists have a sort of loose structure that
allows you to insert a value into the middle of the list.

By simply resetting a few pointers, I can insert anything that I want and the only changes
that happen is somewhere in the middle of my Data Structure. Just like you saw if you
used the provided link for the Algorithm Visualization.

And this is the same for deleting node in a Linked List. And we remember with an array data
structure how when we wanted to insert something that wasn't at the end of the array, we had
to add the item, let's say in memory space one into here and then shift all the items down
and index it down, which costs us a lot of time. It costs us O(n).

The main difference between arrays and Linked Lists is that in an array, an element or elements
are indexed. So if I wanted to go to item at index five, I can do that easily. In a Linked List,

You start at the head and traverse the list until you get to item five, which is O of RN.
And this idea of traversal is the same as iteration that we did with the arrays where we go zero,
one, two, three, four, five. Except we like to call this traversal because you don't really know
when the length list will end. You start from the head and you keep going until you hit null.

And as you'll see in our coding example, we're going to have to use something like a while loop
when we implement our own length lists because we don't usually know how long the list is going
to be.

Another advantage that an array might have is that most computers have caching systems that make
reading from sequential memory.

That is memory right next to each other, shelves right next to each other, faster than reading
scattered addresses. And that's something that we've talked about already.

Array items are always located right next to each other in computer memory. Linked lists and nodes
instead are actually scattered all over memory, kind of like hash tables.

So iterating through a Linked List or traversing through a Linked List is usually quite a bit slower
than iterating through items like an array, even though they're technically both O(n). However, these
inserts that we can do in the middle of a Linked List is a lot better than an array.

What about hash tables?

Well, just like hash tables, when we insert something into a Linked List, we just scatter it all over our
memory and we can just keep adding it and we don't have to do any of the on shifting or shifting on the
indexes that we did with the arrays, which is really, really nice.

You can also delete notes very easily versus with an array. But the one advantage that it has over hash
tables is that there is some sort of order to Linked List.

Each node points to the next node so you can have sorted data unlike a hash table. So if we look at
our Big O of Linked Lists:

prepend - O(1) - add to the beginning of a Linked List
append - O(1) - add to the end of the list
lookup - O(n) - also called traversal
insert - O(n) - add in a certain index
delete - O(n) - delete a certain index

Now you're thinking to yourself: "Hold on, insert and delete and erase are also O(n). So how is that better?"
And that's something that we're going to get into when we actually take a look at the code. Remember, that
table above are the worst cases, in which case we insert or delete the very last item, and most of the times
that won't be the case in Linked Lists.
"""