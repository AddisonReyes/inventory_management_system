import random
from typing import List

from sqlmodel import Session, SQLModel, create_engine, select

from models.client import Client
from models.order import Order
from models.product import Product

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

dummy_products: list[str] = [
    "One Plus S1",
    "Samsung Galaxy A16",
    "iPhone 8",
    "Backberry 8",
    "Galaxy Z Fold7",
]
dummy_clients: list[str] = [
    "Addison Reyes",
    "Maria Gutierrez",
    "Michell Gomez",
]


def generate_data():
    new_products: List[Product] = []
    for product in dummy_products:
        prod = Product(
            name=product,
            price=random.randrange(100, 1600),
            quantity=random.randint(0, 30),
        )
        new_products.append(prod)

    new_clients: List[Client] = []
    for client in dummy_clients:
        c = Client(name=client)
        new_clients.append(c)

    with Session(engine) as session:
        new_orders: List[Client] = []
        for i in range(6):
            product_ids = [
                random.randint(1, len(dummy_products))
                for _ in range(random.randint(1, 4))
            ]
            statement = select(Product).where(Product.id in product_ids)
            products = session.exec(statement).all()
            total_price = 0
            for product in products:
                total_price += product.price

            order = Order(
                name=f"Order #{i + 1}",
                total_price=total_price,
                product_ids=product_ids,
                client_id=1,
            )
            new_orders.append(order)

        for p in new_products:
            statement = select(Product).where(Product.name == p.name)
            prod = session.exec(statement).first()
            if not prod:
                session.add(p)

        for c in new_clients:
            statement = select(Client).where(Client.name == c.name)
            client = session.exec(statement).first()
            if not client:
                session.add(c)

        for o in new_orders:
            statement = select(Order).where(Order.name == o.name)
            client = session.exec(statement).first()
            if not client:
                session.add(o)

        session.commit()


if __name__ == "__main__":
    generate_data()
