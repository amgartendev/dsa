"""
Looking at Hash Functions, we can start to think about what actions they perform and how fast it can be done.
When it comes to

Insert - inserting something in our memory space it's going to be O(1). We hash the key such as 'grapes'
through the Hash Function and places it automatically into the address space that it comes up with.

Lookup - is the exact same. We accessed the property, that property is going to get hashed and direct us exactly
to the address to find the values.

Delete - same thing. We simply use the key right away. We know where to delete the item from and because it isn't
ordered, we don't have to shift indexes like we did with arrays. Everything is just nice and simple.

Search - if we want to find something in our basket like apples, we simply use Hash Functions.

In Python, we can do:
user = {'age': 54, 'name': 'Kylie', 'magic': True, 'scream': 'aaaaah!'}

I've created a user dictionary and the age 54, name Kylie, magic True, scream aaaaah are all going to get placed
somewhere in memory at different addresses.

But we can access it really, really fast. We can say user['age'] and it will return us the age of the user in a Time
Complexity of O(1).

Perhaps, adding a new property, we can simply say user['spell'] = 'abra kadabra'.
print(user) --> {'age': 54, 'name': 'Kylie', 'magic': True, 'scream': 'aaaaah!', 'spell': 'abra kadabra'}

We can see now the spell 'abra kadabra' added. And accessing this new property will also be O(1).

And you might be thinking: "Hash Tables are amazing! We should be using them all the time".
And you're right, we should be using them in a lot of cases. But as we know, there's always pros and cons.

Now let's talk about one of the main problems with Hash Tables. And I have a nice visual to demonstrate this for you.
Go to this link -> https://www.cs.usfca.edu/~galles/visualization/OpenHash.html

We have 12 memory spaces (those rectangles with a black line inside). Remember, our computer has limited space and when
we create an object or a Hash Table, the computer decides how much space to allocate. It's not going to allocate all
the space to the Hash Table, it's going to allocate a bit of it (I'll show you later on when we implement our own
Hash Table how we can adjust the size).

But seeing that there's only 12 spaces, you can imagine if I insert 1 (in the insert button on the top), 3, 55, and
keep inserting numbers, at some point the Hash Function will randomly assign a space and memory and put it in some space
that might be already assigned.

Remember, there's nothing telling the Hash Function to evenly distribute until everything is full. Although
Hash Functions are optimized to try to distribute this data all over, it also matters what we put into it. So when
55 gets hashed, this Hash Function generates the address location of three to put it in. And because we already have
three there, it does something funny. It is called Collision.

Theoretically, when you have a collision, it slows down reading and writing with a Hash Table with O(n/k) where k is
the size of your Hash Table. And remember, because we remove constants and simplify things, it becomes an O(n).

And luckily for us, we're never going to have to really implement it by ourselves. And it's not a very common interview
question, but you do want to know about it, so you can talk about it. There's two common ways to deal with these
collisions. One of them is Linked Lists (we are going to see it later on).

There are a lot of ways to deal with collisions and if you want to check them, you can read the Hash Table wikipedia
and then goes to "Collision" section

Hash Table Wikipedia -> https://en.wikipedia.org/wiki/Hash_table
Hash Table Collision Resolution -> https://en.wikipedia.org/wiki/Hash_table#Collision_resolution

When we talk about fast lookups and Hash Tables, occasionally, depending on the Hash Function, it might take O(n).
"""
