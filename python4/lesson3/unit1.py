# 1
# Напиши функцію для зведення в ступінь
def exponentiation(power):
    def exponent(base):
        return base ** power
    return exponent

# Cтворіть два замикання: для зведення в квадрат та куб
square = exponentiation(2)
cube = exponentiation(3)

# Отримайте від користувача число
number = int(input("Введіть число"))

# Виведіть результат роботи замикань для числа
print(number, 'в квадраті:', square(number))
print(number, 'в кубі:',cube(number))


# 2
# Функція для зведення в ступінь
def power_function(power):
    return lambda x: x ** power


# Функція для обчислення кореня
def root_function(power):
    return lambda x: x ** (1 / power)


# Створіть замикання, яке зводить число в квадрат
square = power_function(2)
# Створіть замикання, яке зводить число в куб
cube = power_function(3)
# Створіть замикання, яке обчислює квадратний корінь
square_root = root_function(2)
# Створіть замикання, яке обчислює кубічний корінь
cube_root = root_function(3)
# Зведіть конкретні числа в квадрат та куб
print(square(8))
print(cube(5))
# Обчисліть квадратний та кубічний корені конкретного числа
print(square_root(8))
print(cube_root(5))

# 3
# Функція для обчислення факторіалу числа
import time


def memoize_factorial():
    cache = {}

    def factorial(n):
        if n in cache:
            return cache[n]

        if n == 0:
            result = 1
        else:
            result = n * factorial(n - 1)

        cache[n] = result

        return result

    return factorial


factorial = memoize_factorial()

start_time = time.time()
result = factorial(555)
print(round((time.time() - start_time), 4))
start_time = time.time()
result = factorial(555)
print(round((time.time() - start_time), 4))
# print(result)
