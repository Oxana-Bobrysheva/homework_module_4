from unicodedata import category


def test_category_init(category_1, category_2):
    assert category_1.name == "Vegetables"
    assert category_1.description == "Fresh vegetables"
    assert category_1.products == ["potatoes", "tomatoes", "carrot"]
    assert len(category_1.products) == 3

    assert category_1.product_count == 7
    assert category_2.product_count == 7

    assert category_1.category_count == 2

