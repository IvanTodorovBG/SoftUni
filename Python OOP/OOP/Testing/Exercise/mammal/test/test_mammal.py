from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "TestType", "TestSound")

    def test_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("TestSound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Test makes TestSound", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Test is of type TestType", self.mammal.info())


if __name__ == "__main__":
    main()
