def divide(ourDividend, ourDivisor):

    sign = -1 if ((ourDividend < 0) ^ (ourDivisor < 0)) else 1

    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)

    quotientnumber = 0
    tempnumber = 0

    for i in range(31, -1, -1):
        if (tempnumber + (ourDivisor << i) <= ourDividend):
            tempnumber += ourDivisor << i
            quotientnumber |= 1 << i

    if (sign == -1):
        quotientnumber = -quotientnumber
    return quotientnumber
    
a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))
print("\nThe result of a/b is: ", divide(a, b))