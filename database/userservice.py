from database import get_db
from database.models import *

# добавление юзера
def add_user_db(name, phone_number, password):
    # создание сессии
    with next(get_db()) as db:
        new_user = User(username=name, phone_number=phone_number, password=password)
        db.add(new_user)
        db.commit()
        return "Клиент успешно добавлен!"
# получение всех юзеров
def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users

#получение информации о конкретном юзере
def concrentniy_user_db(id):
    with next(get_db()) as db:
        concretniy_user = db.query(User).filter_by(id=id).one()
        if concretniy_user:
            return concretniy_user
        return "Юзер не найден"

# изменение данных о юзере
def change_info_user_db(id, change_info, new_info):
    with next(get_db()) as db:
        info_user = db.query(User).filter_by(id=id).first()
        if info_user:
            if change_info == "name":
                info_user.name = new_info
            if change_info == "phone_number":
                info_user.phone_number = new_info
            if change_info == "password":
                info_user.password = new_info
            else:
                return False
            db.commit()
            return "Изменения прошли успешно!"
        else:
            return "Пользователь не найден"


# удаление юзера
def delete_user_db(id):
    with next(get_db()) as db:
        delete_user = db.query(User).filter_by(id=id).first()
        if delete_user:
            db.delete(delete_user)
            db.commit()
            return "Юзер успешно удален!"
        return "Юзер не найден!"

