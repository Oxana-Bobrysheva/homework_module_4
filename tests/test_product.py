def test_product_init(product):
    assert product.name == "potatoes"
    assert product.description == "Kursk origin"
    assert product.price == 40.5
    assert product.quantity == 25
