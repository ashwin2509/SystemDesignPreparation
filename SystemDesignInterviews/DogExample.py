class Dog:
    species = "mammal"
    is_hungry = True


    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def walk(self):
        print("{} is walking".format(self.name))

    def eat(self):
        self.is_hungry = False


    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

   


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:
    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs 

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())






dogs = [
        Bulldog("Ashwin", 23), 
        RussellTerrier("Supreet", 24)
        
        ]

my_pets = Pets(dogs)
my_pets.walk()
is_hungry_my_dogs = True

for dog in my_pets.dogs:
    if dog.is_hungry is True:
        is_hungry_my_dogs = True

if is_hungry_my_dogs:
    print("My dogs are hungry")
else:
    print("They are not")




for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
print("And they're all {}s, of course.".format(dog.species))

Tommy = RussellTerrier("Tommy", 14)
print(Tommy.description())


Anisha = Dog("Anisha", 45)
Anisha.eat()
print("{} is hungry is {}".format(Anisha.name, Anisha.is_hungry))




        
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
rockey = Dog("Rocky", 8)
array = [5, 6, 8]

print("{} is {} and {} is {}. ".format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == 'mammal':
    print("{} is a {}!!".format(philo.name, philo.species))
    
print(mikey.description())
print(rockey.speak("Woof woof"))


def get_biggest_number(nums):
    return max(nums)

print("the oldest dog is {} years old".format(get_biggest_number(array)))
    

        

