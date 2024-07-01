from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.db.database import get_db
from app.api.db.models import User
from app.api.v1.schemas import UserPublic, UserSchema
from app.auth import read_current_user, read_hash_password

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', status_code=HTTPStatus.OK, response_model=list[UserPublic])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [UserSchema.from_orm(user) for user in users]


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='E-mail já registrado'
        )

    hash_pwd = read_hash_password(user.password)

    db_user = User(name=user.name, email=user.email, password=hash_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@router.put('/{email}', status_code=HTTPStatus.OK, response_model=UserPublic)
async def update_user(
    email: str,
    user_update: UserSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(read_current_user),
):
    if current_user.email != email:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Without permissions'
        )
    # db_user = db.query(User).filter(User.email == email).first()
    # if not db_user:
    #    raise HTTPException(
    #        status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
    #    )

    current_user.name = user_update.name
    current_user.email = user_update.email
    current_user.password = read_hash_password(user_update.password)
    db.commit()
    db.refresh(current_user)

    return UserPublic.from_orm(current_user)


@router.delete('/{email}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(
    email: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(read_current_user),
):
    if current_user.id != email:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Not enough permissions'
        )
    if not current_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    db.delete(current_user)
    db.commit()
