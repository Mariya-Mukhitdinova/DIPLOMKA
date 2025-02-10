from sqlalchemy.orm import Session
from database.models import Cart, Product, User

# добавляем продукт в корзину
def add_to_cart_db(db: Session, user_id: int, product_id: int, quantity: int):
  #провкряем существует ли товар
    product = db.query(Product).filter(Product.id == product_id)
    if not product:
        return None
    # проверяем, есть ли товар уже в корзине клиента
    cart_item = db.query(Cart).filter(Cart.user_id == user_id,
                                      Cart.product_id == product_id).first()
    if cart_item:
        # если есть добавить количество
        cart_item.quantity += quantity
    else:
        new_car_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        db.add(new_car_item)
    db.commit()
    return True

# удалить товар из корзины
def delete_from_cart_db(db: Session, user_id: int, product_id: int):
    cart_item = db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    if cart_item:
        db.delete(cart_item)
        db.commit()
        return True
    return True

# получить содержимое корзины
def get_cart_db(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    return cart_items

# очистить корзину
def delete_cart_db(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    if cart_items:
        for item in cart_items:
            db.delete(item)
        db.commit()
        return True
    return False

# обновить количество товара в корзине
def update_cart_db(db:Session, user_id: int, product_id: int, quantity: int):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id, Cart.product_id == product_id).first()
    if cart_items:
        if quantity > 0:
            cart_items.quantity = quantity
        else:
            # если количество 0 удалить
            db.delete(cart_items)
        db.commit()
        return True
    print(f"Не найден товар {product_id} в корзине пользователя {user_id}")
    return False