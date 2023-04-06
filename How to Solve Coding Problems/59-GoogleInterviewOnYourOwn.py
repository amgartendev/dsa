# always array - N array length
# target_sum can receive integers or float numbers
# output should be True/False


def has_pair_with_sum(arr, target_sum):
    my_set = set()
    for item in arr:
        if item in my_set:
            return True
        my_set.add(target_sum - item)
    return False


print(has_pair_with_sum(arr=[4, 2, 5], target_sum=7))

