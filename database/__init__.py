from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# указываем тип и название базы данных
SQLALCHEMY_DATABASE_URL = 'sqlite:///data3.db'
# создаем движок нашей базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# создание функции для создания сессий
SessionLocal = sessionmaker(bind=engine)
# создаем супер класс для моделей (будет его наследовать как Models в джанго
Base = declarative_base()

# создание функции-генератора запуска сессий

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()




