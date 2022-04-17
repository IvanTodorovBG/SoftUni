from project.animals.animal import Mammal, Bird, Animal
from project.food import Vegetable, Fruit, Meat, Seed, Food


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.gain_weight(0.25, food)


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.gain_weight(0.35, food)


