from base import Base
from sqlalchemy import Column,String, Integer



class User(Base):
    __tablename__ = "users_prediction"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)

    class Config:
        orm_mode = True