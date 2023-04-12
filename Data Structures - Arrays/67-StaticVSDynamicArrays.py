"""
There are two types of arrays. One is called Static Array, and the other Dynamic Array.

What is the difference between the two?
The one limitation of Static Arrays is that they're fixed in size, meaning you need to specify the number of elements
your array will hold ahead of time. For example:

0 - Juice
1 - Apple
2 - Cheese
3 - Kale
4 - Mango
5 - Grapes
6 - Eggs
7 - Bread

So in this case, If this was a static array, I would say create an array of seven items knowing beforehand that in my
grocery list I'm only going to have max seven items. Because arrays are allocated in adjacent blocks of memory when
they're created, there's no guarantee that after we've allocated seven shelves of memory that you can keep addings
things on, especially in order.

We solve this problem with static arrays that require us to say ahead of time how many items we want into our array
with Dynamic Arrays.

Dynamic Arrays allows us to copy and rebuild an array at a new location, which with more memory if we wanted more
memory. So for example, with our static array, if we realize that we forgot another item on our list, and we need eight
items, what happens is we copy this entire array. We allocate 14 blocks of memory and paste this list, plus the eighth
item into that new location.

# Static Arrays in C++
int a[20];  <- Create an array thas has space of 20 items


But luckily for us, we never had to worry about reallocate memory. And that's because in Python and other languages
like JavaScript, where you have lists and ArrayList in Java, they work like Dynamic Arrays. They automatically allocate
memory according to the increase in size of the array.

So right off the bat, you're thinking Dynamic Arrays are way better and easier, because I don't have to think about
memory because of automatic resizing. And that ghets into a discussion of managing memory which low level languages like
C++ allow, while higher level languages like JavaScript or Python allow us to not think about memory and let the machine
take care of it for you. There's times when maybe you do want to manage your memory and times when you don't need to
based on your needs. Obviously, having more control over memory allows you to really tweak things and make things
faster, and that's why languages like C++ can be much faster than higher level languages.

But we don't need to get into that. What we want to get out of this lesson is that dynamic array expands as you add more
elements, so you don't need to determine the size ahead of time.
"""
