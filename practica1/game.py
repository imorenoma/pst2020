import random


class Person:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg

    def generate_damage(self):
        return random.randint(1, self.dmg)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp
