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

# изменение инфы о товаре
def change_info_product_db(id, change_info, new_info):
    with next(get_db()) as db:
        info_product = db.query(Product).filter_by(id=id).first()
        if info_product:
            if change_info == "name_prod":
                info_product.name_prod = new_info
            if change_info == "dict_prod":
                info_product.dict_prod = new_info
            if change_info == "price":
                info_product.price = new_info
            if change_info == "category":
                info_product.category = new_info
            if change_info == "quantity":
                info_product.quantity = new_info
            else:
                return False
            db.commit()
            return "Изменения прошли успешно!"
        else:
            return "Товар не найден"

# удаление товара
def delete_prod_db(id):
    with next(get_db()) as db:
        delete_prod = db.query(Product).filter_by(id).first()
        if delete_prod:
            db.delete(delete_prod)
            db.commit()
            return "Товар удален"
        return "Товар не найден"
