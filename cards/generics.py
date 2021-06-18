"""
Generic classes which can be extended to create specific cards
"""

class Card:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost
    
    def __str__(self) -> str:
        return (
            "Name:\t {}\n".format(self.name) +
            "Cost:\t {}".format(self.cost)
        )

    def __iter__(self):
        return self

class Spell(Card):
    def __init__(self, name, cost, speed) -> None:
        super().__init__(name, cost)
        self.speed = speed
    
    def __str__(self) -> str:
        return (
            super().__str__() + "\n" +
            "Speed:\t {}".format(self.speed)
        )

class Unit(Card):
    def __init__(self, name, cost, power, health) -> None:
        super().__init__(name, cost)
        self.power = power
        self.health = health
    
    def __str__(self) -> str:
        return (
            super().__str__() + "\n" +
            "Power:\t {}\n".format(self.power) +
            "Health:\t {}".format(self.health)
        )

class Champion(Unit):
    def __init__(self, name, cost, power, health, level=0) -> None:
        super().__init__(name, cost, power, health)
        self.level = level
    
    def __str__(self) -> str:
        return (
            super().__str__() + "\n" +
            "Level:\t {}".format(self.level)
        )

    
class Follower(Unit):
    def __init__(self, name) -> None:
        super().__init__(name)