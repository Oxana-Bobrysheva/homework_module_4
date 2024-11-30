
class Product:
    """Класс для представления продукции"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product, products):
        for product in products.get_products:
            if product.name == new_product["name"]:
                product.quantity += new_product["quantity"]
                product.price = max(product.price, new_product["price"])
                return product
        return cls(new_product["name"], new_product["description"],
                   new_product["price"], new_product["quantity"])

    @property
    def price(self):
        """The price property"""
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            answer = input("Цена на товар снизилась?\nЕсли да, то введите 'y', если нет, то введите 'n': ")
            if answer == "y":
                self.__price = value
            else:
                print("Цена не была изменена.")
        return self.__price
