from src.product import Product
from src.category import Category


def test_new_product_existing(category_with_products):
    # Test adding a new product that already exists
    new_product_dict = {'name': 'potatoes', 'description': 'New Description', 'price': 15.0, 'quantity': 3}

    existing_product = Product.new_product(new_product_dict, category_with_products)
    assert existing_product.price == 40.5
    assert existing_product.quantity == 28


def test_new_product_not_existing(category_with_products):
    # Test adding a new product that does not already exist
    new_product_dict = {'name': 'New Product', 'description': 'Description', 'price': 20.0, 'quantity': 2}

    new_product = Product.new_product(new_product_dict, category_with_products)
    assert new_product.name == 'New Product'
    assert new_product.price == 20.0
    assert new_product.quantity == 2


def test_add_product(category_1):
    # Test adding a product to a category
    new_product = Product('New Product', 'Description', 25.0, 10)
    category_1.add_product(new_product)
    assert category_1.product_count == 6


