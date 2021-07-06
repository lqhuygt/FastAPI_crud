from fastapi import FastAPI
from .database import engine, Base
from .controller import BlogController, UserController, Authentication

app = FastAPI()

Base.metadata.create_all(engine) # khai báo để sinh ra table trong db

# Gọi controller để view ra
app.include_router(Authentication.router)
app.include_router(BlogController.router)
app.include_router(UserController.router)

