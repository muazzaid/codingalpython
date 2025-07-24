file = open("codingal.txt", "r")
print('codingal.txt', 'r')
file.close()

file = open("codingal.txt", "r")
print("\n Read in part \n")
print(file.read(10))  
file.close()

file = open("codingal.txt", "a")
file.write(" Hi! I am penguin and I am 1 year old.")
file.close()