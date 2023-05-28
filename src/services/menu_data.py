import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as file:
            csv_reader = csv.reader(file)
            header, *data = csv_reader
            dishes = dict()

            for item in data:
                if item[0] not in dishes:
                    dishes[item[0]] = Dish(item[0], float(item[1]))

                dishes[item[0]].add_ingredient_dependency(
                    Ingredient(item[2]),
                    int(item[3])
                )

            dishes_menu = list()
            for dish in dishes:
                dishes_menu.append(dishes[dish])
            self.dishes = set(dishes_menu)
