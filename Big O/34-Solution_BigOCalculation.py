def fun_challenge(input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(input)):  # O(n)
        def another_function():  # O(n)
            return
        stranger = True  # O(n)
        a += 1  # O(n)
    return a  # O(1)


fun_challenge([1])


"""
Explanation:

Line 1 - We have a function called "fun_challenge" that take some sort of an input, but the input doesn't really
matter. It could be an array, an object, etc. For now, let's keep things simple and let's say it is an array of five.

Line 2 - The first thing we do when we run this function is an assignment. We're going to assing variable "a" as ten.
Some people say that you shouldn't count assignments as Big O, and some people say you should. In our case, just to
simplify things, let's count every single step and what the function is doing. So, "a = 10" is O(1) because this in 
only running once, don't matter how big our input is.

Line 3 - We're reassigning "a". This once again, is O(1)

Line 5 -  Now we get into a loop. We know that with the loop it looks like we're going at the length of the input and
looping over depending on whatever the input is. In our case, this is going to be O(n).

Line 6 - Now we have another function, we don't know what this function is, but it's calling to another function
outside of the "fun_challenge" function. This is also being called N times, depending on how big our input is. So once
again, it's O(n).

Line 8 - Another random assignment here, but this runs as many times as this loop happens. If input was five, this will
run five times. So again, this will be O(n).

Line 9 - Here we're just incrementing our "a" variable, and as we loop through it, it'll keep incrasing by 1. This once
again, runs O(n) times.

Line 10 - And then finally, another thing that some people don't count, bust just to keep it consistent let's consider
it. This runs just once, so it is O(1).


Now we can start thinking of how a function runs and how efficient a function is. If we actually calculate all of these,
if we total all these up, we see that we have three times O(1) and four times O(n). It should look something like this:

3 + n + n + n + n
3 + 4n

BIG O(3 + 4n)

But in the end of the day, we will see that it just gets simplified to O(n).
We will see why that is later.
"""
