from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = [c_c for c_c in self.customers if c_c.id == customer_id][0]
        current_dvd = [c_d for c_d in self.dvds if c_d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        elif current_dvd.is_rented:
            return "DVD is already rented"
        elif current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
        else:
            current_customer.rented_dvds.append(current_dvd)
            current_dvd.is_rented = True
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [c_c for c_c in self.customers if c_c.id == customer_id][0]
        current_dvd = [c_d for c_d in self.dvds if c_d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        else:
            return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        return '\n'.join([c_c.__repr__() for c_c in self.customers]) + '\n' + \
               '\n'.join([c_d.__repr__() for c_d in self.dvds])


movie_world = MovieWorld("Test")
d = DVD("A", 1, 1254, "February", 10)
c = Customer("Pesho", 20, 4)
movie_world.add_customer(c)
movie_world.add_dvd(d)
movie_world.rent_dvd(4, 1)
a = 5






