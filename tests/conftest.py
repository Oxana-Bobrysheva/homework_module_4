import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category(
        name="Vegetables",
        description="Fresh vegetables",
        products=[Product("potatoes", "Kursk origin", 40.5, 25),
                  Product("tomatoes", "Kursk origin", 140.5, 15),
                  Product("carrots", "Kursk origin", 20.0, 35)]
    )
@pytest.fixture
def category_with_products():
    category = Category(
        name="Vegetables",
        description="Fresh vegetables",
        products=[],
    )
    category.add_product(Product("potatoes", "Kursk origin", 40.5, 25))
    return category
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
