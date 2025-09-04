 # test main.py

from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)


# TEST CREATE TOY
def test_create_toy():
    response = client.post(
        "/toys/",
        json={"name": "Football WORLD CUP", "price": 190.99, "in_stock": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Football WORLD CUP"
    assert data["price"] == 190.99
    assert data["in_stock"] is True
    assert "id" in data # ID should be auto generated

# TEST GET ALL TOYS
def test_read_toys():
    response = client.get("/toys/")
    assert response.status_code == 200
    data = response.json()
    assert  isinstance(data, list)
    assert  len(data) > 0


# TEST TOYS BY (GET ID)
def test_read_toy_by_id():
 # First create a toy
 new_toy = client.post("/toys/", json={"name": "Football WORLD CUP", "price": 190.99}).json()
 toy_id = new_toy["id"]

 # Now fetch it by ID
 response = client.get(f"/toys/{toy_id}")
 assert response.status_code == 200
 data = response.json
 assert data["id"] == toy_id
 assert data["name"] == "Football WORLD CUP"

# TEST UPDATE TOYS
def test_update_toy():
 # create a toy
 toy = client.post("/toys/", json={"name": "Football EURO'S CUP", "price": 170.89}).json()
 toy_id = toy["id"]

 #update it
 response = client.put(
     f"/toys/{toy_id}",
     json={"name": "Football EURO'S CUP", "price": 170.89}
 )
 assert response.status_code == 200
 data = response.json()
 assert data["name"] == "Football EURO'S CUP"
 assert data["price"] == 170.89

# TEST DELETE TOYS
def test_delete_toy():
    # create a toy
    toy = client.post("/toys/", json={"name": "Football NATION'S CUP", "price": 150.65}).json()
    toy_id = toy["id"]

    # Delete it
    response = client.delete(f"/toys/{toy_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Toy deleted"

    # Confirm it's gone
    response = client.get(f"/toys/{toy_id}")
    assert response.status_code == 404