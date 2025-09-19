class Queue:
    def __init__(self):
        self._items = []
        self._front_index = 0

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self._front_index >= len(self._items):
            raise IndexError("dequeue from empty queue")
        value = self._items[self._front_index]
        self._front_index += 1
        # Compact the underlying list occasionally to avoid unbounded growth
        if self._front_index > 50 and self._front_index * 2 > len(self._items):
            self._items = self._items[self._front_index :]
            self._front_index = 0
        return value

    def peek(self):
        if self._front_index >= len(self._items):
            return None
        return self._items[self._front_index]

    def is_empty(self):
        return self._front_index >= len(self._items)

    def size(self):
        return len(self._items) - self._front_index


support_queue = Queue()
support_queue.enqueue("Password reset")
support_queue.enqueue("Refund request")
support_queue.enqueue("Bug report")

print("Queue size:", support_queue.size())
print("Next ticket:", support_queue.peek())
print("Handle:", support_queue.dequeue())
print("Handle:", support_queue.dequeue())
print("Queue empty?:", support_queue.is_empty())

