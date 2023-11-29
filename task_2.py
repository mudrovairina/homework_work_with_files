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


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish_ in cook_book:
        if dish_ in dishes:
            list_ing = cook_book[dish_]
            for ind in list_ing:
                key = ind['ingredient_name']
                value = ind['quantity'] * person_count
                if key not in shop_list_by_dishes:
                    shop_list_by_dishes[key] = {
                        'measure': ind['measure'],
                        'quantity': value
                    }
                else:
                    shop_list_by_dishes[key]['quantity'] += value
    return shop_list_by_dishes


print(get_shop_list_by_dishes(dishes=['Омлет', 'Фахитос'], person_count=3))

