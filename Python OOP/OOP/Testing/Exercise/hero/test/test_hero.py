from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def test_init_upon_initialisation(self):
        hero = Hero("Hero", 60, 100, 20)
        self.assertEqual("Hero", hero.username)
        self.assertEqual(60, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(20, hero.damage)

    def test_hero_str_(self):
        hero = Hero("Hero", 60, 100, 20)
        result = str(hero)
        self.assertEqual(f"Hero {hero.username}: {hero.level} lvl\n"
               f"Health: {hero.health}\n"
               f"Damage: {hero.damage}\n", result)

    def test_battle_same_names_with_hero_and_enemy_raise(self):
        hero = Hero("Hero", 60, 100, 20)
        enemy = Hero("Hero", 60, 100, 20)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_negative_or_zero_raise(self):
        for health in [0, -10]:
            hero = Hero("Hero", 60, health, 20)
            enemy = Hero("Enemy", 60, 100, 20)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_negative_or_zero_raise(self):
        for health in [0, -10]:
            hero = Hero("Hero", 60, 100, 20)
            enemy = Hero("Enemy", 60, health, 20)
            with self.assertRaises(ValueError) as ex:
                hero.battle(enemy)
            self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_if_both_enemy_and_hero_health_zero_or_below(self):
        hero = Hero("Hero", 60, 100, 20)
        enemy = Hero("Enemy", 60, 100, 20)
        hero_health = hero.health - enemy.damage * enemy.level
        enemy_health = enemy.health - hero.damage * hero.level
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(hero_health, hero.health)
        self.assertEqual(enemy_health, enemy.health)

    def test_battle_if_enemy_hero_health_zero_or_below(self):
        hero = Hero("Hero", 60, 100, 20)
        enemy = Hero("Enemy", 6, 10, 2)
        hero_health = hero.health - enemy.damage * enemy.level
        result = hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(61, hero.level)
        self.assertEqual(hero_health + 5, hero.health)
        self.assertEqual(25, hero.damage)

    def test_battle_if_hero_health_zero_or_below(self):
        hero = Hero("Hero", 6, 10, 2)
        enemy = Hero("Enemy", 60, 100, 20)
        enemy_health = enemy.health - hero.damage * hero.level
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(61, enemy.level)
        self.assertEqual(enemy_health + 5, enemy.health)
        self.assertEqual(25, enemy.damage)


if __name__ == "__main__":
    main()