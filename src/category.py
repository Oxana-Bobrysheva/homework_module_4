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
        self.products = products

        Category.category_count += 1
        Category.all_product_count += len(products) if products else 0


    @property
        def add_products(self):
            products_str = ""
            for product in self.__products:
                products_str += f"{product.name}, "