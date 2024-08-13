"""
As the name suggests, it's a list that is linked.

All right, that's not very helpful.

Well, I have a little diagram here for you. Open the file named "LinkedListsDiagram.png" located in this same directory while reading this
lesson.

A list or in this case, as we'll find out soon, a singly Linked List, contains a set of notes and think of nodes
as those blocks. Both red and green block together is a note.

Those notes have two elements the value of the data you want to store, in the case of the first block, the number
five and a pointer to the next node in line.

So you can see the green block points to the next node. The first node is called the head and the last node is
called the tail.

Now, depending on some people, some people like to call the tail anything that is after the head. So including the block
in the middle. But I prefer the term tail referring to the very last note.

Finally, Linked Lists are what we call null terminated, which signifies that it's the end of the list.

So we know that the last block is the tail node because it points to null, there's nothing coming after it.
Now pointer is a term that you hear a lot in programming and computer science.

And we have a lesson coming up discussing what a pointer actually is, but to focus just on length lists
for now.

You can see that it's a very simple data structure. It's simply an element that links to the next element
that links to the next element. And it keeps going, keeps going, keeps going until the last element 
that points to null.

You can have them sorted, you can have them unsorted and you can have notes pretty much contain any
sort of data type.

But let's take a look at some pseudocode.

# Up until now, we learned how arrays work
basket = ["apples", "grapes", "pears"]

# How can we have a basket that is not an array, but a Linked List?
# Well, we can just say that our Linked List will contain apples that then points to grapes

linked list: apples --> grapes --> pears  # This is just a pseudocode. A diagram.

# A more accurate diagram would be something like this:
apples
8947 --> grapes
         8742 --> pears
                  372 --> null

# The numbers represents the memory address and the arrows are the pointers
# Python does not have a built-in linked list library in its standard library. However, linked lists can be implemented
# using classes and references in Python.
"""