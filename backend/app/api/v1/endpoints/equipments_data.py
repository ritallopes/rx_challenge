from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from app.api.db.database import get_db
from app.api.db.models import Equipment, EquipmentData
from app.api.v1.schemas import (
    EquipmentDataCreate,
    EquipmentDataIntervalResponse,
    EquipmentDataResponse,
    EquipmentDataStatisticsResponse,
    EquipmentDataUpdate,
)

router = APIRouter(prefix="/equipments_data", tags=["equipments_data"])


@router.get('/{equipment_id}', status_code=HTTPStatus.OK, response_model=list[EquipmentDataIntervalResponse])
async def read_equipment_timestamp(
    equipment_id: str,
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found')

    equipment_data = db.query(EquipmentData).filter(
        EquipmentData.equipment_id == equipment_id,
        EquipmentData.timestamp >= start_time,
        EquipmentData.timestamp <= end_time
    ).all()

    return [EquipmentDataIntervalResponse.from_orm(eq) for eq in equipment_data]


@router.get('/statistics/{equipment_id}', status_code=HTTPStatus.OK, response_model=EquipmentDataStatisticsResponse)
async def read_equipment_data_statistics(
    equipment_id: str,
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found')

    sum_value = db.query(func.sum(EquipmentData.value)).filter(
        EquipmentData.equipment_id == equipment_id,
        EquipmentData.timestamp >= start_time,
        EquipmentData.timestamp <= end_time
    ).scalar()

    average_value = db.query(func.avg(EquipmentData.value)).filter(
        EquipmentData.equipment_id == equipment_id,
        EquipmentData.timestamp >= start_time,
        EquipmentData.timestamp <= end_time
    ).scalar()

    subquery = db.query(EquipmentData.value).filter(
        EquipmentData.equipment_id == equipment_id,
        EquipmentData.timestamp >= start_time,
        EquipmentData.timestamp <= end_time
    ).subquery()

    median_value = db.query(func.percentile_cont(0.5).within_group(subquery.c.value)).scalar()

    if sum_value is None:
        sum_value = 0.0

    if average_value is None:
        average_value = 0.0

    if median_value is None:
        median_value = 0.0

    return EquipmentDataStatisticsResponse(
        sum_value=sum_value, average_value=average_value, median_value=median_value
    )


@router.post('/', status_code=HTTPStatus.CREATED, response_model=EquipmentDataResponse)
async def create_equipment_data(data: EquipmentDataCreate, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.equipment_id == data.equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Equipment not found')

    db_equipment_data = EquipmentData(
        equipment_id=data.equipment_id, timestamp=data.timestamp, value=data.value
    )
    db.add(db_equipment_data)
    db.commit()
    db.refresh(db_equipment_data)

    return db_equipment_data


@router.put('/{id}', status_code=HTTPStatus.OK, response_model=EquipmentDataResponse)
async def update_equipment_data(id: int, data_update: EquipmentDataUpdate, db: Session = Depends(get_db)):
    db_equipment_data = db.query(EquipmentData).filter(EquipmentData.id == id).first()
    if not db_equipment_data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Equipment data not found')

    db_equipment_data.timestamp = data_update.timestamp
    db_equipment_data.value = data_update.value
    db.commit()
    db.refresh(db_equipment_data)

    return db_equipment_data


@router.delete('/{id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_equipment_data(id: int, db: Session = Depends(get_db)):
    db_equipment_data = db.query(EquipmentData).filter(EquipmentData.id == id).first()
    if not db_equipment_data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Equipment data not found')

    db.delete(db_equipment_data)
    db.commit()
