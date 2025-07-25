with open('codingal.txt', 'w') as file:
    file.write("Hi! I am muaz and I am 15 years old.")
    file.close()

with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        words = line.split()
        print(words)
    file.close()