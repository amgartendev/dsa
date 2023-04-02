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
In our previous exercises we were doing a bit of calculations to determine our Big O complexity, but in interviews,
you are never going to do this. Most of the time when you go into interviews, there's some rules that we are going
to follow, where you dont need to that calculations, but just taking a look at the function and immediately say what
type of Big O it is.

Rule 1: Worst Case
Rule 2: Remove Constants
Rule 3: Different terms for inputs
Rule 4: Drop Non Dominants

We are going to create separate examples for each rule to better understanding.
"""
