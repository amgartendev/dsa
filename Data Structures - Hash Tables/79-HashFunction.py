"""
What is a Hash Function?

It's something that's used all across computer science.
A Hash Function is simply a function that generates a value of fixed length for each input that it gets.

What does that mean?

In the link below you will have a URL to MD5 Hash Generator

MD5 Hash Generator: https://www.miraclesalad.com/webtools/md5.php

MD5 is the type of Hash Function and there's many, many types. You might have heard of SHA-1, SHA-256, and many others.
Using this Hash Function, let's see what happens if we write "Hello":

"Hello" -> 8b1a9953c4611296a827abf8c47804d7

MD5 hashes this string and turns it into that gibberish. That's what a Hash Function does. We give it an input and
the function generates some random pattern.

Now there's some key aspects of Hash Functions.
- First is that it's one way. In the sense that if I give somebody this: 8b1a9953c4611296a827abf8c47804d7, they have no
idea what the input was, and it's practically impossible for me to have any clue as to what the input is.

- Second is that no matter how many times you put "Hello" in that text box, it's going to be the same. But as soon as
you change one thing, it's going to completely change the output. That is called idempotent. It's a fancy way to say
that a function given an input will always output the same output. Now, the one benefit and why we would want to use
this in a data structure is that we get really fast data access, because all we have to do to find grapes, or
basket.grapes is to passs grapes into something like an MD5 Hash.

basket.grapes -> 048db1d6caf8e4ffef0ab75c4fde5701

It generates that number, and we immediately know where it is in memory on our computer.
It doesn't look like an address, does it?
Technically a Hash Function that we use for Hash Tables is going to take grapes, generate some sort of gibberish (hash
code), and then convert it to an index space or an address space it has based on this number.

Unlike arrays where we just had ordered indexes, with Hash Tables, all we need to do is give it a key, and we know
exactly where that item is in our memory.

But you might be wondering
That Black Box that we have talked before, the Hash Function. Doesn't it slow things down?

If you noticed that, good job, that is a big factor. You don't want your Hash Function to take a very long time because
every time you add property to memory or retrieve a property to memory, we both times we're sending the key 'grapes'
into the Hash Function to find where to get it from. We need this to be really, really fast.

And underneath the hood, remember, because Hash Tables exist in all languages, they're implemented with an optimum
hashing function that's really, really fast.

As a side note: Hash Functions like SHA-256 take a really long time to generate a hash, and it is an overly complex
hashing function that is used a lot in places like cryptography where you want this to take loner, but that is outside
the scope of this course.

-- TO REVIEW --

We have a key that is 'grapes'.
We send it through a Hash Function that is going to hash something really, really fast and then map whatever the hash
came out to be into a memory address where we want to store our data, in this case, grapes 10.000.

And when it comes to Hash Functions, you typically leave this to whatever framework or language you're using, and we
usually assume a Time Complexity or Big O Notation of O(1), because this happens really fast.
"""
