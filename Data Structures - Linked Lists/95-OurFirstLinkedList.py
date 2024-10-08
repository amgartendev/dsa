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
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"{self.__class__.__name__}(\n\thead: {self.head}\n\ttail: {self.tail}\n\tlength: {self.length}\n)"

    def prepend(self, value):
        new_node = {"value": value, "next": None}
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        return self

    def append(self, value):
        new_node = {"value": value, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return self

        if index == self.length:
            self.append(value)
            return self

        lead_node = self.traverse_to_index(index-1)
        new_node = {"value": value, "next": None}
        new_node["next"] = lead_node["next"]
        lead_node["next"] = new_node
        self.length += 1 
        return self

    def remove(self, index):
        lead_node = self.traverse_to_index(index-1)
        target = lead_node["next"]
        lead_node["next"] = target["next"]
        self.length -= 1
        return self

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        return current_node


linked_list = LinkedList(10)
print(linked_list)
print(linked_list.prepend(1))
print(linked_list.append(5))
print(linked_list.append(16))
print(linked_list.insert(3, 99))
print(linked_list.remove(3))