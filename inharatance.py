# Parent class 
class dad:
    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

        print("your eye color is", self.eyes)
        print("you aggressive", self.aggressive)

# Child class
class son(dad):
    def __init__(self, eyes, aggressive, hair_color):
        super().__init__(eyes, aggressive)  # Call the parent class constructor
        self.hair_color = hair_color

        print("your hair color is", self.hair_color)

        # inovoking the __init__ of parent class
        # to access its attributes 
        super().__init__(eyes, aggressive)

# Object creation
obj = son("Penguin", "blue", True)

# calling method display
def display(self):
    print("Eye color:", self.eyes)
    print("Aggressive:", self.aggressive)
    print("Hair color:", self.hair_color)
