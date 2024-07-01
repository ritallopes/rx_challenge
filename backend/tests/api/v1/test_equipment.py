from datetime import datetime
from http import HTTPStatus


def test_read_equipment(client):
    equipment_id = 'EQ-001'
    response = client.get(f'/equipments/{equipment_id}')
    assert response.status_code == HTTPStatus.OK


def test_read_equipment_timestamp(client):
    equipment_id = 'EQ-001'
    start_time = datetime(2024, 1, 1, 0, 0, 0).isoformat()
    end_time = datetime(2024, 1, 31, 23, 59, 59).isoformat()
    response = client.get(
        f'/equipments_data/{equipment_id}?start_time={start_time}&end_time={end_time}'
    )
    assert response.status_code == HTTPStatus.OK
