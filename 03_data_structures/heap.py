class BinaryHeap:
    def __init__(self, *, is_min=True):
        self._data = []
        self._is_min = is_min

    def _compare(self, child, parent):
        return child < parent if self._is_min else child > parent

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self._compare(self._data[index], self._data[parent_index]):
                self._data[index], self._data[parent_index] = (
                    self._data[parent_index],
                    self._data[index],
                )
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        n = len(self._data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            target = index

            if left < n and self._compare(self._data[left], self._data[target]):
                target = left
            if right < n and self._compare(self._data[right], self._data[target]):
                target = right

            if target == index:
                break
            self._data[index], self._data[target] = self._data[target], self._data[index]
            index = target

    def push(self, value):
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty heap")
        top_value = self._data[0]
        last_value = self._data.pop()
        if self._data:
            self._data[0] = last_value
            self._heapify_down(0)
        return top_value

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def __repr__(self):
        kind = "min" if self._is_min else "max"
        return f"BinaryHeap({kind}={self._data})"


if __name__ == "__main__":
    print("Min-heap example:")
    tasks = BinaryHeap(is_min=True)
    for priority in [5, 3, 8, 1, 4]:
        tasks.push(priority)
        print("push", priority, "->", tasks)

    while tasks:
        print("pop ->", tasks.pop())

    print("\nMax-heap example:")
    leaderboard = BinaryHeap(is_min=False)
    for score in [42, 75, 23, 88, 57]:
        leaderboard.push(score)
        print("push", score, "->", leaderboard)

    while leaderboard:
        print("pop ->", leaderboard.pop())
