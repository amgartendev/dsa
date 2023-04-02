import time

# Let's measure the scalability of the previous code
# When whe talk about scalability, we are talking about how much our code slow down as we add more and more inputs

NEMO = ['nemo']
EVERYONE = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
LARGE = ['nemo'] * 100_000


def find_nemo(array):
    time_start = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('Found NEMO!')
    time_finish = time.time()
    return time_finish - time_start


print(find_nemo(LARGE))
