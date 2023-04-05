"""
Give 2 arrays, create a function that let a user know (true/false) whether these two arrays contain any common items

For example:
    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'i']
    It should return False

    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'x']
    It should return True

Make sure to follow the "Step by Step through a problem" on your Cheatsheet
"""

# 2 parameters - arrays - no size limit
# return True or False


"""
array1_false = ['a', 'b', 'c', 'x']
array2_false = ['z', 'y', 'i']

array1_true = ['a', 'b', 'c', 'x']
array2_true = ['z', 'y', 'x']


# Brute Force Solution

def contains_common_item(array1, array2):  # Big O(a * b)
    for item in array1:
        for item2 in array2:
            if item == item2:
                return True
    return False
    

But we can make this function better and more optimized than O(a*b)
"""
