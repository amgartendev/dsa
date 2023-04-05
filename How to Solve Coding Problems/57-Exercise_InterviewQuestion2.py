array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'w']


def contains_common_items(arr1, arr2):  # O(a+b)
    # 1. Loop through first array and create object where properties equal items in the array
    # 2. Loop through second array and check if item in second array exists on created object

    array_map = {}
    for i in range(len(arr1)):
        if arr1[i] not in array_map:
            item = arr1[i]
            array_map[item] = True

    for j in range(len(arr2)):
        if arr2[j] in array_map:
            return True
    return False


print(contains_common_items(array1, array2))
