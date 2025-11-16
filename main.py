import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, SQLModel, create_engine, select

from models.client import Client
from models.order import Order
from models.product import Product

engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        "title": "IMS - Inventory Management System",
        "message": "Hello world!",
    }

    return templates.TemplateResponse("index.html", context)


@app.get("/products")
async def products(request: Request):
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        context = {
            "request": request,
            "products": products,
        }

        return templates.TemplateResponse("products.html", context)


@app.get("/orders")
async def orders(request: Request):
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        context = {
            "request": request,
            "orders": orders,
        }

        return templates.TemplateResponse("orders.html", context)


@app.get("/clients")
async def clients(request: Request):
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
        context = {
            "request": request,
            "clients": clients,
        }

        return templates.TemplateResponse("clients.html", context)


if __name__ == "__main__":

    uvicorn.run(
        app="main:app",
        log_level="info",
        reload=True,
        port=3000,
    )
