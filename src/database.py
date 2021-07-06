from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import Column
from sqlalchemy import Integer, String, ForeignKey

DATABASE_URL = "postgresql://postgres:huy12345678@127.0.0.1:5432/DB_Test_Fastapi"
engine = create_engine(DATABASE_URL) # tạo engine để connect với db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # tạo một phiên của db
Base = declarative_base() # tạo ra mô hình orm

# tạo tables class
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates= "blogs") # tạo quan hệ bảng user

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog', back_populates="creator")

# Denpendecy injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()