from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import database, oauth2
from ..model import Models
from sqlalchemy.orm import Session
from ..repository import BlogRepository

# khai báo api router để điều hướng đến main
router = APIRouter(
    prefix="/blog",
    tags=['Blogs'] # tên trong documentation
)

# gọi DI để nhúng vào mỗi requet
get_db = database.get_db

@router.post("/", status_code= status.HTTP_201_CREATED)
def createBlog(request: Models.Blog, db: Session = Depends(get_db), current_user: Models.User = Depends(oauth2.get_current_user)):
    return BlogRepository.create(request, db)

@router.get("/", response_model= List[Models.ShowBlog])
def getAllBlog(db: Session = Depends(get_db), current_user: Models.User = Depends(oauth2.get_current_user)):
    return BlogRepository.get_all(db)

@router.get("/{id}", response_model= Models.ShowBlog)
def getBlog(id: int, db: Session = Depends(get_db), current_user: Models.User = Depends(oauth2.get_current_user)):
    return BlogRepository.getById(id,db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id: int, request: Models.Blog, db: Session = Depends(get_db), current_user: Models.User = Depends(oauth2.get_current_user)):
    return BlogRepository.update(id,request,db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id: int, db: Session = Depends(get_db), current_user: Models.User = Depends(oauth2.get_current_user)):
    return BlogRepository.delete(id,db) # vẫn xóa đưuọc nhưng bắn ra log
  