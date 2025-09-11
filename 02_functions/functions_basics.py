def greet(name):
    # Return a friendly greeting string for the given name.
    return f"Hello, {name}!"

def add(a, b=1):
    return a + b

def area_rectangle(length, width=1):
    # Compute the area of a rectangle.
    return length * width

def is_even(number):
    # Return True if the number is even, else False.
    return number % 2 == 0

def to_upper(text):
    # Return `text` converted to uppercase (does not modify original).
    return text.upper()

def say_hello(name="Friend"):
    # Print a friendly message.
    print(f"Hi {name}, how are you?")

def average(a, b, c=0):
    # Compute the average of 2 or 3 numbers.
    return (a + b + c) / (3 if c else 2)

# Example usage (simple demonstrations)
print(greet("Alice"))
print(add(5, 3))         # both args
print(add(10))           # uses default b=1
print(area_rectangle(4, 2))
print(area_rectangle(7)) # uses default width=1

print(is_even(10))
print(to_upper("python"))
say_hello()
say_hello("Bob")
print("Average of 5 and 10:", average(5, 10))
print("Average of 3, 6 and 9:", average(3, 6, 9))