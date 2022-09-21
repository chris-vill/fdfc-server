from sqlalchemy import Column, Integer, String
from db_handler import Base

class UserInfo(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    username = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), index=True, nullable=False)
    registration_status = Column(String, index=True, nullable=True)
    address_permanent = Column(String(255), index=True, nullable=True)
    address_temporary = Column(String(255), index=True, nullable=True)
    occupation = Column(String(255), index=True, nullable=True)
    civil_status = Column(String(255), index=True, nullable=True)
    mobile = Column(String(255), index=True, nullable=True)
    landline = Column(Integer, index=True, nullable=True)
    email_address = Column(String(255), index=True, nullable=True)