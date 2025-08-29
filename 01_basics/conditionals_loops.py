# Conditional statement
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# For loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
count = 0
print("\nCounting with while loop:")
while count < 5:
    print("Count is", count)
    count += 1
