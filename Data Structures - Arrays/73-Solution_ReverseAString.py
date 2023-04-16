# Create a function that reverses a string:
# 'Hi My Name is Andrei' should be:
# 'ierdnA si eman yM iH'


def reverse_string(string):
    # Check input
    if not isinstance(string, str) or len(string) < 2:
        return 'hmm that is not good'

    backwards = []
    total_items = len(string) - 1

    for i in range(total_items, -1, -1):
        backwards.append(string[i])

    return ''.join(backwards)


def reverse_string2(string):
    # Check input
    if not isinstance(string, str) or len(string) < 2:
        return 'hmm that is not good'
    return string[::-1]


def reverse_string3(string):
    # Check input
    if not isinstance(string, str) or len(string) < 2:
        return 'hmm that is not good'
    return ''.join(reversed(string))


print(reverse_string('Hi My Name is Andrei'))
print(reverse_string2('Hi My Name is Andrei'))
print(reverse_string3('Hi My Name is Andrei'))
