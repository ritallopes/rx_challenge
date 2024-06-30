from datetime import datetime, timezone

from .database import SessionLocal
from .models import Equipment, EquipmentData, User


def seed_data():
    db = SessionLocal()

    # Criar usuários
    users = [
        User(
            name='Jane Doe', email='jane.doe@example.com', password='securepassword123'
        ),
    ]
    db.add_all(users)
    db.commit()

    # Criar equipmentos
    equipments = [
        Equipment(equipment_id='EQ-1001', name='Temperature Sensor'),
        Equipment(equipment_id='EQ-1002', name='Pressure Sensor'),
        Equipment(equipment_id='EQ-1003', name='Humidity Sensor'),
    ]
    db.add_all(equipments)
    db.commit()

    # Criar dados dos equipmentos
    equipment_data = [
        EquipmentData(
            equipment_id='EQ-1001',
            timestamp=datetime(2024, 6, 28, 14, 0, 0, tzinfo=timezone.utc),
            value=22.50,
        ),
        EquipmentData(
            equipment_id='EQ-1002',
            timestamp=datetime(2024, 6, 28, 15, 0, 0, tzinfo=timezone.utc),
            value=1012.30,
        ),
        EquipmentData(
            equipment_id='EQ-1003',
            timestamp=datetime(2024, 6, 28, 16, 0, 0, tzinfo=timezone.utc),
            value=45.75,
        ),
        EquipmentData(
            equipment_id='EQ-1001',
            timestamp=datetime(2024, 6, 28, 17, 0, 0, tzinfo=timezone.utc),
            value=23.10,
        ),
    ]
    db.add_all(equipment_data)
    db.commit()

    print('Data seeded successfully.')


if __name__ == '__main__':
    seed_data()
