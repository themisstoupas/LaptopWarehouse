from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0, description="Price must be greater than zero")
    quantity: Optional[int] = Field(None, ge=0, description="Quantity cannot be negative")


class StockPayLoad(BaseModel):
    action: str
    quantity: int = Field(gt=0, description="Quantity must be a positive integer")
