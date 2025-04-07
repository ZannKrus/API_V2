from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    name:str=Field(min_length=3, max_length=255, example="Молоко")
