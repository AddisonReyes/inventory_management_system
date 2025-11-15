import uvicorn
from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select

from dummy_data import generate_data
from models.product import Product

app = FastAPI()
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)


@app.get("/")
async def index():
    return "Hello world!"


def create_dummy_data():
    products_list = generate_data()
    with Session(engine) as session:
        for p in products_list:
            statement = select(Product).where(Product.name == p.name)
            prod = session.exec(statement).first()
            if not prod:
                session.add(p)
        session.commit()


if __name__ == "__main__":
    create_dummy_data()

    uvicorn.run(
        app="main:app",
        log_level="info",
        reload=True,
        port=3000,
    )
