# Fast api
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Toy store API", version="2.0")

# Dependency: get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ------- CRUD ENDPOINT ------#
# CREATE (POST) (Add new Toy)
@app.post("/toys/", response_model=schemas.Toy)
def create_toy(toy: schemas.ToyCreate, db: Session = Depends(get_db)):
    db_toy = models.Toy(**toy.dict())
    db.add(db_toy)
    db.commit()
    db.refresh(db_toy)
    return db_toy


# READ (Get all toys)
@app.get("/toys/", response_model=list[schemas.Toy])
def read_toys(db: Session = Depends(get_db)):
    return db.query(models.Toy).all()


# READ (Get a single toy by ID)
@app.get("/toys/{toy_id}", response_model=schemas.Toy)
def read_toy(toy_id: int, db: Session = Depends(get_db)):
    toy = db.query(models.Toy).filter(models.Toy.id == toy_id).first()
    if not toy:
        raise HTTPException(status_code=404, detail="Toy not found")
    return toy


# UPDATE (edit toy by ID)
@app.put("/toys/{toy_id}", response_model=schemas.Toy)
def update_toy(toy_id: int, updated_toy: schemas.ToyCreate, db: Session = Depends(get_db)):
    toy = db.query(models.Toy).filter(models.Toy.id == toy_id).first()
    if not toy:
        raise HTTPException(status_code=404, detail="Toy not found")

    toy.name = updated_toy.name
    toy.price = updated_toy.price
    toy.in_stock = updated_toy.in_stock

    db.commit()
    db.refresh(toy)
    return toy



# Delete (Remove toy by id)
@app.delete("/toys/{toy_id}")
def delete_toy(toy_id: int, db: Session = Depends(get_db)):
    toy = db.query(models.Toy).filter(models.Toy.id == toy_id).first()
    if not toy:
        raise HTTPException(status_code=404, detail="Toy not found")

    db.delete(toy)
    db.commit()
    return {"message": "Toy deleted successfully"}