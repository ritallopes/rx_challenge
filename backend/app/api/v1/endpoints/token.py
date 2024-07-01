from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.db.database import get_db
from app.api.db.models import User
from app.api.v1.schemas import Token, UserPublic, UserSchema
from app.auth import create_token_access, read_hash_password, verify_pwd

router = APIRouter(prefix='/token', tags=['token'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=Token,
)
async def login_access_tooken(
    form: OAuth2PasswordRequestForm = Depends(),
    response_model=Token,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form.username).first()
    if user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='E-mail não encontrado'
        )

    if not verify_pwd(form.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='E-mail ou senha incorreta'
        )

    access_token = create_token_access(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.put('/{email}', status_code=HTTPStatus.OK, response_model=UserPublic)
async def update_user(
    email: str, user_update: UserSchema, db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    db_user.name = user_update.name
    db_user.email = user_update.email
    db_user.password = read_hash_password(user_update.password)
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@router.delete('/{email}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    db.delete(db_user)
    db.commit()
