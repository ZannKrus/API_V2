from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd

app=FastAPI()

@app.get('/products', response_model=List[pyd.BaseProduct])
def get_all_products(db:Session=Depends(get_db)):
    products=db.query(m.Product).all()
    return products