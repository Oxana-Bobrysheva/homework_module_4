from src.product import Product
from tests.conftest import category_1, category_2


def test_new_product_existing(category_with_products):
    # Test adding a new product that already exists
    new_product_dict = {"name": "potatoes", "description": "New Description", "price": 15.0, "quantity": 3}
    existing_product = Product.new_product(new_product_dict, category_with_products)
    assert existing_product.price == 40.5
    assert existing_product.quantity == 28


def test_new_product_not_existing(category_with_products):
    # Test adding a new product that does not already exist
    new_product_dict = {"name": "New Product", "description": "Description", "price": 20.0, "quantity": 2}

    new_product = Product.new_product(new_product_dict, category_with_products)
    assert new_product.name == "New Product"
    assert new_product.price == 20.0
    assert new_product.quantity == 2


def test_add_product(category_1):
    # Test adding a product to a category
    new_product = Product("New Product", "Description", 25.0, 10)
    category_1.add_product(new_product)
    assert category_1.product_count == 3


def test_category_str(category_1):
    assert str(category_1) == "Vegetables, количество продуктов: 75 шт."


def test_products_getter(category_1):
    assert category_1.products == (
        "potatoes, 40.5руб. Остаток: 25шт.\n"
        "tomatoes, 140.5руб. Остаток: 15шт.\n"
        "carrots, 20.0руб. Остаток: 35шт.\n"
    )


def test_middle_price_exists(category_1):
    "Test for function middle_price to verify that it finds right amount"
    assert category_1.middle_price() == 67


def test_middle_price_not_exist(category_2):
    "Test for function middle_price to verify that is raises ZeroDivisionError"
    assert category_2.middle_price() == 0
