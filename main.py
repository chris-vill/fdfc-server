from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db_handler import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
  title="FDFC Server",
  version="1.0.0"
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/session", response_model=schemas.UserInfoResponse)
def post_session(request: schemas.UserRequest, db: Session=Depends(get_db)):
  user = crud.get_user(
    db=db,
    username=request.username
  )
  return user

@app.post("/register", response_model=schemas.UserInfoResponse)
def post_register(request: schemas.UserRequest, db: Session=Depends(get_db)):
  response = crud.add_user(
    db=db,
    username=request.username,
    password=request.password
  )
  return response

@app.put("/additional-info")
def put_additional_info(request: schemas.AdditionalInfoRequest, db: Session=Depends(get_db)):
  crud.set_additional_info(
    db=db,
    id=request.id,
    civil_status=request.civil_status,
    occupation=request.occupation
  )
  return {}

@app.put("/contact-info")
def put_contact_info(request: schemas.ContactInfoRequest, db: Session=Depends(get_db)):
  crud.set_contact_info(
    db=db,
    id=request.id,
    mobile=request.mobile,
    landline=request.landline,
    email_address=request.email_address
  )
  return {}

@app.put("/location-info")
def put_location_info(request: schemas.LocationInfoRequest, db: Session=Depends(get_db)):
  crud.set_location_info(
    db=db,
    id=request.id,
    address_permanent=request.address_permanent,
    address_temporary=request.address_temporary
  )
  return {}

###
#
# Model
# - user
#   - username
#   - password
#   - registration_status
#       - step1
#       - step2
#       - step3
#       - finished
#   - address_permanent
#   - address_temporary
#   - occupation
#   - civil_status
#   - mobile
#   - landline
#   - email_address
#
#
#
# Login
#
# POST /session
#
# DELETE /session
#
# Register
###