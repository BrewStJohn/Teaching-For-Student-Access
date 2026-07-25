from extra import Toy, Dog, Person

toy1 = Toy("tennis ball")
dog1 = Dog("Max", toy1)
person1 = Person("Sarah", dog1)

dog2 = Dog("Peter", toy1)
person2 = Person("Dylan", dog2)

# What is this going to print?
print(person1.name) # Sarah
print(person1.pet.name) # Max
print(person1.pet.bark()) # Sarah, Max, "Max says woof"
# print(person1.pet.toy.name)
# print(person1.pet.toy.play()) 
# print(person1.pet.play_with_toy()) 
print(person1.introduce_pet()) # My dog is Max
print(person2.introduce_pet()) # My dog is Max

