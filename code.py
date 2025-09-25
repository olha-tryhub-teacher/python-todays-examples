class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name {self.name}")
        print(f"Age: {self.age}")


class Pupil(Human):
    def __init__(self, name, age, school, marks):
        super().__init__(name, age)
        self.marks = marks
        self.school = school

    def full_info(self):
        self.info()
        print(f"School: {self.school}")
        print(f"Marks: {self.marks}")


class Worker(Human):
    def __init__(self, name, age, work, salary):
        super().__init__(name, age)
        self.work = work
        self.salary = salary

    def full_info(self):
        super().info()
        print(f"Work: {self.work}")
        print(f"Salary: {self.salary}")


human = Human("Stas", 34)
student = Pupil("Vika", 13, "7A", [11, 10, 9, 11])
worker = Worker("Halyna Ivanivna", 32, "Logika", 10000)

human.info()
print("***********")
student.full_info()
student.info()
print("***********")
worker.full_info()
print("***********")
