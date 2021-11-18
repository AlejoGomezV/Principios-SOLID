class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass


class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass


class SwimmingBird(Bird):

    @abstractmethod
    def swim(self):
        pass


class Crow(FlyingBird):
    def fly(self):
        print(f"{self.name} is flying hign and fast!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(SwimmingBird, FlyingBird):
    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swim in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"
        