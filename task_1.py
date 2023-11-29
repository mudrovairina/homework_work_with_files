cook_book = {}

with open('cookbook.txt', encoding='utf-8') as file:
    for string in file:
        dish = string.strip()
        quantity_ingredients = int(file.readline().strip())

        ingredients = []
        for _ in range(quantity_ingredients):
            ingredient = file.readline().strip().split('|')
            ingredients.append(ingredient)

        cook_book[dish] = []
        for ingredient in ingredients:
            ing = {
                'ingredient_name': ingredient[0].strip(),
                'quantity': int(ingredient[1].strip()),
                'measure': ingredient[2].strip()
            }
            cook_book[dish].append(ing)

        file.readline().strip()  # пустая строка


print(cook_book)
