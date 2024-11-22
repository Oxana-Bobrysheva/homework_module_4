from src.product import Product


class Category:
    """Класс для представления категорий продукции."""

    name: str
    description: str
    products: list

    category_count = 0
    all_product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.all_product_count += len(products) if products else 0


    def add_products(self, new_product):

        self.__products.append(new_product)
        Category.all_product_count += 1
