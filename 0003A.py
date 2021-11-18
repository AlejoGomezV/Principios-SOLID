from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass


    @abstractmethod
    def swim(self):
        pass


    @abstractmethod
    def do_sound(self) -> str:
        pass


class Crow(Bird):
    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def swim(self):
        raise NotImplementedError("Crows don't swim")

    def do_sound(self) -> str:
        return "Caw"


class Duck(Bird):
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swim in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"