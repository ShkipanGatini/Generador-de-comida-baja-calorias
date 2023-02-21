import random


meal_options = {
    "Desayuno": {
        "Avena con  fruta": 300,
        "Fruta y Yoghurt": 200,
        "Tostada con manteca": 250,
        "Huevos revueltos con vegetales": 300,
        "Shake de proteina": 250,
    
    },
    "comida de mañana": {
        "Manzana con manteca y almendras": 150,
        "huevo hervido": 70,
        "Zanahoria  con hummus": 100,
        " yogurt griego con  berries": 100,
        " nueces": 150,
    },
    "Almuerzo": {
        "Ensalada de atún con tostada de grano entero": 350,
        "Pollo con sofrito de verduras ": 400,
        "Ensalada de espinaca con verduras ": 300,
        "Carne picada con garbanzos negros": 350,
        "Sopa de vegetales con pan de grano entero": 250,
    },
    "Comida de mediatarde": {
        "Banana con manteca de mani/dulce de leche": 200,
        "Queso cottage con tomate y pepino": 100,
        "Wraps de pollo con vegetales": 150,
        "Garbanzos rosti.": 100,
        "Tortitas de arroz.": 150,
    },
    "Cena": {
        "Pescado grillado con vegetales rosti": 350,
        "Morrón con arroz integral": 300,
        "Sofrito de arroz con vegetales rosti.": 300,
        "Kebab de pollo con vegetales": 350,
    },
}


days_of_week = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


meal_plan = {}
for day in days_of_week:
    meal_plan[day] = {}
    total_calories = 0
    for meal in meal_options:
        food, calories = random.choice(list(meal_options[meal].items()))
        meal_plan[day][meal] = {"food": food, "calories": calories}
        total_calories += calories
    meal_plan[day]["total_calories"] = total_calories


for day in meal_plan:
    print(day + ":")
    for meal in meal_plan[day]:
        if meal != "total_calories":
            food = meal_plan[day][meal]["food"]
            calories = meal_plan[day][meal]["calories"]
            print("  " + meal + ": " + food + " (" + str(calories) + " calorias)")
    print("  Total calorias: " + str(meal_plan[day]["total_calories"]))