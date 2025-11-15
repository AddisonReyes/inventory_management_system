import random
from typing import List

from models.product import Product

dummy_products = [
    "One Plus S1",
    "Samsung Galaxy A16",
    "iPhone 8",
    "Backberry 8",
    "Galaxy Z Fold7",
]


def generate_data():
    new_products: List[Product] = []
    for i, product in enumerate(dummy_products):
        prod = Product(
            name=product,
            price=random.randrange(100, 1600),
            quantity=random.randint(0, 30),
        )
        new_products.append(prod)
    return new_products


if __name__ == "__main__":
    generate_data()
