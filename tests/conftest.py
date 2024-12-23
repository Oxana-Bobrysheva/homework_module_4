import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def category_1():
    return Category(
        name="Vegetables",
        description="Fresh vegetables",
        products=[
            Product("potatoes", "Kursk origin", 40.5, 25),
            Product("tomatoes", "Kursk origin", 140.5, 15),
            Product("carrots", "Kursk origin", 20.0, 35),
        ],
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
def product():
    return Product("potatoes", "Kursk origin", 40.5, 25)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass_1():
    return LawnGrass("Cleverance", "For sports ground", 250, 23, "Russia", "6 weeks", "Greenish")


@pytest.fixture
def category_2():
    return Category(
        name="Vegetables",
        description="Fresh vegetables",
        products=[],
    )
