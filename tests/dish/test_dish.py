from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient

import pytest


def test_dish():
    pancake = Dish('pancake', 4.50)
    rice_beans = Dish('Rice and Beans', 10.50)

    assert pancake.name == 'pancake'

    assert hash(pancake) == hash("Dish('pancake', R$4.50)")

    assert hash(rice_beans) != hash('pancake')

    assert pancake == pancake

    assert pancake != rice_beans

    assert repr(pancake) == "Dish('pancake', R$4.50)"

    with pytest.raises(TypeError, match='Dish price must be float.'):
        Dish('rice', 'ten dolars')

    with pytest.raises(ValueError,
                       match='Dish price must be greater then zero.'):
        Dish('beans', -15)

    pancake.add_ingredient_dependency(Ingredient("milk"), 2)
    pancake.add_ingredient_dependency(Ingredient("flour"), 1)

    assert pancake.recipe == {
        Ingredient("milk"): 2,
        Ingredient("flour"): 1,
    }

    pancake_ingredients = pancake.get_ingredients()

    assert {ingredient.name for ingredient in pancake_ingredients} == {
        "milk",
        "flour",
    }

    assert pancake.get_restrictions() == set()
