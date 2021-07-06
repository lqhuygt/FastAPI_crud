from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from ..model import Models
from .. import database
from fastapi import HTTPException, status

def create(request: Models, db: Session):
    new_blog = database.Blog(
        title = request.title, 
        description = request.description,
        user_id= request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(id: int, request: Models ,db: Session):
    blog = db.query(database.Blog).filter(database.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.update(request.dict()) # add dict() vì data ở dạng json = dict
    db.commit()
    return "Updated"

def delete(id:int, db: Session):
    blog = db.query(database.Blog).filter(database.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False) 
    db.commit()
    return  "Deleted"

def get_all(db: Session):
    blogs = db.query(database.Blog).all()
    return blogs

def getById(id: int, db: Session):
    blog = db.query(database.Blog).filter(database.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Blog with the id {id} is not available")
    return blog

