from pydantic import BaseModel


# Request/Response schema
class ToyBase(BaseModel):
    name: str
    price: float
    in_stock: bool


class ToyCreate(ToyBase):
    pass


class Toy(ToyBase):
    id: int

    class Config:
        form_attributes = True
