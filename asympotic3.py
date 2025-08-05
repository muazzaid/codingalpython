def OnSquareTime(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            iteration += 1
            print("")
        print("\nwhen n is", n, "Iterations =", iteration)
    
OnSquareTime(10)
OnSquareTime(20)
OnSquareTime(30)

print("\nWith every 'n' the time taken equals n^2")
print("O(n^2) ")

                  

                  
