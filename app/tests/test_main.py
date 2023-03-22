from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_callname():
    response = client.get("/callname/iffan")
    assert response.status_code == 200
    assert response.json() == {"hello": "iffan"}
    
def test_callname():
    response = client.post("/callname", data={"name": "iffan"})
    assert response.status_code == 200
    assert response.json() == {"hello": "iffan"}
