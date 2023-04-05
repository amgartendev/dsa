# Naive Solution

def has_pair_with_sum(arr, target_sum):
    len_array = len(arr)
    for i in range(len_array-1):
        for j in range(i+1, len_array):
            if arr[i] + arr[j] == target_sum:
                return True
    return False


# Better Solution

def has_pair_with_sum2(arr, target_sum):
    my_set = {}
    len_array = len(arr)
    for i in range(len_array):
        if arr[i] in my_set:
            return True
        my_set[target_sum - arr[i]] = True
    return False


print(has_pair_with_sum([1, 2, 4, 4], 8))
print(has_pair_with_sum2([1, 2, 4, 4], 8))
