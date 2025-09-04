# Fast api
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# initilaize fast api app
app = FastAPI(title="Toy store Api", version="1.0")

# In-memory database
toys = []


# pyandic model(defines structures of data)
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
