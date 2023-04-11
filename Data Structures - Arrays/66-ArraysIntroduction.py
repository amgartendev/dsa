"""
Arrays (sometimes called lists) organizes items sequentially.

Arrays are probably the simplest and most widely used data structure. And luckily for us, we're starting with this
because arrays have the least amount of rules and because they're stored in contiguous memory, that is in order. They
also have the smallest footprint of any data structure.

So if all you need is to store some data and iterate over it, that is go one by one, step by step, arrays are the best
choice. Especially if you know the indices of the items you're storing.
"""

strings = ['a', 'b', 'c', 'd']  # 4 * 4 = 16 bytes of storage
numbers = [1, 2, 3, 4, 5]

# append - O(1)
strings.append('e')

# pop - O(1)
strings.pop()
strings.pop()

# insert - O(n)
strings.insert(0, 'x')
strings.insert(2, 'alien')

print(strings)
