# Sets: unordered collections of unique, hashable elements

# Creating sets
empty_set = set()  # {} is a dict, use set() for empty set
nums = {1, 2, 3, 3, 2, 1}  # duplicates are removed
letters = set("banana")  # from iterable

print("empty_set:", empty_set)
print("nums (unique):", nums)
print("letters from 'banana':", letters)

# Adding and updating
nums.add(4)
print("After add(4):", nums)

nums.update([4, 5, 6])  # add multiple from iterable
print("After update([4, 5, 6]):", nums)

# Removing elements
nums.remove(6)  # KeyError if not present
print("After remove(6):", nums)

nums.discard(999)  # safe: does nothing if absent
print("After discard(999):", nums)

popped = nums.pop()  # removes and returns an arbitrary element
print("pop() ->", popped)
print("After pop():", nums)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("a:", a, "b:", b)
print("Union a | b:", a | b)
print("Intersection a & b:", a & b)
print("Difference a - b:", a - b)
print("Symmetric diff a ^ b:", a ^ b)

# Relations
subset = {1, 2}
superset = {1, 2, 3, 4}
print("subset <= a:", subset.issubset(a))
print("superset >= a:", superset.issuperset(a))
print("Disjoint with {9}?:", a.isdisjoint({9}))

# Set comprehension
squares = {n * n for n in range(6)}
evens = {n for n in range(10) if n % 2 == 0}
print("squares set:", squares)
print("evens set:", evens)

# Removing duplicates from a list using set
data = [1, 2, 2, 3, 3, 3]
unique = set(data)
print("unique from list:", unique)
print("back to list (unordered):", list(unique))

# frozenset: immutable set (hashable, can be dict key)
fs = frozenset({1, 2, 3})
print("frozenset:", fs)

mapping = {fs: "immutable-key"}
print("dict with frozenset key:", mapping)

