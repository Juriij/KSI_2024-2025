from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    # TODO
    def describe(self):
        return f'Im {self.__class__.__name__} and I {self.sound()}!'

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return f'Bark'
    

class Cat(Animal):
    def sound(self):
        return f'Meow'
    

class Cow(Animal):
    def sound(self):
        return f'Mooo'


class Karlik(Animal):
    def describe(self):
        return f"Jmenuju se Karlik a tohle tezce nedavam..."
    
    def sound(self):
        return f'Moneyyyy'



def check(animals: list[Animal]) -> list[tuple[str, str]]:
    # TODO
    return  [(animal.sound(), animal.describe()) for animal in animals]








# Tests
dog = Dog()
assert dog.sound() == "Bark"
assert dog.describe() == "Im Dog and I Bark!"

cat = Cat()
assert cat.sound() == "Meow"
assert cat.describe() == "Im Cat and I Meow!"

cow = Cow()
assert cow.sound() == "Mooo"
assert cow.describe() == "Im Cow and I Mooo!"

karlik = Karlik()
assert karlik.sound() == "Moneyyyy"
assert karlik.describe() == "Jmenuju se Karlik a tohle tezce nedavam..."

assert check([dog, cat]) == [("Bark", "Im Dog and I Bark!"), ("Meow", "Im Cat and I Meow!")]
