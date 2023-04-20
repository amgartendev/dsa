# Given 2 arrays that are sorted
# Merge these two arrays into one big one that's still sorted
# The function takes two parameters

def merge_sorted_arrays(array1, array2):
    merged_array = []
    array1_item = array1[0]
    array2_item = array2[0]
    i = 0
    j = 0

    # Check input
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    while array1_item or array2_item:
        print(str(array1_item) + ' - ' + str(array2_item))
        if array1_item < array2_item:
            merged_array.append(array1_item)
            array1_item = array1[i]
            i += 1
        else:
            merged_array.append(array2_item)
            array2_item = array2[j]
            j += 1

    return merged_array


print(merge_sorted_arrays([0, 3, 4], [4, 6, 30]))
