"""
It's time to create our first Linked List data structure.

Let's say we want to create a Linked List that has:
10-->5-->16
"""

my_linked_list = {
    "head": {
        "value": 10,
        "next": {
            "value": 5,
            "next": {
                "value": 16,
                "next": None
            }
        }
    }
}

class LinkedList:
    def __init__(self, value):
        new_node = {"value": value, "next": None}
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def __repr__(self):
        return f"{self.__class__.__name__}(\nhead: {self.head},\ntail: {self.tail},\nlength: {self.length}\n)"
    
    def append(self, value):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = {"value": value, "next": None}
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, value):
        if index > self.length:
            return False

        current_node = self.head
        count = 0
        while current_node != None:
            current_node = current_node["next"]
            count += 1
            if count == index:
                print(current_node)


my_linked_list = LinkedList(10)
print(my_linked_list)
print(my_linked_list.append(5))
print(my_linked_list.append(16))
print(my_linked_list.prepend(1))
my_linked_list.insert(2, 99)
