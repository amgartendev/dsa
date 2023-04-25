# Google Question
# Given an array, tell me the first recurring character
# Given an array = [2, 4, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]
# It should return None


def first_recurring_character(array):
    my_set = set()
    for item in array:
        if item in my_set:
            return item
        my_set.add(item)
    return None


print(first_recurring_character(array=[2, 4, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character(array=[2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character(array=[2, 3, 4, 5]))
