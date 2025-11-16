from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
