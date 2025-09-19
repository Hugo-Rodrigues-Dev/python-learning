class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value!r})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        self.head = Node(value, next_node=self.head)

    def insert_after(self, target, value):
        current = self.head
        while current and current.value != target:
            current = current.next
        if current:
            current.next = Node(value, next_node=current.next)

    def find(self, target):
        current = self.head
        while current:
            if current.value == target:
                return current
            current = current.next
        return None

    def delete(self, target):
        if not self.head:
            return False
        if self.head.value == target:
            self.head = self.head.next
            return True
        prev = self.head
        current = self.head.next
        while current:
            if current.value == target:
                prev.next = current.next
                return True
            prev, current = current, current.next
        return False

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


contacts = SinglyLinkedList()
contacts.append("Alice")
contacts.append("Bob")
contacts.append("Charlie")
print("Initial contacts:", contacts.to_list())

contacts.prepend("Admin")
print("After prepend('Admin'):", contacts.to_list())

contacts.insert_after("Bob", "Dave")
print("After insert_after('Bob', 'Dave'):", contacts.to_list())

print("find('Charlie'):", contacts.find("Charlie"))
print("delete('Alice'):", contacts.delete("Alice"))
print("After delete('Alice'):", contacts.to_list())

