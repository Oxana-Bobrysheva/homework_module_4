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

if __name__ == "__main__":
    product1 = Product("potatoes", "Kursk origin", 40.5, 25)
    product2 = Product("tomatoes", "Belgorod origin", 140.5, 35)
    product3 = Product("carrot", "Oboyan origin", 50.5, 45)

    category = Category("Vegetables", "Fresh vegetables", [product1, product2, product3])

    print(category.name)
    print(category.description)
    print(category.products)

    print(category.category_count)
    print(Category.all_product_count)