# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number "))

    # check if the number is negative
if num < 0:
        print("sorry, factorial does not exist for negative numbers")
elif num == 0:
        print("The factorial of 0 is 1")
else:
        print("the factorial of", num, "is", factorial(num))