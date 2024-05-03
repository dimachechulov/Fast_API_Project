from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str
    price : float = Field(gt=0)