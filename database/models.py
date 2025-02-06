from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


# модель юзеров
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# модель товаров
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_prod = Column(String, nullable=False)
    dict_prod = Column(String, nullable=False)
    price = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
