class MyArray:
    def __init__(self):
        self.__length = 0
        self.__data = {}

    def infos(self):
        return {'length': self.__length, 'data': self.__data}

    def push(self, item):
        self.__data[self.__length] = item
        self.__length += 1
        return self.__data

    def pop(self):
        if self.__length > 0:
            last_item = self.__data[self.__length-1]
            del self.__data[self.__length-1]
            self.__length -= 1
            return last_item
        return

    def delete(self, index):
        return self.shift_items(index)

    def shift_items(self, index):
        deleted_item = {index, self.__data[index]}

        for i in range(index, self.__length-1):
            self.__data[i] = self.__data[i+1]
        del self.__data[self.__length-1]
        return deleted_item


new_array = MyArray()

print(new_array.infos())
new_array.push('a')
new_array.push('b')
new_array.push('c')
new_array.push('d')
new_array.push('e')
new_array.push('f')
new_array.pop()
print(new_array.infos())
print(new_array.delete(2))
print(new_array.infos())
