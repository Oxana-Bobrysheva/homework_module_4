class Category:
    """Класс для представления категорий продукции."""
    name: str
    description: str
    products: list

    quantity_of_category = 0
    quantity_of_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.quantity_of_category += 1
        Category.quantity_of_products += 1
