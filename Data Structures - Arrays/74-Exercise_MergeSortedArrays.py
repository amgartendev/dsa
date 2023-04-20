# Given 2 arrays that are sorted
# Merge these two arrays into one big one that's still sorted
# The function takes two parameters

def merge_sorted_arrays(array1, array2):
    merged_array = []
    i = 0
    j = 0

    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    return merged_array


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
