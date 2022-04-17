from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100.1, 500.1)

    def test_class_init(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_upon_initialisation(self):
        self.assertEqual(100.1, self.vehicle.fuel)
        self.assertEqual(100.1, self.vehicle.capacity)
        self.assertEqual(500.1, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_not_enough_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(87.6, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raise(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_enough_fuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(1)
        self.assertEqual(88.6, self.vehicle.fuel)

    def test_str_(self):
        self.assertEqual("The vehicle has 500.1 horse power with "
                         "100.1 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()
