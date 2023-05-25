from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    milk = Ingredient("milk")
    hamburguer = Ingredient("hamburguer")

    assert milk.name == "milk"

    assert hash(hamburguer) == hash("hamburguer")

    assert hamburguer != milk
    assert milk == milk

    assert repr(hamburguer) == "Ingredient('hamburguer')"

    assert milk.restrictions == set()
