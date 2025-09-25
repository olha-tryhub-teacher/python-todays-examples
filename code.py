# Оголошення класу Animal (Тварина)
class Animal:
    # Метод ініціалізації — встановлює ім'я та початковий рівень енергії тварини
    def __init__(self, name, energy):
        self.name = name        # Ім'я тварини
        self.energy = energy    # Поточний рівень енергії тварини


    # Метод eat — тварина їсть їжу, додаючи енергію від їжі до своєї
    def eat(self, food):
        self.energy += food.energy     # Збільшуємо енергію тварини на енергію їжі
        print(f"Animal {self.name} eat {food.name}. Energy: {self.energy}")
        # Виводимо повідомлення про те, що тварина з'їла їжу і показуємо оновлений рівень енергії


# Оголошення класу Food (Їжа)
class Food:
    # Метод ініціалізації — встановлює назву їжі та її енергетичну цінність
    def __init__(self, name, energy):
        self.name = name        # Назва їжі
        self.energy = energy    # Кількість енергії, яку дає їжа
