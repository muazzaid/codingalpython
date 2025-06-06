# This fuction add two numbers
def add(x, y):
    return x + y

# This fuction subtract two numbers
def subtract(x, y):
    return x - y

# This fuction multiplies two numbers
def multiply(x, y):
    return x * y

# This fuction divides two numbers
def divides(x, y):
    return x / y

num1 = int(input("Enter first number 1 "))
num2 = int(input("Enter second number 2 "))

print("sum:", add(num1, num2))
print("Difference:", subtract(num1, num2))
print("Product:", multiply(num1, num2))
print("Quotient:", divides(num1, num2))