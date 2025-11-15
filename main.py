import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import SQLModel, create_engine

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


if __name__ == "__main__":

    uvicorn.run(
        app="main:app",
        log_level="info",
        reload=True,
        port=3000,
    )
