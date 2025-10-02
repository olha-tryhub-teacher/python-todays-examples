class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 50

    def eat(self, food):
        self.energy += food.energy
        food.energy = 0
        print(f"Смачно, сила {self.name} = {self.energy}")

class Food:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

meat = Food("meat", 30)
dog = Animal("Max")
dog.eat(meat)
