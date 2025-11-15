import random
from typing import List

from sqlmodel import Session, SQLModel, create_engine, select

from models.product import Product

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)
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

    with Session(engine) as session:
        for p in new_products:
            statement = select(Product).where(Product.name == p.name)
            prod = session.exec(statement).first()
            if not prod:
                session.add(p)
        session.commit()


if __name__ == "__main__":
    generate_data()
