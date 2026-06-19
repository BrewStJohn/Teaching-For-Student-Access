from extra import Toy, Dog, Person

toy1 = Toy("tennis ball")
dog1 = Dog("Max", toy1)
person1 = Person("Sarah", dog1)

# What is this going to print?
print(person1.name) # Sarah
print(person1.pet.name) # Max
print(person1.pet.bark()) # Max says woof
print(person1.pet.toy.name) # tennis ball
print(person1.pet.toy.play()) 
print(person1.pet.play_with_toy()) 
print(person1.introduce_pet()) 