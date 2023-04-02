import math


def print_first_item_then_first_half_then_say_hi_100_times(items):
    print(items[0])

    middle_index = math.floor(len(items) / 2)
    index = 0

    while index < middle_index:
        print(items[index])
        index += 1

    for i in range(100):
        print('Hi')


"""
Yes, I know... Probably not the best named function ever

If we calculate all the operations, it should look something like this:

Line 5: O(1)
Line 7: O(1)
Line 8: O(1)

Line 10: O(n/2) --> Because we are looping only half the input length
Line 11: O(1)
Line 12: O(1)

Line 14: O(100) --> This is a bit of a trick. We are not looping over the items array, we just have 100
Line 15: O(1)

Big O(3 + n/2 + 2 + 100 + 1)

But Rule #2 states we want to drop the constants. We simply are saying that we don't really care about all that numbers.
Remember in an interview, we only care about the things that we saw on the chart (BigOChart.png), not specific like
this.

So O(3 + n/2 + 2 + 100 + 1) turns into O(n/2 + 1). In the grand scheme of things, we only 
care about when it scales, when the inputs are getting larger and larger. So, as N gets bigger and bigger, we don't care
about adding an extra 100 if N is a million, because if N is a million, adding an extra 100 on there, another 100 steps
doesn't really matter. 

And same with n/2, we drop the constants. So now we have O(n + 1). And because we have N, we can drop the 1 aswell,
even if it is a million. So in the end of the day, we have O(n).

!! FINAL ANSWER: that function above has an O(n) complexity.
"""


# What if we have two for loops?

def compress_boxes_twice(boxes):
    for box in boxes:  # O(n)
        print(box)

    for box in boxes:  # O(n)
        print(box)


"""
We have two O(n) loops, and because this is two separate steps, we add them together. So it becomes O(2n). But again,
in an interview it doesn't really matter. We have to drop the constants, so O(2n) turns into O(n).
"""
