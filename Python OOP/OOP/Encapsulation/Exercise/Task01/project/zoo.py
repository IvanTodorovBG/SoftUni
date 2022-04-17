from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for current_worker in self.workers:
            total_salaries += current_worker.salary
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = 0
        for current_care_money in self.animals:
            total_money_for_care += current_care_money.money_for_care
        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        total_lions = 0
        lions_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                total_lions += 1
                lions_info.append(repr(animal))

        total_tigers = 0
        tigers_info = []
        for animal in self.animals:
            if type(animal) == Tiger:
                total_tigers += 1
                tigers_info.append(repr(animal))

        total_cheetahs = 0
        cheetahs_info = []
        for animal in self.animals:
            if type(animal) == Cheetah:
                total_cheetahs += 1
                cheetahs_info.append(repr(animal))

        result += f'----- {total_lions} Lions:\n'
        lions_result = '\n'.join(lions_info)
        result += lions_result + '\n'

        result += f'----- {total_tigers} Tigers:\n'
        tigers_result = '\n'.join(tigers_info)
        result += tigers_result + '\n'

        result += f'----- {total_cheetahs} Cheetahs:\n'
        cheetahs_result = '\n'.join(cheetahs_info)
        result += cheetahs_result

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        total_keepers = 0
        keepers_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                total_keepers += 1
                keepers_info.append(repr(worker))

        total_caretakers = 0
        caretakers_info = []
        for worker in self.workers:
            if type(worker) == Caretaker:
                total_caretakers += 1
                caretakers_info.append(repr(worker))

        total_vets = 0
        vets_info = []
        for worker in self.workers:
            if type(worker) == Vet:
                total_vets += 1
                vets_info.append(repr(worker))

        result += f'----- {total_keepers} Keepers:\n'
        keepers_result = '\n'.join(keepers_info)
        result += keepers_result + '\n'

        result += f'----- {total_caretakers} Caretakers:\n'
        caretakers_result = '\n'.join(caretakers_info)
        result += caretakers_result + '\n'

        result += f'----- {total_vets} Vets:\n'
        vets_result = '\n'.join(vets_info)
        result += vets_result

        return result


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

