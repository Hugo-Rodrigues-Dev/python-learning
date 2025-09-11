# Tuples: ordered, immutable sequences

# Creating tuples
empty = ()
single = (1,)  # note the trailing comma for single-element tuple
coords = (10, 20)
mixed = (1, "two", 3.0)

print("empty:", empty)
print("single:", single)
print("coords:", coords)
print("mixed:", mixed)

# Indexing and slicing
print("First of coords:", coords[0])
print("Slice coords[:]:", coords[:])

# Immutability (cannot modify in place)
try:
    coords[0] = 99
except TypeError as e:
    print("Cannot modify tuple:", e)

# Packing and unpacking
packed = 1, 2, 3  # tuple packing without parentheses
a, b, c = packed  # tuple unpacking
print("packed:", packed)
print("unpacked:", a, b, c)

# Swapping values (classic Python trick)
x, y = 5, 10
x, y = y, x
print("Swapped:", x, y)

# Returning multiple values as a tuple
def min_max(values):
    return min(values), max(values)

mn, mx = min_max([5, 2, 8, 1])
print("min_max ->", mn, mx)

# Tuple methods: count and index
letters = ("a", "b", "a", "c")
print("letters:", letters)
print("count('a'):", letters.count("a"))
print("index('c'):", letters.index("c"))

# Tuples can be dictionary keys (immutable and hashable)
locations = {
    (40.7128, -74.0060): "New York",
    (48.8566, 2.3522): "Paris",
}
print("locations:", locations)

# Converting between tuple and list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print("Converted to list and modified:", lst)
print("Original tuple unchanged:", t)

print("Back to tuple:", tuple(lst))

