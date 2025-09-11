# Lists: ordered, mutable sequences

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
nested = [[1, 2], [3, 4]]

print("Numbers:", numbers)
print("Mixed:", mixed)
print("Nested:", nested)

# Indexing and slicing
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice 2..4 (exclusive):", numbers[1:4])

# Modifying elements (lists are mutable)
numbers[0] = 10
print("After modifying first element:", numbers)

# Inserting and extending
numbers.append(6)  # add at the end
print("After append(6):", numbers)

numbers.extend([7, 8])  # extend with another iterable
print("After extend([7, 8]):", numbers)

numbers.insert(1, 99)  # insert at index 1
print("After insert(1, 99):", numbers)

# Removing elements
numbers.remove(99)  # removes first matching value
print("After remove(99):", numbers)

popped = numbers.pop()  # removes and returns last item
print("Popped value:", popped)
print("After pop():", numbers)

popped_index = numbers.pop(0)  # removes by index
print("Popped index 0:", popped_index)
print("After pop(0):", numbers)

# Searching and counting
vals = [1, 2, 2, 3, 3, 3]
print("vals:", vals)
print("Index of first '2':", vals.index(2))
print("Count of '3':", vals.count(3))

# Sorting
unsorted_nums = [5, 2, 9, 1, 5]
print("Unsorted:", unsorted_nums)

sorted_copy = sorted(unsorted_nums)  # returns a new list
print("sorted(list):", sorted_copy)
print("Original unchanged:", unsorted_nums)

unsorted_nums.sort()  # in-place sort
print("After .sort():", unsorted_nums)

words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)  # sort by length
print("Words sorted by length:", words)

words.reverse()  # reverse in place
print("Words reversed:", words)

# Copying lists (avoid aliasing)
a = [1, 2, 3]
alias = a  # both names point to the same list
copy1 = a.copy()
copy2 = a[:]  # slicing copy

a.append(4)
print("a:", a)
print("alias (same object):", alias)
print("copy1 (separate):", copy1)
print("copy2 (separate):", copy2)

# List comprehension
nums = list(range(10))
squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
labels = [f"even-{n}" if n % 2 == 0 else f"odd-{n}" for n in nums]

print("nums:", nums)
print("squares:", squares)
print("evens:", evens)
print("labels:", labels)

# Nested list comprehension (matrix flatten)
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [x for row in matrix for x in row]
print("matrix:", matrix)
print("flattened:", flattened)

# Common patterns
print("Sum of nums:", sum(nums))
print("Min and max:", min(nums), max(nums))
print("Is 3 in nums?:", 3 in nums)

print("Enumerate with index:")
for idx, value in enumerate(["a", "b", "c"], start=1):
    print(idx, value)

