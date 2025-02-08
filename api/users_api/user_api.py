from fastapi import APIRouter, Depends
from database.userservice import *

# объект нашего компонента
user_router = APIRouter(prefix='/user',
                        tags=['Клиенты'])


# регистрация
@user_router.post('/register')
async def register_user(username: str, phone_number: str, password: str):
    result = add_user_db(name=username, phone_number=phone_number, password=password)
    if result:
        return {"message": "Регистрация прошла успешно!"}
    return {"message": result}


# получение всех юзеров
@user_router.post('/users_all')
async def users_all(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()
        return {'message': result}
    else:
        result = concrentniy_user_db(user_id)
        return {'message': result}

class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    phone_number: Optional[str] = None

# изменение данных о юзере
@user_router.put('/edit_user')
async def edit_user(user_id:  int, user_update: UpdateUser, db: Session =Depends(get_db)):
    result = change_info_user_db(db, user_id, user_update)
    if result:
        return {"message": "Изменения прошли успешно"}
    return {"message": result}


# удаление юзера
@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)
    if result:
        return {"message": "Клиент удален!"}
    else:
        return {"message": result}
