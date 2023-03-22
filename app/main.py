from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/hello/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.get("/callname/{name}")
def call_name(name: str):
    return {"hello": name}

@app.post("/callname")
def call_name(name: str):
    return {"hello": name}

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_callname():
    name = "Iffanz"
    response = client.post("/callname", json={"name": name})
    assert response.status_code == 200
    assert response.json() == {"hello": name}

handler = Mangum(app)
