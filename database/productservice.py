from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from database.models import *


# добавление товара
def add_product_db(name_prod, dict_prod, price, category, quantity):
    with next(get_db()) as db:
        new_product = Product(name_prod=name_prod, dict_prod=dict_prod,
                              price=price, category=category, quantity=quantity)
        db.add(new_product)
        db.commit()
        return "Продукт успешно добавлен!"


# получение всех товаров
def get_products_db():
    with next(get_db()) as db:
        all_products = db.query(Product).all()
        return all_products


# получение информации о конкретном товаре
def concretniy_product_db(id):
    with next(get_db()) as db:
        concretniy_product = db.query(Product).filter_by(id=id).one()
        if concretniy_product:
            return concretniy_product
        return "Товар не найден"


# изменение данных о продукте
class UpdateProduct(BaseModel):
    name_prod: Optional[str] = None
    dict_prod: Optional[str] = None
    category: Optional[str] = None
    price: Optional[str] = None
    quantity: Optional[str] = None


def change_info_prod_db(db: Session, id: int, product_update: UpdateProduct):
    db_product = db.query(Product).filter(Product.id == id).first()
    if db_product is None:
        return None

    for field, value in product_update.dict(exclude_unset=True).items():
        setattr(db_product, field, value)

    db.commit()
    db.refresh(db_product)
    return db_product


# удаление товара
def delete_prod_db(id):
    with next(get_db()) as db:
        delete_prod = db.query(Product).filter_by(id=id).first()
        if delete_prod:
            db.delete(delete_prod)
            db.commit()
            return "Товар удален"
        return "Товар не найден"


# добавление фото продукта
def prod_photo_db(id, prod_path):
    db = next(get_db())

    product = db.query(Product).filter_by(id=id).first()
    if not product:
        return {'message': 'товар не найден'}
    new_photo = Photo(photo_path=prod_path, prod_id=id)
    db.add(new_photo)
    db.commit()
    return {'message': 'Фото успешно добавлено', 'photo': new_photo}



# def del_prod_photo_db(id):
#     db = next(get_db())
#
#     checker = db.query(Product).filter_by(id=id).first()
#     if checker:
#         db.delete(checker)
#         db.commit()
#     else:
#         return {'message': 'Ошибка'}