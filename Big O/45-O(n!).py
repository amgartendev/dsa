"""
Let's talk about a Big O notation that you're most likely not going to encounter. And if you're writing any code that
has this Big O notation, you're definitely doing something wrong. It's the most expensive one, it's the steepest of
them all. This is called factorial time, or as I like to call it, the O(no). Here's an example of a O(n!)


def factorial_permutations(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    permutations = 1
    for j in range(1, result+1):
        permutations *= j
    return permutations


print(factorial_permutations(100))


The chances you have to encounter this Big O notation is very, very rare. This notation adds a nested loop for every
input that we have.
"""
