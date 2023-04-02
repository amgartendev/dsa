def booooo(n):
    for i in range(len(n)):
        print('boooooo!')


booooo([1, 2, 3, 4, 5])


"""
We know the time complexity of that function is O(n). But when it comes to space complexity...

The one gotcha when it comes to space complexity is that when we talk about space complexity, we're talking about
aditional space. So we don't include space taken up by the inputs. So we don't really care how big the input is.

So within that function, are we adding any space?
Well, not really. The only thing we're really doing is we're creating that 'i' variable for the for loop, and that's it.
Other than that, we're not really adding any more memory. 

So this function has a space complexity of O(1).
"""


# But what if we have a function like this?


def array_of_hi_n_times(n):
    hi_array = []
    for i in range(n):
        hi_array.append('hi')
    return hi_array


print(array_of_hi_n_times(6))


"""
All we're doing is we're creating a new array and for the number of items in our input, we're going to just fill up
hi_array with repeatedly 'hi' string.

But, what is the space complexity of this?

Remember our cheatsheet?
What causes space complexity is:
- Variables
- Data Structures
- Function Call
- Allocations

All those things take space. And in our case, we created variables in our loop. Variable 'i'.
But we've also created data structures, we created a new array.

So we have O(n + 1), but remember the rule "drop constants". So we have O(n).
"""
