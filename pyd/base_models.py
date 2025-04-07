from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id:int=Field(example=1)
    name:str=Field(example="Молоко")

class BaseType(BaseModel):
    id:int=Field(example=1)
    name:str=Field(example="Электроника")
    undertype:str=Field(example="Телефон")
