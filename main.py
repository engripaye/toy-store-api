# Fast api
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# initialize fast api app
app = FastAPI(title="Toy store Api", version="1.0")

# In-memory database
toys = []


# pydantic model(defines structures of data)
class Toy(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


# ------- CRUD ENDPOINT ------#
# CREATE (Add new Toy)
@app.post("/toys/")
def add_toys(toy: Toy):
    # check if toy id exist
    for t in toys:
        if t["id"] == toy.id:
            raise HTTPException(status_code=400, detail="Toy with this ID already exist")

    toys.append(toy.dict())
    return {"message": "toys added successfully", "toy": toy}


# READ (Get all toys)
@app.get("/toys/")
def get_toys():
    return {"toys": toys}


# READ (Get a single toy by ID)
@app.get("/toys/{toy_id}")
def get_toy(toy_id: int):
    for toy in toys:
        if toy["id"] == toy_id:
            return toy
        raise HTTPException(status_code=404, detail="Toy not found")


# UPDATE (edit toy by ID)
@app.put("/toys/{toy_id}")
def update_toy(toy_id: int, updated_toy: Toy):
    for index, toy in enumerate(toys):
        if toy["id"] == toy_id:
            toys[index] = updated_toy.dict()
            return HTTPException(status_code=404, detail="Toy not found")


# Delete (Remove toy by id)
@app.delete("/toys/{toy_id}")
def delete_toy(toy_id: int):
    for index, toy in enumerate(toys):
        if toy["id"] == toy_id:
            deleted = toys.pop(index)
            return {"message": "Toy deleted successfully", "toys": deleted}
        raise HTTPException(status_code=404, detail="Toy not found")
