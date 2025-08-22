numberLargest = int(input("Enter Largest Number: "))
numberSmallest = int(input("Enter Smallest Number: "))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print(f"The HCF is {numberLargest}.")