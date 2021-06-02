from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.config.infra.database.sqlalchemy.connection import SessionLocal

from src.domain.accounts.models.user_models import UserModel, CreateUserModel
from src.domain.accounts.services.create_account_service import CreateAccountService
from src.domain.accounts.repositories.user_repository import UserRepository

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=UserModel)
def create_user(user: CreateUserModel, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = CreateAccountService(repository=repository)
    return service.create(user)
