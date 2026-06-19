class Toy:
    def __init__(self, name):
        self.name = name

    def play(self):
        return "Playing with " + self.name


class Dog:
    def __init__(self, name, toy):
        self.name = name
        self.toy = toy

    def bark(self):
        return self.name + " says woof!"

    def play_with_toy(self):
        return self.name + " is " + self.toy.play()

class Person:
    def __init__(self, name, dog):
        self.name = name
        self.pet = dog

    def introduce_pet(self):
        return "My dog is " + self.pet.name