import pandas as pd
from sklearn.model_selection import train_test_split  # Імпортуємо функцію для розділення даних на тренувальну і тестову вибірки
from sklearn.preprocessing import StandardScaler  # Імпортуємо StandardScaler для нормалізації даних
from sklearn.neighbors import KNeighborsClassifier  # Імпортуємо K-Nearest Neighbors Classifier
from sklearn.metrics import confusion_matrix, accuracy_score  # Імпортуємо метрики оцінки моделі

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

df = pd.read_csv("train.csv")
print(df.head())

print(df.info())

df.drop(["id", "bdate", "has_mobile", "education_form", "education_status", "langs", "life_main", "people_main", "last_seen", "occupation_type", "followers_count", "has_photo", "career_start", "career_end"], axis=1, inplace=True)
print(df.info())

# Навчання моделі
# Вибір цільової змінної та ознак
X = df.drop("result", axis=1)
y = df["result"]

# Розділення даних
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=99999)

# Навчання моделі
sc = StandardScaler()
X_train = sc.fit_transform(X_train)  # Нормалізуємо тренувальні дані
X_test = sc.transform(X_test)  # Нормалізуємо тестові дані на основі параметрів тренувальної вибірки

classifier = KNeighborsClassifier(n_neighbors=5)  # Створюємо модель K-Nearest Neighbors з 5 сусідами
classifier.fit(X_train, y_train)  # Навчаємо модель на тренувальних даних

y_pred = classifier.predict(X_test)  # Виконуємо прогнозування на тестових даних
print("Відсоток правильно передбачених результатів:",accuracy_score(y_test, y_pred) * 100)  # Виводимо точність моделі
print("Confusion matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)  # Виводимо матрицю плутанини для оцінки моделі

print(cm[0][0], "- правильно класифіковані як ті, хто не придбав курс")
print(cm[0][1], "- помилково класифіковані як ті, хто придбав курс, хоча насправді вони його не придбали")
print(cm[1][0], "- помилково класифіковані як ті, хто не придбав курс, хоча насправді вони його придбали")
print(cm[1][1], "- правильно класифіковані як ті, хто придбав курс")

df = pd.read_csv("test.csv")
id_test = df["id"]
df.drop(["id", "bdate", "has_mobile", "education_form", "education_status", "langs", "life_main", "people_main", "last_seen", "occupation_type", "followers_count", "has_photo", "career_start", "career_end"], axis=1, inplace=True)
X_test = sc.transform(df)
y_pred = classifier.predict(X_test)

print(y_pred)
df_sub = pd.DataFrame({"id":id_test, "result":y_pred})
df_sub.to_csv("result.csv", index=False)

