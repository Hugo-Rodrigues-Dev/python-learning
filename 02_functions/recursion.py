def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)

def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print("Factorial of 5:", factorial(5))
print("Countdown from 5:")
countdown(5)
print("Sum from 1 to 10:", sum_to_n(10))

print("2^5 =", power(2, 5))
print("Reverse of 'hello' is", reverse_string("hello"))