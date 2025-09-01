def greet(name):
    return f"Hello, {name}!"

def add(a, b = 1):
    return a + b

def area_rectangle(length, width=1):
    return length * width

def is_even(number):
    return number % 2 == 0

def to_upper(text):
    return text.upper()

def say_hello(name="Friend"):
    print(f"Hi {name}, how are you?")

def average(a, b, c = 0):
    return (a + b + c) / (3 if c else 2)

print(greet("Alice"))
print(add(5, 3))
print(add(10)) 
print(area_rectangle(4, 2))
print(area_rectangle(7))

print(is_even(10))
print(to_upper("python"))
say_hello()
say_hello("Bob")
print("Average of 5 and 10:", average(5, 10))
print("Average of 3, 6 and 9:", average(3, 6, 9))