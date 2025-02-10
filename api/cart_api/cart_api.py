from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.cartservise import *
from database import get_db
from pydantic import BaseModel
from typing import Optional

# объект нашего компонента
cart_router = APIRouter(prefix='/cart', tags=['Корзина'])

# добавление товара в корзину
class AddToCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int

@cart_router.post('/add', response_model=dict)
async def add_to_cart(data: AddToCartRequest, db: Session = Depends(get_db)):
    result = add_to_cart_db(db, data.user_id, data.product_id, data.quantity)
    if not result:
        raise HTTPException(status_code=400, detail="Ошибка добавления в корзину")
    return {"message": "Товар добавлен в корзину!"}
    # удаление товара из корзины
@cart_router.delete('/delete_product')
async def delete_from_cart(user_id: int, product_id: int, db: Session = Depends(get_db)):
    result = delete_from_cart_db(db, user_id, product_id)
    if not result:
        raise HTTPException(status_code=404, detail='Товар не найден в корзине')
    return {"message": "Товар удален из корзины"}

# Получить содержимое корзины
@cart_router.get('/')
async def get_cart(user_id: int, db: Session = Depends(get_db)):
    cart_items = get_cart_db(db, user_id)
    return {"cart": cart_items}

# очистить корзину
@cart_router.delete('/delete_cart')
async def delete_cart(user_id: int, db: Session = Depends(get_db)):
    result = delete_cart_db(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Корзина уже пуста или не найдена")
    return {"message": "Корзина очищена!"}

# изменить количество товара в корзине
class UpdateCartRequest(BaseModel):
    user_id: int
    product_id: int
    quantity: int

@cart_router.put('/update')
async def update_cart(data: UpdateCartRequest, db: Session = Depends(get_db)):
    result = update_cart_db(db, data.user_id, data.product_id, data.quantity)
    cart_item = db.query(Cart).filter(Cart.user_id == data.user_id, Cart.product_id == data.product_id).first()
    print(f"Текущий товар в корзине перед обновлением: {cart_item}")

    print(f"Обновление: {data.dict()}")

    if not result:
        raise HTTPException(status_code=404, detail="Ошибка обновления корзины")
    print(data.dict())
    return {"message": "Количество товара обновлено!"}



