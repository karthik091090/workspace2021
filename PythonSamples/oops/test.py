class Dog:
    def __init__(self, name, age):
        self.name = name  # self.name refers to the instance variable 'name'
        self.age = age    # self.age refers to the instance variable 'age'

    def bark(self):
        return f"{self.name} says woof!"  # self.name accesses the instance's 'name' attribute

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

print(my_dog.bark())  # Output: Buddy says woof!
