from abc import ABC, abstractmethod
#

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

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def favorite_food(self):
        pass

    # @abstractmethod
    # def unique_method(self):
    #     pass
    #
    # @abstractmethod
    # def another_unique_method(self):
    #     pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} says {self.sound} and likes to eat {self.food}"

class Dog(AbstractPet):
    def make_sound(self):
        print("Woof")

    def favorite_food(self):
        return "Bones"

    # def unique_method(self):
    #     print("Dog-specific method")

    # def another_unique_method(self):
    #     print("Another dog-specific method")


class Cat(AbstractPet):
    def make_sound(self):
        print("Meow")

    def favorite_food(self):
        return "Fish"

    def unique_method(self):
        print("Cat-specific method")

    # def another_unique_method(self):
    #     print("Another cat-specific method")


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

    def unique_method(self):
        print("Bird-specific method")

    # def another_unique_method(self):
    #     print("Another bird-specific method")


# Testing the classes
#________dog______________
dog = Dog("Buddy", "Woof", "Bones")
print(dog)
dog.make_sound()


#________cat______________
cat = Cat("Whiskers", "Meow", "Fish")
print(cat)
cat.make_sound()


#________bird______________
bird = Bird("Robin", "Tweet", "Seeds", "Red")
print(bird)
bird.make_sound()
print(f"{bird.name} is {bird.color}")
bird.favorite_food()
