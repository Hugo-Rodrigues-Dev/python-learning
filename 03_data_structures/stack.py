class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)


undo_stack = Stack()
undo_stack.push("type 'hello'")
undo_stack.push("type 'world'")
undo_stack.push("delete last char")

print("Stack size:", undo_stack.size())
print("Top of stack:", undo_stack.peek())
print("Pop:", undo_stack.pop())
print("Pop:", undo_stack.pop())
print("Is empty?:", undo_stack.is_empty())

