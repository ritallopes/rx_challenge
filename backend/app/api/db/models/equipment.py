from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.api.db.database import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)

    data = relationship('EquipmentData', back_populates='equipment')

    def __repr__(self):
        return f'<Equipment(equipment_id={self.equipment_id}, name={self.name})>'
