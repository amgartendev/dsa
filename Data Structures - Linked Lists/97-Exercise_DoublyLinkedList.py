"""
Try implementing your own Doubly Linked List before reviewing the solution.
"""


class DoublyLinkedList:
    def __init__(self, value):
        self.head = {"value": value, "previous": None, "next": None}
        self.tail = self.head
        self.length = 1
    
    def __repr__(self):
        return f"{self.__class__.__name__}(\n\thead: {self.head}\n\ttail: {self.tail}\n\tlength: {self.length}\n)"

    def prepend(self, value):
        new_node = {"value": value, "previous": None, "next": None}
        new_node["next"] = self.head
        self.head["previous"] = new_node
        self.head = new_node
        self.length += 1
        return self

    def append(self, value):
        new_node = {"value": value, "previous": None, "next": None}
        new_node["previous"] = self.tail
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
        new_node = {"value": value, "previous": None, "next": None}
        new_node["previous"] = lead_node
        new_node["next"] = lead_node["next"]
        lead_node["next"]["previous"] = new_node
        lead_node["next"] = new_node
        self.length += 1 
        return self
    
    def remove(self, index):
        # Idk
        pass

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        return current_node


linked_list = DoublyLinkedList(10)
print(linked_list.append(5))
print(linked_list.append(16))
print(linked_list.prepend(1))
print(linked_list.insert(2, 99))
print(linked_list.remove(2))
