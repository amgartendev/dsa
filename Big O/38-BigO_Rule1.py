NEMO = ['nemo']
EVERYONE = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
LARGE = ['nemo'] * 100_000


def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO!')
            break


print(find_nemo(LARGE))


"""
The very first rule is: we always care about what is the worst scenario case, because when we talk about scalability,
we can't just assume things are going well, even though the "find_nemo" function might be O(1) in the best scenario (if
nemo is the first item of the array), it doesn't matter in the grand scheme of things because we can't be certain of
what the input is going to be. So, we're going to say that function is O(n), linear time. 
"""
