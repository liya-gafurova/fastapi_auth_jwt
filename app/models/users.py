from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, Column

from app.db.base_class import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String)