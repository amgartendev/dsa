# Google Question
# Given an array, tell me the first recurring character
# Given an array = [2, 4, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [2, 3, 4, 5]
# It should return None


# Naive Approach -> Different problem where you need to find the first recurring character for i
def first_recurring_character_naive(array):  # O(n^2)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return array[i]
    return None


# Better Approach
def first_recurring_character(array):  # O(n)
    my_dict = {}
    for index, value in enumerate(array):
        if my_dict.get(value) is not None:
            return value
        else:
            my_dict[value] = index
    return None


# Bonus Challenge - Fix the first solution to work properly
def bonus_challenge(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i+1] == array[j+1]:
                return array[i+1]
    return None


print('------ NAIVE SOLUTION -------')
print(first_recurring_character_naive(array=[2, 4, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character_naive(array=[2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character_naive(array=[2, 3, 4, 5]))


print('------ HASH TABLE ------')
print(first_recurring_character(array=[2, 4, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character(array=[2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_character(array=[2, 3, 4, 5]))


print('------ BONUS CHALLENGE ------')
print(bonus_challenge(array=[2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(bonus_challenge(array=[2, 5, 5, 2, 3, 5, 1, 2, 4]))
