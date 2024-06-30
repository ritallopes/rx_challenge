from typing import List

from pydantic import BaseModel, Field

from .equipment_data import EquipmentDataResponse


class EquipmentBase(BaseModel):
    equipment_id: str = Field(min_length=1, example='EQ-001')
    name: str = Field(min_length=1, example='Temperature Sensor')


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(BaseModel):
    name: str = Field(..., example='Novo Nome do Equipamento')

    class Config:
        from_attributes = True


class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {'id': 1, 'equipment_id': 'EQ-001', 'name': 'Temperature Sensor'}
        }


class EquipmentWithDataResponse(EquipmentResponse):
    equipment_data: List[EquipmentDataResponse] = []

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'id': 1,
                'equipment_id': 'EQ-001',
                'name': 'Temperature Sensor',
                'equipment_data': [
                    {
                        'timestamp': '2024-06-28T14:00:00+00:00',
                        'value': 22.50,
                        'received_at': '2024-06-28T14:00:00+00:00',
                    }
                ],
            }
        }
