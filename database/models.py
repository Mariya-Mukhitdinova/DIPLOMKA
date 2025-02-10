from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from datetime import datetime


# модель юзеров
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    phone_number = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now)


# модель товаров
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_prod = Column(String, nullable=False)
    dict_prod = Column(String, nullable=False)
    price = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

class Photo(Base):
    __tablename__ = 'photos'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String, nullable=False)
    prod_id = Column(Integer, ForeignKey('products.id'), nullable=True)
    product = relationship("Product", lazy="subquery")
# uvicorn main:app --reload запуск проекта
class Cart(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1)
    user = relationship("User")
    product = relationship("Product")

