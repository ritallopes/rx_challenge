from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.api.db.database import Base


class EquipmentData(Base):
    __tablename__ = 'equipment_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(
        String, ForeignKey('equipment.equipment_id', ondelete='CASCADE'), nullable=False
    )
    timestamp = Column(DateTime, nullable=False)
    value = Column(Numeric(precision=5, scale=2), nullable=False)
    received_at = Column(DateTime, server_default=func.now(), nullable=False)

    equipment = relationship('Equipment', back_populates='data')

    def __repr__(self):
        return (
            f'<EquipmentData(equipment_id={self.equipment_id}, '
            f'timestamp={self.timestamp}, value={self.value}, '
            f'received_at={self.received_at})>'
        )
