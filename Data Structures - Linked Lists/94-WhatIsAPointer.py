"""
A pointer is simply a reference to another place in memory.

A pointer in Python can be done like this:
obj1 = {"a": True}
obj2 = obj1

We are not copying the object, we are not saying "obj1 is equals obj2". We are pointing our obj2 to the same
location in memory that our obj1 is located.

We can check it by doing this:
print(obj1)  # {'a': True}
print(obj2)  # {'a': True}

If we change obj1...
obj1["a"] = "booya"
print(obj1)  # {'a': 'booya'}
print(obj2)  # {'a': 'booya'}

Both obj1 and obj2 changed because we created a pointer saying that obj2 is going to reference obj1 and they
both point to the same location in memory.

Let's see a fun thing

obj1 = {"a": True}
obj2 = obj1
print(obj1)  # {'a': True}
print(obj2)  # {'a': True}
del obj1
# print(obj1)  # Error: name 'obj1' is not defined
print(obj2)  # {'a': True}

We still have our obj2 as True even though we deleted obj1. What happened? Well, the way it works in most programming
languages is that our computers are going to delete the memory that is unused, and because it sees that obj2 is still
referencing the {"a": True} location in memory, its not going to delete it because there is still a pointer to this
location in memory.

This is what you might call "Garbage Collection". As soon as we set:
obj2 = "Hello"

Now, obj2 what referenced the memory space that had {"a": True} is now just simply a string. Because Python has
Garbage Collection, that is memory is managed automatically, the {"a": True} gets automatically garbage collected and
deleted because nothing is pointing to it. However, there are low level languages where you have to manage your own
memory and you have to manually delete the referenced item in memory and this can cause a lot of possible issues where
you leave memory that is not being used in memory, which is a valuable resource. But then, there are also benefits with
no Garbage Collection languages where you get to manage your own memory so you can make things really fast and efficient.
"""