class MyArray:
    def __init__(self):
        self.__length = 0
        self.__data = {}

    def infos(self):
        return {'length': self.__length, 'data': self.__data}

    def push(self, item):
        self.__data[self.__length] = item
        self.__length += 1
        return self.infos()

    def pop(self):
        last_item = self.__data[self.__length-1]
        del self.__data[self.__length-1]
        self.__length -= 1
        return last_item

    def delete(self, index):
        return self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.__length-1):
            self.__data[i] = self.__data[i+1]
        del self.__data[self.__length-1]
        self.__length -= 1
        return index


new_array = MyArray()
print(new_array.infos())
print(new_array.push('a'))
print(new_array.push('b'))
print(new_array.push('c'))
print(new_array.push('d'))
print(new_array.pop())
print(new_array.delete(1))
print(new_array.infos())
