def print_all_numbers_than_all_pair_sums(numbers):
    print('These are the numbers:')
    for number in numbers:
        print(number)

    print('and these are their sums:')
    for first_number in numbers:
        for second_number in numbers:
            print(f'{first_number} + {second_number} = {first_number + second_number}')


print_all_numbers_than_all_pair_sums([1, 2, 3, 4, 5])

"""
Again... Not the best name for a function ever, but it's just for learning purposes

In the function above we are passing 'numbers' as parameter to our function. That can be an array, for example.
Then we are looping through the array and printing all numbers within the array. 
And finally we are creating nested for loops to sum the first and second number.

What do you think the Big O notation here is? 

Our first foor loop has a Big O of O(n), and our nested for loop has a Big O of O(n^2). So we have O(n + n^2).
But rule number four states that we want to drop the non dominant terms. That means we care about the most important
term. In this case, we actually drop the N. So our Big O of O(n + n^2) turns into O(n^2) because as the input increases,
the size of O(n^2) is way more important than O(n). So we always just keep the dominant term.

Let me give you another example, a little bit harder this time:

Let's say we have calculated the Big O of a function and the result was 
O(x^2 + 3x + 100 + x/2)

Well, in this case we will have a function with O(n^2) complexity. Let's see why:
Let's say that our X equals 5.

5^2 = 25
3x5 = 15
100 = 100
5/2 = 2.5

You can say that in this case, the dominant term is 100, but remember, with Big O, we're worried about scale and as
things grows larger and larger and larger. So when X becomes 500:

500 ^ 2 = 250000
3x500 = 1500
100 = 100
500 / 2 = 250


Fun fact here: if we have another for loop inside our nested loop, our Big O is now O(n^3), because we have 3 nested
layers, and you can keep going. 

But, here's the thing: if you have 3 nested loops, 99.99% of the time, that's usually a bad idea. It scales really
really badly, and most of the time you're doing something wrong.
"""
