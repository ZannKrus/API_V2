from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id:int=Field(example=1)
    name:str=Field(example="Молоко")
