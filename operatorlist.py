lst = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

print("Length of the list:", len(lst))
print("First element:", lst[2])
print("Last element:", lst[-1])

lst.append('cherry')
print("updated list:", lst)

lst.remove('Banana')
print("updated list :", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("updated list:", lst)

lst.reverse()
print("Reversed list:", lst)