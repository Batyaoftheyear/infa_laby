# coding: utf-8
# license: GPLv3


class Attacker:
    _health = 0
    _attack = 0

    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0
    