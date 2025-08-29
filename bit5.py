def Oddcurring(arr):
    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []

n = int(input("Enter number of elements: "))

while(n):
    num = int(input("Enter element: "))
    arr.append(num)
    n -= 1

print("\n\nOdd occurring element is: ", Oddcurring(arr))