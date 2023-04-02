NEMO = ['nemo']
EVERYONE = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
LARGE = ['nemo'] * 100_000


def find_nemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO!')


print(find_nemo(LARGE))  # O(n)  --> Linear Time

