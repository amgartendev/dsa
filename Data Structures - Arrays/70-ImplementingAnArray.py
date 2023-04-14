"""
In this lesson we are going to be using the class syntax in Python. So we're going to create an array class, even
though with Python and many other languages we can do this:

array = []

Let's see if we can build one of our own, because as you'll find out as we go through this course, Data Structures are
simply things that we can build from scratch. We can create whatever Data Structure we want, we can create our own.

The most common Data Structures are well known and are already implemented in most languages because they are so useful.
But you are able to build any Data Structure you want from scratch. And as you'll find out, most Data Structures are
built on top of other Data Structures.
"""


class MyArray:
    def __init__(self):
        self.__length = 0
        self.__data = {}

    def infos(self):
        return {'length': self.__length, 'data': self.__data}

    def get(self, index):
        return self.__data[index]

    def push(self, item):
        self.__data[self.__length] = item
        self.__length += 1
        return self.__length

    def pop(self):
        last_item = self.__length-1
        del self.__data[self.__length-1]
        self.__length -= 1
        return last_item

    def delete(self, index):
        item = self.__data[index]
        self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.__length-1):
            self.__data[i] = self.__data[i+1]
        del self.__data[self.__length-1]
        self.__length -= 1


new_array = MyArray()
new_array.push('hi')
new_array.push('you')
new_array.push('!')
new_array.delete(0)
new_array.push('are')
new_array.push('nice')
new_array.delete(1)

print(new_array.infos())
