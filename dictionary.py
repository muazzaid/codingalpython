my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Output: John
print(my_dict['name'])
print(my_dict['age'])
# Output: 30
print(my_dict['city'])
# Output: New York

# update value
my_dict['age'] = 31
print(my_dict)

# add item
my_dict['email'] = 'josuepelembe@gmail.com'
print(my_dict)

# remove particular element
my_dict.pop('city')
print(my_dict)

# acsess a particular element
print(my_dict['email'])

# remove all elements
my_dict.clear()