

from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.db.database import get_db
from app.api.db.models import User
from app.api.v1.schemas import UserPublic, UserSchema

router = APIRouter(prefix="/users", tags=["users"])


@router.get('/', status_code=HTTPStatus.OK, response_model=list[UserPublic])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [UserSchema.from_orm(user) for user in users]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='E-mail já registrado')

    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@router.put('/{email}',
status_code=HTTPStatus.OK, response_model=UserPublic)
async def update_user(email: str, user_update: UserSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(
          status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    db_user.name = user_update.name
    db_user.email = user_update.email
    db_user.password = user_update.password
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@router.delete('/{email}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(
          status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    db.delete(db_user)
    db.commit()
