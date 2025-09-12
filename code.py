class Vector3D:
    _instances = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Vector3D._instances += 1

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    @staticmethod
    def get_count():
        return Vector3D._instances

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

v3 = v1 + v2
print(f"Додавання векторів: {v3}")

v4 = v1 - v2
print(f"Віднімання векторів: {v4}")

v5 = v1 * 2
print(f"Множення вектора на скаляр: {v5}")

print(f"Порівняння векторів v1 і v2: {v1 == v2}")  # Повинно вивести False

print(f"{'-' * 35}\nВсього було створено {Vector3D.get_count()} векторів")
