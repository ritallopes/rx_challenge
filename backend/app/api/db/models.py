from app.api.db.database import Base
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


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    data = relationship('EquipmentData', back_populates='equipment')

    def __repr__(self):
        return f'<Equipment(equipment_id={self.equipment_id}, name={self.name})>'


class EquipmentData(Base):
    __tablename__ = 'equipment_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(String, ForeignKey('equipment.equipment_id'), nullable=False)
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


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'
