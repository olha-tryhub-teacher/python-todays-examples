# 1
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print("Починаємо рахувати час")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} виконано за {execution_time} секунд")

        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Функція спрацювала!")


slow_function()

# 2
def even_argument_required(func):
    def wrapper(number):
        if number % 2 == 0:
            result = func(number)
            return result
        else:
            print("Помилка: Потрібно парне число для виконання функції.")
            return None
    return wrapper

# Використання декоратора
@even_argument_required
def perform_operation(number):
    return number * 2


print(perform_operation(4))  # Виконає функцію, оскільки 4 - парне число
# Виведе повідомлення про помилку, оскільки 3 - не парне число
print(perform_operation(3))


# 3

# Cловник користувачів
user_database = {
    "maria": {
        "ім'я": "Марія",
        "прізвище": "Шевченко",
        "вік": 34,
        "пароль": "password2"
    },
    "olexiy": {
        "ім'я": "Олексій",
        "прізвище": "Марчук",
        "вік": 22,
        "пароль": "password3"
    },
    "anna": {
        "ім'я": "Анна",
        "прізвище": "Коваленко",
        "вік": 45,
    "пароль": "password4"
    },
    "pavlo": {
        "ім'я": "Павло",
        "прізвище": "Мельник",
        "вік": 30,
        "пароль": "password5"
    }
}


# Прапорець авторизації користувача
auth_user = False


# Функція для перевірки авторизації користувача
def check_password(username, password):
    if username in user_database and user_database[username]["пароль"] == password:
        return True
    return False


# Функція авторизації користувача
def authenticate_user():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if check_password(username, password):
        # Допишіть код
        global auth_user
        auth_user = True
        print(f"Ви успішно авторизувалися, {username}!")
        return username
    else:
        print("Помилка авторизації. Спробуйте ще раз або зверніться до адміністратора.")


# Декоратор для перевірки авторизації користувача
def authentication_required(func):
    # Допишіть код
    def wrapper(*args, **kwargs):
        if auth_user == True:
            result = func(*args, **kwargs)
            return result
        # Допишіть код⬆️⬆️
        else:
            print(f"Помилка! Доступ до функції {func.__name__} заборонено!")
    return wrapper


# Використання декоратора
@authentication_required# Допишіть код
def get_all_users():
    # Допишіть код
    print("\nОСОБИСТІ ДАННІ ВСІХ КОРИСТУВАЧІВ:\n================================\n")
    for user in user_database:
        print(user, user_database[user])
    print()


@authentication_required
def get_user(username):
    print("\nОсобисті дані користувача " +
username + ":\n-------------------------------\n")
    for item in user_database[username]:
        print(item + ":", str(user_database[username][item]) + ";")
    print()


authenticated_user = authenticate_user()


get_user("maria")
get_all_users()
