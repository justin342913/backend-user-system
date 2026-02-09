from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.users import router as users_router
from app.api import auth


app = FastAPI()

app.include_router(health_router)
app.include_router(users_router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Backend system running"}


from app.database import engine
from app.models import user

user.Base.metadata.create_all(bind=engine)
