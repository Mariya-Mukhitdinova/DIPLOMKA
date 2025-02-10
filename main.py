from fastapi import FastAPI

from api.products_api.product_api import product_router
from api.users_api.user_api import user_router
from api.cart_api.cart_api import cart_router

from sqlalchemy import text
app = FastAPI(docs_url="/", title='МАГАЗИН LIMON', description='Эксклюзивные ручки')
# делаем миграции (первичная - первый раз только сработает)
from database import Base, engine
with engine.connect() as conn:
    result = conn.execute(text("PRAGMA table_info(cart_items);"))
    print(result.fetchall())




Base.metadata.create_all(bind=engine)

# регитрируем компонент (роутер)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)
for route in app.router.routes:
    print(f"Маршрут: {route.path} | Методы: {route.methods}")
