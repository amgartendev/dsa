"""
Hash Tables or Hash Maps, Maps, Unordered Maps, Dictionaries, Objects... There are many ways to call this Data Structure
and different languages has different names for it and slightly variations on the Hash Tables.

Objects for example, in JavaScript, are a type of Hash Table. The reason we are starting our studies with Arrays and
Hash Tables is that these are the most common interview questions. You're going to use them in any coding question.
They are an absolute must.

Now, luckily for us, pretty much every language has a built-in hash table, just like arrays.
In Python, they're called dictionaries.

And Hash Tables are very important all across computer science. You see them a lot in databases and caches, and they're
extremely useful.

So what are they? And also, you may be wondering, what does the name Hash Table means? Where did this name come from?
Imagine you're going grocery shopping, and you have an object (array) basket, and you want to add grapes as the property
of the basket object.

So we want to set that basket.grapes = 10_000. We are buying 10.000 grapes because you can never have too many grapes.
Now, first off, thinking about how we would store this with arrays. It would be a little bit more difficult, right?.

In an array we have an index that's humbered and a value. With a Hash Table or a Dictionary, we get to set a key, which
is grapes and a value. So we get to set a key value pair.

Now a way a hash table works is we have the key, which is grapes. And this key is used as the index of where to find
the value in memory. Remember with the arrays we had the index, which was the number, but with Hash Tables, we use
'grapes' as a way to find it in our memory shelf.

This is done with something called 'Hash Function', but for now let's just assume this is a black box. We don't know
what's going on there. All that's going to happen is we're going to pass grapes into this black box, this black box is
going to do some magic, and out of it comes a key into an index where we want to store this value (in our case 10.000,
because we want 10.000 grapes). So now our 10.000 grapes can be stored in a memory address.
And technically it actually stores both 'grapes' the key and the value of 10.000.

So that black box gets to decide where to put the data on our memory in our computers. But you might be wondering
'What is that black box called Hash Function? And why does it get to decide where to put all this information?'.

For that, see the next file called 79-HashFunction
"""
