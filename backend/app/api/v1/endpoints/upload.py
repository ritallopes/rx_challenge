from http import HTTPStatus

import pandas as pd
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.api.db.database import get_db
from app.api.db.models import Equipment, EquipmentData

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post('/', status_code=HTTPStatus.CREATED)
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Error reading CSV file')

    required_columns = ['equipmentId', 'timestamp', 'value']
    if not all(column in df.columns for column in required_columns):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='CSV file must contain equipmentId, timestamp, and value columns')

    invalid_rows = []
    for index, row in df.iterrows():
        equipment_id = row['equipmentId']
        timestamp = row['timestamp']
        value = row['value']

        try:
            timestamp = pd.to_datetime(timestamp)
        except Exception:
            invalid_rows.append(index)
            continue

        equipment = db.query(Equipment).filter(Equipment.equipment_id == equipment_id).first()
        if not equipment:
            new_equipment = Equipment(equipment_id=equipment_id, name=equipment_id)
            db.add(new_equipment)
            db.commit()

        equipment_data = EquipmentData(
            equipment_id=equipment_id,
            timestamp=timestamp,
            value=value
        )
        db.add(equipment_data)

    db.commit()
    return CSVUploadResponse(message='CSV upload completed', invalid_rows=invalid_rows)
