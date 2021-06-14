from . import generics

class Fiora(generics.Champion):
    def __init__(self, name="Fiora", cost=3, power=3, health=2, level=0, killed=0) -> None:
        super().__init__(name, cost, power, health, level)
        self.killed = killed
    
    def __str__(self) -> str:
        return (
            super().__str__() + "\n" +
            "Killed:\t {}".format(self.killed)
        )
    
    def speak(self) -> None:
        print("I long for a worthy opponent.")
        return None