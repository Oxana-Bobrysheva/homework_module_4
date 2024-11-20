def test_category_init(category_1, category_2):
    assert category_1.name == "Vegetables"
    assert category_1.description == "Fresh vegetables"
    assert category_1.products == ["potatoes", "tomatoes", "carrot"]
    assert category_2.name == "Fruit"
    assert category_2.description == "Fresh fruit"
    assert category_2.products == ["apples", "pears", "apricots", "peaches"]

    assert len(category_1.products) == 3
    assert len(category_2.products) == 4

    assert category_1.category_count == 2
    assert category_2.all_product_count == 7
