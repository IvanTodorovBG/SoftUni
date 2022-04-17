from project.animals.animal import Mammal, Bird, Animal
from project.food import Vegetable, Fruit, Meat, Seed, Food


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(0.1, food)


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(0.4, food)


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(0.3, food)


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(1.00, food)
