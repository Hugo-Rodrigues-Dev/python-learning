# Lambda expression
square = lambda x: x ** 2
print("Square of 4:", square(4))

# Using lambda with sorted()
points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda p: p[1])
print("Sorted by y-value:", sorted_points)

# Using map
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print("Squares:", squared)

# Using filter
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)

# Lambda with reduce to compute product
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print("Product:", product)

# Sorting by string length
words = ["banana", "kiwi", "apple", "strawberry"]
sorted_words = sorted(words, key=lambda w: len(w))
print("Words sorted by length:", sorted_words)

# Filter strings with more than 5 letters
long_words = list(filter(lambda w: len(w) > 5, words))
print("Words with more than 5 letters:", long_words)