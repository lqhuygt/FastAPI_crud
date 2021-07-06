from fastapi import APIRouter,Depends,status,HTTPException
from .. import database
from ..model import Models
from sqlalchemy.orm import Session
from ..repository import UserRepository

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=Models.ShowUser)
def createUser(request: Models.User,db: Session = Depends(get_db)):
    return UserRepository.create(request,db)

@router.get('/{id}',response_model=Models.ShowUser)
def getUser(id:int,db: Session = Depends(get_db)):
    return UserRepository.show(id,db)