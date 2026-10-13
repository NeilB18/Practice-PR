class Dog:
    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def bark(self):
        print(f"Bark Bark yo my name is {self.name}")

    def eat(self):
        print("I'm eating good shit")

Jack = Dog("Jack", "Golden Retriever", "Golden", 3)
Jack.bark()
Jack.eat()