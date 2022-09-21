from datetime import timedelta
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from constants import ACCESS_TOKEN_EXPIRE_MINUTES
import models
import schemas
import utils

def authn_user(db: Session, username: str, password: str):
  user = db.query(models.UserInfo).filter(models.UserInfo.username == username).first()
  is_authed = utils.verify_password(password, user.password)

  if not is_authed:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )

  access_token = utils.create_token(
    data={
      "id": user.id,
      "registration_status": user.registration_status,
      "address_permanent": user.address_permanent,
      "address_temporary": user.address_temporary,
      "occupation": user.occupation,
      "civil_status": user.civil_status,
      "mobile": user.mobile,
      "landline": user.landline,
      "email_address": user.email_address,
    },
    expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  )

  return {
    "access_token": access_token,
    "token_type": "bearer"
  }

def get_user(current_user: schemas.UserInfoResponse=Depends(utils.get_current_user)):
  return current_user

def add_user(db: Session, username: str, password: str):
  user_info = models.UserInfo(
    username=username,
    password=utils.create_password_hash(password),
    registration_status="step1"
  )

  db.add(user_info)
  db.commit()
  db.refresh(user_info)

  return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

def set_additional_info(db: Session, id: int, civil_status: str, occupation: str, current_user=Depends(utils.get_current_user)):
  db.query(models.UserInfo).filter(models.UserInfo.id == id).update({
    "civil_status": civil_status,
    "occupation": occupation,
    "registration_status": "step2"
  })
  db.commit()

  return True

def set_contact_info(db: Session, id: int, mobile: str, landline: int, email_address: str):
  db.query(models.UserInfo).filter(models.UserInfo.id == id).update({
    "mobile": mobile,
    "landline": landline,
    "email_address": email_address,
    "registration_status": "finished"
  })
  db.commit()

  return True

def set_location_info(db: Session, id: int, address_permanent: str, address_temporary: str):
  db.query(models.UserInfo).filter(models.UserInfo.id == id).update({
    "address_permanent": address_permanent,
    "address_temporary": address_temporary,
    "registration_status": "step3"
  })
  db.commit()

  return True