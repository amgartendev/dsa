class LinkedList:
    def __init__(self, value: int) -> None:
        self.head: dict = {"value": value, "prev": None, "next": None}
        self.tail: dict = self.head
        self.length: int = 1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\n\thead: {self.head}\n\ttail: {self.tail}\n\tlength: {self.length}\n)"

    def prepend(self, value: int) -> object:
        new_node = {"value": value, "prev": None, "next": None}
        new_node["next"] = self.head
        self.head["prev"] = new_node
        self.head = new_node
        self.length += 1
        return self

    def append(self, value: int) -> object:
        new_node: dict = {"value": value, "prev": None, "next": None}
        new_node["prev"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def insert(self, index: int, value: int) -> object:
        leader_node = self.traverse_to_index(index-1)
        target_node = leader_node["next"]
        
        self.length += 1
        return self

    def traverse_to_index(self, index: int) -> dict:
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        return current_node


linked_list = LinkedList(10)
print(linked_list)
print(linked_list.append(6))
print(linked_list.prepend(1))
print(linked_list.insert(1, 99))
