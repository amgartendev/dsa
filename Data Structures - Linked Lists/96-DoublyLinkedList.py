"""
What is a Doubly Linked List?

Doubly Linked List is very similar to Singly Linked Lists with only one exception. Doubly Linked Lists points not only
for the next value in the list but also for the previous value.

Why is it so important? Well, we can't traverse backwards in a Singly Linked List but we can in a Doubly Linked List.
Also, searching in a Doubly Linked List can actually be a little bit more efficient. Its lookup Big O Notation is still
O(n), but can be O(n/2) if we know in which half of the list we are looking for we can pick the optimum place to start.

Now the downside to a Doubly Linked List is that we might have to hold a a little bit more of memory to store the new
pointer.
"""
