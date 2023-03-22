from fastapi import FastAPI, Form
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/callname/{name}")
def call_name(name: str):
    return {"hello": name}

@app.post("/callname")
def call_name(name: str = Form(...)):
    return {"hello": name}

handler = Mangum(app)
