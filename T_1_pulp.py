from pulp import LpMaximize, LpProblem, LpVariable, value

# Створюємо модель лінійного програмування
model = LpProblem(name="production_optimization", sense=LpMaximize)

# Оголошуємо змінні (x - кількість лимонаду, y - кількість фруктового соку)
x = LpVariable(name="Lemonade", lowBound=0, cat="Integer")  # Лимонад
y = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")  # Фруктовий сік

# Функція цілі: максимізація кількості вироблених продуктів
model += x + y, "Total Production"

# Додаємо обмеження на ресурси
model += (2*x + y <= 100), "Water Constraint"  # Вода
model += (x <= 50), "Sugar Constraint"  # Цукор
model += (x <= 30), "Lemon Juice Constraint"  # Лимонний сік
model += (2*y <= 40), "Fruit Puree Constraint"  # Фруктове пюре

# Розв’язуємо задачу
model.solve()

# Виводимо результати
print(f"Оптимальна кількість Лимонаду: {value(x)}")
print(f"Оптимальна кількість Фруктового соку: {value(y)}")
print(f"Максимальна загальна кількість продуктів: {value(model.objective)}")
