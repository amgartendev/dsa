def find_pair_with_sum(array, target_sum):
    my_set = set()
    for item in array:
        if item in my_set:
            return True
        my_set.add(target_sum - item)
    return False


print(find_pair_with_sum(array=[4, 1, 5]*10_000, target_sum=7))
