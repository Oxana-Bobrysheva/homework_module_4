from src.product import Product


def test_product_init(product):
    assert product.name == "potatoes"
    assert product.description == "Kursk origin"
    assert product.price == 40.5
    assert product.quantity == 25


def test_price_adding():
    product1 = Product("potatoes", "good", 14, 12)
    product2 = Product("tomatoes", "good", 15, 10)
    result = product1 + product2
    assert result == 318
