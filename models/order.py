from typing import List

from sqlmodel import JSON, Column, Field, SQLModel


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    total_price: float
    product_ids: List = Field(sa_column=Column(JSON))
    client_id: int
