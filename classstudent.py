class fruit:
    # class variable
    taste = 'sweet'

    # instance variable
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Object Creation
apple = fruit('Apple', 'Red')
banana = fruit('Banana', 'Yellow')
strawberry = fruit('Strawberry', 'Red')
print(apple.taste)
print(apple.name, apple.color)
print(banana.name, banana.color)
print(strawberry.name, strawberry.color)