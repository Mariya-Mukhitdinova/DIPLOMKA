from typing import Optional

from pydantic import BaseModel
from sqlalchemy.orm import Session

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


# получение информации о конкретном юзере
def concrentniy_user_db(id):
    with next(get_db()) as db:
        concretniy_user = db.query(User).filter_by(id=id).first()
        if concretniy_user:
            return concretniy_user
        return "Юзер не найден"

# изменения данных о клиенте
class UpdateUser(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    phone_number: Optional[str] = None


def change_info_user_db(db: Session, user_id: int, user_update: UpdateUser):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None

    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


# удаление юзера
def delete_user_db(id):
    with next(get_db()) as db:
        delete_user = db.query(User).filter_by(id=id).first()
        if delete_user:
            db.delete(delete_user)
            db.commit()
            return "Юзер успешно удален!"
        return "Юзер не найден!"
