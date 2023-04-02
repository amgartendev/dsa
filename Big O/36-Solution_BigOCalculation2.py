def another_fun_challenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in range(len(input)):  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(len(input)):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    who_am_i = "I don't know"  # O(1)


"""
Explanation: 

Line 1 - We have a function called "another_fun_challenge" that take some sort of input, it could be an object, an array,
etc. It doesn't really matter.

Line 2,3,4 - We are just assigning variables once. So it will be O(1).

Line 5 - We have a for loop that is running based on the input. We don't know what that input is, but we can assume
that we're looping based on however long this input is. So it will be O(n).

Line 7,8,9 - In each iteration of our loop, we are reassigning those variables. It's an O(n).

Line 11 - Same thing as our previous loop, we don't know what the input is, but we can just assume that we're looping
based on however long this input is. O(n) again.

Line 12,13 - Those variables are being reassigned inside the loop, which is running N times. Those variables have an
O(n) complexity.

Line 15 - This line just runs once, because it is not inside the loop. So it has an constant time O(1).
"""