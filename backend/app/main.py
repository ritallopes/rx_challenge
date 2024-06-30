from datetime import datetime
from http import HTTPStatus

import pandas as pd
from fastapi import Depends, FastAPI, File, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.db.database import SessionLocal
from app.api.db.models import Equipment, EquipmentData, User
from app.api.v1.schemas import (
    EquipmentCreate,
    EquipmentDataBase,
    EquipmentDataCreate,
    EquipmentDataIntervalResponse,
    EquipmentDataResponse,
    EquipmentDataStatisticsResponse,
    EquipmentDataUpdate,
    EquipmentResponse,
    EquipmentUpdate,
    EquipmentWithDataResponse,
    UserPublic,
    UserSchema,
)

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app = FastAPI()


def get_db():
    databse = SessionLocal()
    try:
        yield databse
    finally:
        databse.close()


@app.get('/', status_code=HTTPStatus.OK)
async def main():
    return {'message': 'Bem-vindo!'}


@app.get('/users/', status_code=HTTPStatus.OK, response_model=list[UserPublic])
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [UserSchema.from_orm(user) for user in users]


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='E-mail já registrado'
        )

    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@app.put('/users/{email}', status_code=HTTPStatus.OK, response_model=UserPublic)
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
    db_user.password = user_update.password
    db.commit()
    db.refresh(db_user)

    return UserPublic.from_orm(db_user)


@app.delete('/users/{email}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )

    db.delete(db_user)
    db.commit()


@app.get(
    '/equipments/', status_code=HTTPStatus.OK, response_model=list[EquipmentResponse]
)
async def read_equipments(db: Session = Depends(get_db)):
    equipments = db.query(Equipment).all()
    return equipments


@app.get(
    '/equipments/{equipment_id}',
    status_code=HTTPStatus.OK,
    response_model=EquipmentWithDataResponse,
)
async def read_equipment(equipment_id: str, db: Session = Depends(get_db)):
    equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    if not equipment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found'
        )
    equipment_data = (
        db.query(EquipmentData).filter(EquipmentData.equipment_id == equipment_id).all()
    )
    return EquipmentWithDataResponse(
        id=equipment.id,
        equipment_id=equipment.equipment_id,
        name=equipment.name,
        equipment_data=equipment_data,
    )


@app.post(
    '/equipments/', status_code=HTTPStatus.CREATED, response_model=EquipmentResponse
)
async def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    existing_equipment = (
        db.query(Equipment)
        .filter(Equipment.equipment_id == equipment.equipment_id)
        .first()
    )
    if existing_equipment:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail='Equipamento já registrado'
        )

    db_equipment = Equipment(equipment_id=equipment.equipment_id, name=equipment.name)
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


@app.put(
    '/equipments/{equipment_id}',
    status_code=HTTPStatus.OK,
    response_model=EquipmentResponse,
)
async def update_equipment(
    equipment_id: str, equipment_update: EquipmentUpdate, db: Session = Depends(get_db)
):
    db_equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    if not db_equipment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Equipamento não encontrado'
        )

    db_equipment.name = equipment_update.name
    db.commit()
    db.refresh(db_equipment)

    return db_equipment


@app.delete('/equipments/{equipment_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_equipment(equipment_id: str, db: Session = Depends(get_db)):
    db_equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    if not db_equipment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Equipamento não encontrado'
        )

    db.delete(db_equipment)
    db.commit()


@app.get(
    '/equipments_data/{equipment_id}',
    status_code=HTTPStatus.OK,
    response_model=list[EquipmentDataIntervalResponse],
)
async def read_equipment_timestamp(
    equipment_id: str,
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    db: Session = Depends(get_db),
):
    equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    if not equipment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found'
        )

    equipment_data = (
        db.query(EquipmentData)
        .filter(
            EquipmentData.equipment_id == equipment_id,
            EquipmentData.timestamp >= start_time,
            EquipmentData.timestamp <= end_time,
        )
        .all()
    )

    return [EquipmentDataIntervalResponse.from_orm(eq) for eq in equipment_data]


@app.get(
    '/equipments_data_statistics/{equipment_id}',
    status_code=HTTPStatus.OK,
    response_model=EquipmentDataStatisticsResponse,
)
async def read_equipment_data_statistics(
    equipment_id: str,
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    db: Session = Depends(get_db),
):
    equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    if not equipment:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found'
        )

    sum_value = (
        db.query(func.sum(EquipmentData.value))
        .filter(
            EquipmentData.equipment_id == equipment_id,
            EquipmentData.timestamp >= start_time,
            EquipmentData.timestamp <= end_time,
        )
        .scalar()
    )

    average_value = (
        db.query(func.avg(EquipmentData.value))
        .filter(
            EquipmentData.equipment_id == equipment_id,
            EquipmentData.timestamp >= start_time,
            EquipmentData.timestamp <= end_time,
        )
        .scalar()
    )

    subquery = (
        db.query(EquipmentData.value)
        .filter(
            EquipmentData.equipment_id == equipment_id,
            EquipmentData.timestamp >= start_time,
            EquipmentData.timestamp <= end_time,
        )
        .subquery()
    )
    median_value = db.query(
        func.percentile_cont(0.5).within_group(subquery.c.value)
    ).scalar()

    if sum_value is None:
        sum_value = 0.0

    if average_value is None:
        average_value = 0.0

    if median_value is None:
        median_value = 0.0

    return EquipmentDataStatisticsResponse(
        sum_value=sum_value, average_value=average_value, median_value=median_value
    )


@app.post(
    '/equipments_data/',
    status_code=HTTPStatus.CREATED,
    response_model=EquipmentDataResponse,
)
async def create_equipment_data(
    equipment_data: EquipmentDataCreate, db: Session = Depends(get_db)
):
    existing_equipment = (
        db.query(Equipment)
        .filter(Equipment.equipment_id == equipment_data.equipment_id)
        .first()
    )
    if not existing_equipment:
        db_equipment = Equipment(
            equipment_id=equipment_data.equipment_id, name=equipment_data.equipment_id
        )
        db.add(db_equipment)
        db.commit()
        db.refresh(db_equipment)

    db_equipment_data = EquipmentData(
        equipment_id=equipment_data.equipment_id,
        timestamp=equipment_data.timestamp,
        value=equipment_data.value,
    )
    db.add(db_equipment_data)
    db.commit()
    db.refresh(db_equipment_data)

    return db_equipment_data


@app.put(
    '/equipments_data/{data_id}',
    status_code=HTTPStatus.OK,
    response_model=EquipmentDataResponse,
)
async def update_equipment_data(
    data_id: int,
    equipment_data_update: EquipmentDataUpdate,
    db: Session = Depends(get_db),
):
    db_equipment_data = (
        db.query(EquipmentData).filter(EquipmentData.id == data_id).first()
    )
    if not db_equipment_data:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Dados do equipamento não encontrados',
        )

    if equipment_data_update.timestamp is not None:
        db_equipment_data.timestamp = equipment_data_update.timestamp
    if equipment_data_update.value is not None:
        db_equipment_data.value = equipment_data_update.value

    db.commit()
    db.refresh(db_equipment_data)

    return db_equipment_data


@app.delete('/equipments_data/{data_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_equipment_data(data_id: int, db: Session = Depends(get_db)):
    db_equipment_data = (
        db.query(EquipmentData).filter(EquipmentData.id == data_id).first()
    )
    if not db_equipment_data:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Dados do equipamento não encontrados',
        )

    db.delete(db_equipment_data)
    db.commit()


@app.post('/upload_csv/')
async def upload_csv(
    file: UploadFile = File(...),
    delimiter: str = Query(',', regex='[,;]'),
    db: Session = Depends(get_db),
):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail='O arquivo deve ser um CSV.')

    try:
        df = pd.read_csv(file.file, delimiter=delimiter)
        if not set(['equipmentId', 'timestamp', 'value']).issubset(
            df.columns
        ) and not set(['equipment_id', 'timestamp', 'value']).issubset(df.columns):
            raise HTTPException(
                status_code=400,
                detail='O CSV deve conter as colunas: equipmentId, timestamp e value.',
            )

        if 'equipmentId' in df.columns:
            df = df.rename(columns={'equipmentId': 'equipment_id'})

        valid_data = []
        for index, row in df.iterrows():
            try:
                timestamp = pd.to_datetime(row['timestamp'])
                value = float(row['value'])

                equipment_id_row = row['equipment_id']
                result = (
                    db.query(Equipment)
                    .filter(Equipment.equipment_id == equipment_id_row)
                    .first()
                )
                if not result:
                    new_equipment = Equipment(
                        equipment_id=equipment_id_row, name=equipment_id_row
                    )
                    db.add(new_equipment)
                    await db.commit()

                equipment_data = EquipmentData(
                    equipment_id=equipment_id_row, timestamp=timestamp, value=value
                )
                db.add(equipment_data)
                valid_data.append(equipment_data)

            except (ValueError, TypeError) as e:
                print(f'Linha inválida: {row} - Erro: {e}')
                continue

        db.commit()

        response_data = [
            EquipmentDataBase(
                equipment_id=edata.equipment_id,
                timestamp=edata.timestamp,
                value=edata.value,
            )
            for edata in valid_data
        ]

        return response_data

    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
