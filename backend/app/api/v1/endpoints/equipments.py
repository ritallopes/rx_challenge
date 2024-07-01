from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.db.database import get_db
from app.api.db.models import Equipment, EquipmentData
from app.api.v1.schemas import (
    EquipmentCreate,
    EquipmentResponse,
    EquipmentUpdate,
    EquipmentWithDataResponse,
)

router = APIRouter(prefix='/equipments', tags=['equipments'])


@router.get('/', status_code=HTTPStatus.OK, response_model=list[EquipmentResponse])
async def read_equipments(db: Session = Depends(get_db)):
    equipments = db.query(Equipment).all()
    return equipments


@router.get(
    '/{equipment_id}',
    status_code=HTTPStatus.OK,
    response_model=EquipmentWithDataResponse,
)
async def read_equipment(equipment_id: str, db: Session = Depends(get_db)):
    equipment = (
        db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
    )
    print('QQQAQAQQQ ===========')
    print(equipment)
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


@router.post('/', status_code=HTTPStatus.CREATED, response_model=EquipmentResponse)
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


@router.put(
    '/{equipment_id}', status_code=HTTPStatus.OK, response_model=EquipmentResponse
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


@router.delete('/{equipment_id}', status_code=HTTPStatus.NO_CONTENT)
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
