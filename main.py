from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
  "http://localhost",
  "http://localhost:3000",
  "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/login", response_model=schemas.UserInfoResponse)
def post_login(request: schemas.UserRequest, db: Session=Depends(get_db)):
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

@app.put("/additional-info", response_model=schemas.UserInfoResponse)
def put_additional_info(request: schemas.AdditionalInfoRequest, db: Session=Depends(get_db)):
  response = crud.set_additional_info(
    db=db,
    id=request.id,
    civil_status=request.civil_status,
    occupation=request.occupation
  )
  return response

@app.put("/contact-info", response_model=schemas.UserInfoResponse)
def put_contact_info(request: schemas.ContactInfoRequest, db: Session=Depends(get_db)):
  response = crud.set_contact_info(
    db=db,
    id=request.id,
    mobile=request.mobile,
    landline=request.landline,
    email_address=request.email_address
  )
  return response

@app.put("/location-info", response_model=schemas.UserInfoResponse)
def put_location_info(request: schemas.LocationInfoRequest, db: Session=Depends(get_db)):
  response = crud.set_location_info(
    db=db,
    id=request.id,
    address_permanent=request.address_permanent,
    address_temporary=request.address_temporary
  )
  return response