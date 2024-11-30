from src.product import Product


class Category:
    """Класс для представления категорий продукции."""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    def add_product(self, new_product):

        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        """Getter returns list of products according to the request"""
        products_list = ""
        for product in self.__products:
            products_list += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_list

    @property
    def get_products(self):
        """Getter returns list of products according to the request"""
        products_list = []
        for product in self.__products:
            products_list.append(product)
        return products_list