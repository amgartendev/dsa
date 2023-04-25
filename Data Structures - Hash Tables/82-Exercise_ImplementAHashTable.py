"""
It's time for us to implement our own Hash Table.

But let's do a bit of an exercise, and this may be difficult, so don't get upset if you are not able to finish it.
After this, I'll provide a solution file (83-Solution_ImplementAHashTable) and we'll walk through it.

Here is the explanation of the previous built template:
1. We have created a class
2. We have a constructor that will receive N size (N shelves of memory)
3. We have created an attribute self.__data where our data will live, that will receive an array to hold the information
4. We have a method called '_hash' to get the unicode key for each char passed as key as parameter and returns us a hash

-- GOALS --
1. You will have to implement a method called 'set', and you have to my able to set 'grapes' as the first index in
the array and the number of grapes as the second index in the array.

2. You will have to implement another method called 'get' which retrieves the grapes and returns the number of grapes,
i.e: 10000.
"""


class HashTable:
    def __init__(self, size):
        self.__data = []

    def data(self):
        return self.__data

    def set(self, key, value):
        my_dict = {key: value}
        self.__data.append(my_dict)

    def get(self, key):
        return self.__data[0][key]

    def _hash(self, key):
        my_hash = 0
        for i in range(len(key)):
            my_hash = (my_hash + ord(key[i]) * i) % len(self.__data)
        return my_hash


my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))
print(my_hash_table.data())
