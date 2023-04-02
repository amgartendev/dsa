BOXES = [0, 1, 2, 3, 4, 5]


def compress_first_box(boxes):
    print(boxes[0])


compress_first_box(BOXES)  # O(1) --> Constant Time


# What about this?

def log_first_two_boxes(boxes):
    print(boxes[0])  # O(1)
    print(boxes[1])  # O(1)


log_first_two_boxes(BOXES)  # O(2)

# When it comes to constant time, we don't care about the nitty gritty O(1), O(2), 0(3), O(100)... We round this down
# to simply saying O(1).
