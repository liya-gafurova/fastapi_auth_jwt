from sqlalchemy import String, Column, DateTime

from app.db.base_class import Base


class Post(Base):
    id = Column(String)
    title = Column(String)
    text = Column(String)
    created = Column(DateTime(timezone=True))
