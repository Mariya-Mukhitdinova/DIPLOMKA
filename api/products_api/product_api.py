from fastapi import APIRouter
from database.productservice import *

# объект нашего компонента
product_router = APIRouter(prefix='/product',
                           tags=['Товары'])


# добавление товара
@product_router.post('/add_product')
async def add_product(name_prod, dict_prod, price, category, quantity):
    result = add_product_db(name_prod=name_prod, dict_prod=dict_prod,
                            price=price, category=category, quantity=quantity)
    if result:
        return {"message": "Продукт успешно добавлен!"}
    return {"message": result}


# получение всех товаров и получение информации о конкретном товаре
@product_router.post('/products_all')
async def products_all_db(id):
    result = get_products_db()
    if id == 0:
        return {'message': result}
    else:
        result = concretniy_product_db(id)
        return {'message': result}


# изменение инфы о товаре

@product_router.put('/edit_prod')
async def edit_product(id, change_info, new_info):
    result = change_info_product_db(id, change_info, new_info)
    if result:
        return {'message': "Информация изменена"}
    return {'message': result}


# удаление товара
@product_router.delete('/delete_prod')
async def delete_prod(id):
    result = delete_prod_db(id)
    if result:
        return {'message': "Товар удален"}
    return {'message': result}
