class student:
    grade = 12
    name = "John Doe"

    def introduction(self):
        print("hi I am a student")

    def details(self):
        print(f"My name is {self.name} and I am in grade {self.grade}")

ob = student()
ob.introduction()
ob.details()