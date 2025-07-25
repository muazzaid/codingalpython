new_file = open('new_File.txt', 'x')
new_file.close()

import os
print("checking if file exists or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open('my_file.txt', 'w')
my_file.write("Hi! I am muaz and I am 15 years old.")
my_file.close()

os.remove('codingal.txt')

os.rmdir('Folder')
