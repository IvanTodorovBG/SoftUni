from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        asked_sub = [c_s.__repr__() for c_s in self.subscriptions if c_s.id == subscription_id][0]
        asked_cust = [c_c.__repr__() for c_c in self.customers if c_c.id == subscription_id][0]
        asked_trainer = [c_t.__repr__() for c_t in self.trainers if c_t.id == subscription_id][0]
        asked_equip = [c_e.__repr__() for c_e in self.equipment if c_e.id == subscription_id][0]
        asked_plan = [c_p.__repr__() for c_p in self.plans if c_p.id == subscription_id][0]
        return asked_sub + "\n" + asked_cust + "\n" + asked_trainer + "\n" + asked_equip + "\n" + asked_plan

