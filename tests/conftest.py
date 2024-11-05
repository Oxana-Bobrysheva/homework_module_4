import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category(
        name="Vegetables",
        description="Fresh vegetables",
        products=["potatoes", "tomatoes", "carrot"],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Fruit",
        description="Fresh fruit",
        products=["apples", "pears", "apricots", "peaches"],
    )


@pytest.fixture
def product():
    return Product("potatoes", "Kursk origin", 40.5, 25)
