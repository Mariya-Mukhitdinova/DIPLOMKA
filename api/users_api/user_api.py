from fastapi import APIRouter
from database.userservice import *

# объект нашего компонента
user_router = APIRouter(prefix='/user',
                        tags=['Клиенты'])


# регистрация
@user_router.post('/register')
async def register_user(username: str, phone_number: str, password: str):
    result = add_user_db(name=username, phone_number=phone_number, password=password)
    if result:
        return {"message": result}
    return {"message": "Ошибка"}


# получение всех юзеров
@user_router.post('/users_all')
async def users_all(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()
        return {'message': result}
    else:
        result = concrentniy_user_db(user_id)
        return {'message': result}


# изменение данных о юзере
@user_router.put('/edit_user')
async def edit_user(id, change_info, new_info):
    result = change_info_user_db(id, change_info, new_info)
    if result:
        return {"message": "Изменения прошли успешно!"}
    return {"message": result}


# удаление юзера
@user_router.delete('/delete_user')
async def delete_user(id):
    result = delete_user_db(id)
    if result:
        return {"message": "Клиент удален"}
    else:
        return {"message": "Клиент не найден"}
