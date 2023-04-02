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
Answer: the function above has an O(n) complexity since we loop loop through the number of elements in our input.
If we calculate all the operations, it should look something like this:

4 + n + n + n + n + n + n + n
4 + 7n

BIG O(4 + 7n)

But in the end of the day, we just say it is an O(n).
"""
