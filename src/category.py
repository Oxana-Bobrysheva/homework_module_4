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
        Category.product_count += len(products) if products else 0  # noqa

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            # Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Getter returns list of products according to the request"""
        products_list = ""
        for product in self.__products:
            products_list += f"{str(product)}\n"
        return products_list

    @property
    def get_products(self):
        """Getter returns list of products according to the request"""
        products_list = []
        for product in self.__products:
            products_list.append(product)
        return products_list

    def middle_price(self):
        "Function that sums up all the prices in certain category and divides it by the amount of products"
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
