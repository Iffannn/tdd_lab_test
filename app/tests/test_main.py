from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_callname():
    name = "Iffan"
    response = client.get("f'/callname/{name}")
    assert response.status_code == 200
    assert response.json() == {"hello": name}
    
def test_callname_post():
    name = "Iffanz"
    response = client.post("f'/callname", data={"name": name})
    assert response.status_code == 200
    assert response.json() == {"hello": name}
