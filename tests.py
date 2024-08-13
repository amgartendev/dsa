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
        if index == 0:
            self.prepend(value)
            return self

        if index >= self.length:
            self.append(value)
            return self

        new_node = {"value": value, "next": None}
        leader_node = self.traverse_to_index(index-1)
        holding_pointer = leader_node["next"]
        leader_node["next"] = new_node
        new_node["next"] = holding_pointer
        self.length += 1
        return self
    
    def remove(self, index):
        leader_node = self.traverse_to_index(index-1)
        target = leader_node["next"]
        if index == 0:
            self.head = target["next"]
            self.length -= 1
            return self
        
        leader_node["next"] = target["next"]
        self.length -= 1
        return self

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        return current_node


my_linked_list = LinkedList(10)
print(my_linked_list)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
print(my_linked_list)
print(my_linked_list.remove(2))
