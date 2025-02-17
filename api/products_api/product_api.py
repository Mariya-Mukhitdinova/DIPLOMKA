from fastapi import APIRouter, Depends, UploadFile, File
from database.productservice import *
import os

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
async def products_all_db(id: int=0):
    result = get_products_db()
    if id == 0:
        return {'message': result}
    else:
        result = concretniy_product_db(id)
        return {'message': result}


# изменение инфы о товаре
class UpdateProduct(BaseModel):
    name_prod: Optional[str] = None
    dict_prod: Optional[str] = None
    category: Optional[str] = None
    price: Optional[str] = None
    quantity: Optional[str] = None


@product_router.put('/edit_prod')
async def edit_product(id:  int,
                       prod_update: UpdateProduct,
                       db: Session =Depends(get_db)):

    result = change_info_prod_db(db,id,prod_update)
    if result:
        return {'message': "Информация о товаре изменена"}
    return {'message': result}


# удаление товара
@product_router.delete('/delete_prod')
async def delete_prod(id):
    result = delete_prod_db(id)
    if result:
        return {'message': "Товар удален"}
    return {'message': result}

#добавление фото продукта
@product_router.post('/add_photo')
async def add_photo(id: int, prod_photo: UploadFile = File(...)):
    os.makedirs('media', exist_ok=True)
    file_path = f'media/{prod_photo.filename}'
    with open(file_path, 'wb+') as file:
        photo_product = await prod_photo.read()
        file.write(photo_product)
    result = prod_photo_db(id=id, prod_path=f'/media/{prod_photo.filename}')
    return {'message': "Фото загружено", 'photo': result}  # Добавил более ясное сообщение







   # @product_router.delete('/dell_photo')
# async def del_photo(id):
#     result = del_prod_photo_db(id)
#     if result:
#           return {'message': "Картинка удалена"}
#     return {'message': result}


