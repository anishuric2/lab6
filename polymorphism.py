from abc import ABC, abstractmethod


class AbstractPet(ABC):
    def __init__(self, name, sound, food):
        self.__name = name
        self.__sound = sound
        self.__food = food

    @property
    def name(self):
        return self.__name

    @property
    def sound(self):
        return self.__sound

    @property
    def food(self):
        return self.__food

    #Abstract Methods

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def favorite_food(self):
        pass

    @abstractmethod
    def perform_trick(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


    def __str__(self):
        return f"{self.name} says {self.sound} and likes to eat {self.food}"


class Dog(AbstractPet):
    def make_sound(self):
        print("Woof")

    def favorite_food(self):
        return "Bones"

    def perform_trick(self):
        print("Dog performs a trick: Sit")

    def sleep(self):
        print("Dog is sleeping")



class Cat(AbstractPet):
    def make_sound(self):
        print("Meow")

    def favorite_food(self):
        return "Fish"

    def perform_trick(self):
        print("Cat performs a trick: Roll over")

    def sleep(self):
        print("Cat is napping")



class Bird(AbstractPet):
    def __init__(self, name, sound, food, color):
        super().__init__(name, sound, food)
        self.__color = color

    @property
    def color(self):
        return self.__color

    def make_sound(self):
        print("Tweet")

    def favorite_food(self):
        return "Seeds"

    def perform_trick(self):
        print("Bird performs a trick: Whistle")

    def sleep(self):
        print("Bird is resting")



# Testing the classes
#________dog______________
print("----Dog----")
dog = Dog("Buddy", "Woof", "Bones")
print(dog)
dog.make_sound()
dog.perform_trick()
dog.sleep()


print("\n\n----Cat----")

#________cat______________
cat = Cat("Whiskers", "Meow", "Fish")
print(cat)
cat.make_sound()
cat.perform_trick()
cat.sleep()


print("\n\n----Bird----")
#________bird______________
bird = Bird("Robin", "Tweet", "Seeds", "Red")
print(bird)
bird.make_sound()
print(f"{bird.name} is {bird.color}")
bird.favorite_food()
bird.perform_trick()
bird.sleep()

