class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def get_data(self):
        return self.data

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                keys_array.append(self.data[i][0][0])
        return keys_array

    def _hash(self, key):
        my_hash = 0
        for i in range(len(key)):
            my_hash = (my_hash + ord(key[i]) * i) % len(self.data)
        return my_hash


my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
my_hash_table.set('apples', 54)
my_hash_table.set('apples', 30)
my_hash_table.set('oranges', 2)
print(my_hash_table.keys())
