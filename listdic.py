def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'John', 'Doe'], [2, 'Jane', 'Smith'], [3, 'Emily', 'Jones']]

print("\nOriginal list of lists:")
print(students)
print("\nConverted list to a dictionary:")
print(test(students))