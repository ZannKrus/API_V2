from database import Base
from sqlalchemy import Column, Integer, String

class Product(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
