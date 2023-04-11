"""
In order to truly understand the value of data structures, we have to go deep down into the way computer works at the
fundamental level. In order for a computer to run code, it needs to keep track of things like variables, like numbers,
strings, array. These variables are stored in what we call Random Access Memory (or RAM for short). That's how programs
run.

On top of that, we also have storage where we store things like our video files, music files, documents. And the storage
can be a disk drive, a flash drive, or a solid state drive. Data on storage is permanent or what we call persistent.
So when you turn off your laptop or computer, it's still going to be there when you turn it back on.

In RAM, you lose the memory when the computer turns off. So why wouldn't we just always use storage, so we don't lose
any data? Well, the problem is that persistent storage is slow. A computer is run by its CPU. You can think of the CPU
as the little worker that does all the calculations that we need. It does the actual work inside our computer. And this
CPU needs access to the RAM and the storage, but it can access the RAM and the information in the RAM a lot faster. But
let see an example as if we're using Google: When we run Google Chrome, for example, a browser. That Google Chrome
browser has a piece of code.

Let's say it is:
chrome = 1

We simplified it, and we just created a variable 'chrome' equals one. But we can imagine how we have hundreds, thousands
of lines of code of Google Chrome. Now, in order for our computer to run Google Chrome, we run the CPU for it to do so.

Now when a variable is declared in, let's say, a script to run Google Chrome, it's going to hold that in memory, in our
Random Access Memory. But once we turn off or close Google Chrome, we want to be able to reopen it, right? That's what
we do when we save an application on our computer, we save it to storage so that next time we open up Google Chrome, the
CPU is going to grab the program from the storage so that it can use it again. And for Google Chrome to run fast and run
smaller scripts, it's going to keep that information in the Random Access Memory.

So you can think of RAM in the computer as a massive storage area, kind of like a data structure. This massive storage
area has shelves that are numbered. We call these address or addresses, and it's a really, really big shelf that holds
a lot of information, and it allows us to run programs. It kind of looks like this:

RAM:
-------- | --------
ADDRESS  | CONTENT
0        | 00000001
1        | 00100001
2        | 00000001
3        | 01100001
4        | 00000001
5        | 00000001
6        | 11000001
7        | 010000001

Each of these shelves holds what we call eight bits or numbers. Each one of these numbers is a bit. And a bit is a tiny
electrical switch that can be turned on or off. But instead of calling it on or off, we call it one or zero and eight
bits is called a byte. Each shelf has one byte of storage, and the CPU is connected to something called a memory
controller, and a memory controller does the actual reading of this memory as well as writing this memory, because
sometimes the shelf might be blank and doesn't have anything.

This direct connection to the CPU is important because the CPU asks them RAM: "Hey, what's in shelf number 0?", and the
memory controller actually has connections individually to all of these shelves.

This is very important because it means that we can access the zero shelf and immediately access the seven shelf, or
the 10781º shelf without having to climb down or step down. That's what Random Access Memory really means. We can access
memory really fast because we have these connections any shelf we want, we just need to know which shelf we're looking
for.

Even though this memory controller can jump between far apart memory addresses really fast, programs tend to access
memory that is nearby. The closer the information is to the CPU and the less it has to travel, the faster a program can
run.

And to further optimize this, our computers also have what we call a CPU cache, where the CPU has a tiny, tiny memory,
where it stores a copy of stuff that is really recent. And this is called cache.

A common one that you might hear is something called LRU cache.

So again, if we use Google Chrome as an example: we turn on Google Chrome, we have our application downloaded on our
storage, the CPU loads it up and because we've visited hackernews.com it's going to load up the information for that
Hacker News and put it into memory or maybe even cache if it can hold it.

So why is this important for Data Structures?
Remember, data structures are ways for us to store information. For example, if we want to store a variable 'A'
equals one, well, in our modern computers, usually we represent integers. That is the number one in 32 bits.

Number 1 in 32 bits:
RAM:
-------- | --------
ADDRESS  | CONTENT
0        | 00000000
1        | 00000000
2        | 00000000
3        | 00000001

That block size of RAM is the number 1 in 32 bits. And by the way, this now can be 64 bits with more and more recent
upgrades. But this way we can store the number 1 within this block of 32 bits.

Why 32 bits? Because we have 8 bits (which is 1 byte) in the address 0, plus 8 bits in address 1, 2, 3, and 4.
So 8x4=32

If we have another variable 'B' equals to seven, we would store it in the next block with address 4 to 7.

Here is the following amount of information that each system can hold:
8-bit  -> 255
16-bit -> 65.536
32-bit -> 2.147.483.647
64-bit -> 9.223.372.036.854.775.807

In programming, there is something called Integer Overflow. The idea is that a computer can only store a certain number
of information.

Using the following code:

import math
print(math.pow(6, 100))   ->  Output: 6.533186235000709e+77
print(math.pow(6, 1000))  ->  Output: OverflowError: math range error

What is that?
Well, as the number becomes too large to store in our RAM, then wee need to represent this number that we cannot store
into something that is tangible. We can only store this much information and no matter how big you make the code above,
any number above a certain threshold is going to raise an exception in Python. In Javascript it returns "Infinity".

I showed you this because other data types other than numbers work the same way. Each data type has a number of bits
associated with it, and that need to get stored in the system. And the system allocates that storage and then the CPU
reads from that storage.

Here's a link for you so that you can get more information if you want:
https://www.youtube.com/watch?v=fpnE6UAfbtU&ab_channel=CrashCourse
https://statmath.wu.ac.at/courses/data-analysis/itdtHTML/node55.html


We don't want to get too deep in this, but a data structure is this. A data structure is an arrangement of data. You
can define the way you interact with this data and how it is arranged in RAM. So some data strucures in RAM are
organized right next to each other, some are organized apart from each othe, and they have different pros and cons on
access and write.

Our goal is to minimize the operation that we need to do for the CPU to get the information for the CPU to write
information. And that's why data structures are so powerful.
"""
