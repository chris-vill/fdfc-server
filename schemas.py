from pydantic import BaseModel
from typing import Optional

class UserInfoResponse(BaseModel):
  id: int
  occupation: Optional[str] = None
  civil_status: Optional[str] = None
  address_permanent: Optional[str] = None
  address_temporary: Optional[str] = None
  mobile: Optional[str] = None
  landline: Optional[int] = None
  email_address: Optional[str] = None

  class Config:
        orm_mode = True

class UserRequest(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class AdditionalInfoRequest(BaseModel):
    id: int
    occupation: str
    civil_status: str

    class Config:
        orm_mode = True

class LocationInfoRequest(BaseModel):
    id: int
    address_permanent: str
    address_temporary: str

    class Config:
        orm_mode = True

class ContactInfoRequest(BaseModel):
    id: int
    mobile: str
    landline: int
    email_address: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str