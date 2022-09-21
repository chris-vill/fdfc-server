from sqlalchemy.orm import Session
import models
import schemas

def get_user(db: Session, username: str):
  return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

def add_user(db: Session, username: str, password: str):
  user_info = models.UserInfo(
    username=username,
    password=password,
    registration_status="step1"
  )

  db.add(user_info)
  db.commit()
  db.refresh(user_info)

  return db.query(models.UserInfo).filter(models.UserInfo.username == username).first()

def set_additional_info(db: Session, id: int, civil_status: str, occupation: str):
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