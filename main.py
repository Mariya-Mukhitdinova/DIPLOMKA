from fastapi import FastAPI

from api.products_api.product_api import product_router
from api.users_api.user_api import user_router

app = FastAPI(docs_url="/", title='МАГАЗИН LIMON', description='Эксклюзивные ручки')
# делаем миграции (первичная - первый раз только сработает)
from database import Base, engine
Base.metadata.create_all(bind=engine)

# регитрируем компонент (роутер)

app.include_router(user_router)
app.include_router(product_router)
