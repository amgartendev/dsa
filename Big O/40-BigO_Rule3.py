# First of all, let me ask you a question
# What if I have boxes as the first parameter, and then I have boxes2 as the second parameter

def compress_boxes_twice(boxes, boxes2):
    for box in boxes:
        print(box)

    # And the second loop
    for box in boxes2:
        print(box)


"""
What is the Big O of that function? Is it still O(n)?

No. And during an interview, a lot of people trip up and say that this is still O(n), it is not.

Because the third rule states that different terms for inputs, and remember boxes: boxes and boxes2 are two different
inputs. Boxes could be 100 items long, and boxes2 could be just 1 item. So the first for loop is going to depend on
how big the first input is, and then the second for loop depends on how big boxes2 is.

This Big O of that function wuold be something like:
O(a) --> first loop
O(b) --> second loop
O(a + b)
"""
