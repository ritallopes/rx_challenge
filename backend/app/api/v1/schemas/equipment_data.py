from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class EquipmentDataBase(BaseModel):
    equipment_id: str = Field(min_length=1, example='EQ-001')
    timestamp: datetime = Field(example='2024-06-28T14:00:00+00:00')
    value: float = Field(gt=0, example=22.50)

    class Config:
        from_attributes = True


class EquipmentDataCreate(EquipmentDataBase):
    pass


class EquipmentDataUpdate(BaseModel):
    timestamp: Optional[datetime]
    value: Optional[float]

    class Config:
        from_attributes = True


class EquipmentDataResponse(EquipmentDataBase):
    id: int
    received_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'id': 1,
                'equipment_id': 'EQ-001',
                'timestamp': '2024-06-28T14:00:00+00:00',
                'value': 22.50,
                'received_at': '2024-06-28T14:00:00+00:00',
            }
        }


class EquipmentDataIntervalResponse(EquipmentDataBase):
    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': [
                {
                    'timestamp': '2024-06-28T14:00:00+00:00',
                    'value': 22.50,
                    'received_at': '2024-06-28T14:00:00+00:00',
                }
            ]
        }


class EquipmentDataStatisticsResponse(BaseModel):
    sum_value: float
    average_value: float
    median_value: float

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {'sum_value': 300.0, 'average_value': 75.0, 'median_value': 78.0}
        }


class CSVUploadResponse(BaseModel):
    message: str
    invalid_rows: List[Dict[str, str]]
