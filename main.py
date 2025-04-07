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

@app.get('/product/{product_id}', response_model=pyd.BaseProduct)
def get_product(product_id:int,db:Session=Depends(get_db)):
    product=db.query(m.Product).filter(
        m.Product.id==product_id
    ).first()

    if not product:
        raise HTTPException(404, 'Товар не найден')
    return product

@app.post('/product', response_model=pyd.BaseProduct)
def create_product(product:pyd.CreateProduct, db:Session=Depends(get_db)):
    product_db=db.query(m.Product).filter(m.Product.name == product.name).first()
    if product_db:
        raise HTTPException(400, "Такой товар уже есть")
    product_db=m.Product()
    product_db.name=product.name

    db.add(product_db)
    db.commit()
    return(product_db)

@app.get('/types', response_model=List[pyd.BaseType])
def get_all_types(db:Session=Depends(get_db)):
    types=db.query(m.Type).all()
    return types

@app.get('/types/{types_id}', response_model=pyd.BaseType)
def get_type(type_id:int,db:Session=Depends(get_db)):
    type=db.query(m.Type).filter(
        m.Type.id==type_id
    ).first()

    if not type:
        raise HTTPException(404, 'Тип не найден')
    return type

@app.post('/type', response_model=pyd.BaseType)
def create_Type(type:pyd.CreateType, db:Session=Depends(get_db)):
    # type_db=db.query(m.Type).filter(m.Type.name == type.name).first()
    # if type_db:
    #     raise HTTPException(400, "Такой товар уже есть")
    type_db=m.Type()
    type_db.name=type.name
    type_db.undertype=type.undertype

    db.add(type_db)
    db.commit()
    return(type_db)