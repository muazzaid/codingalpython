#Python progam to print astar pattern based on the number of rows specified by the user
# Get the number of rows from the user
n = int(input("Enter the number of rows: "))
# Outer loop for each row
for i in range(1, n + 1):
    
    # Inner loop for printing stars
    for j in range(1, i + 1):
        print("*", end="")
    # Move to the next line after each row
    print()