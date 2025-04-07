from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    name:str=Field(min_length=3, max_length=255, example="Молоко")

class CreateType(BaseModel):
    name:str=Field(min_length=3, max_length=255, example="Электроника")
    undertype:str=Field(min_length=3, max_length=255, example="Телефон")
