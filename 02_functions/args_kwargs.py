# *args = variable number of positional arguments
def sum_all(*args):
    print("Arguments received:", args)
    return sum(args)

print("Sum of 1, 2, 3:", sum_all(1, 2, 3))
print("Sum of 4, 5:", sum_all(4, 5))

# **kwargs = variable number of keyword arguments
def print_info(**kwargs):
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=25, city="Paris")

# Combine *args and **kwargs
def mixed_example(a, b=0, *args, **kwargs):
    print(f"a = {a}, b = {b}")
    print("Extra positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

mixed_example(1, 2, 3, 4, 5, x=10, y=20)