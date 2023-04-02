"""
What happens if we have nested loops? What is the Big O of this kind of function?

One common interview question that you might get is something along the lines of:
"""

# Log all pairs of array
BOXES = [1, 2, 3, 4, 5]


def log_all_pairs_of_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(f"{array[i]} {array[j]}")


log_all_pairs_of_array(BOXES)

"""
What is the Big O of that function? A good role of thumb is if you see nested loops, you are going to use * character
instead of +.

So this becomes O(n * n) that turns into O(n^2).

O(n^2) --> Quadratic Time

An easy rule of thumb is: any step that happens in the same indentation, you add, and anything that happens with
indentation that is nested, you multiply.
"""
