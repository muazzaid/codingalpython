file_read = open("codingal.txt", "r")
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_read_write = open('codingal.txt', 'w')
file_read_write.write(" File in write mode ....\n")
file_read_write.write("hi! I am penguin and I am 1 year old.")
file_read_write.close()

file_append = open("codingal.txt", "a")
file_append.write("\n File in append mode ....\n")
file_append.write("hi! I am penguin and I am 1 year old.")
file_append.close()