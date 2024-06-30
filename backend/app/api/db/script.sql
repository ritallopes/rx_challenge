/*this file contains some used sql commands*/
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE equipment_data (
    id SERIAL PRIMARY KEY,
    equipment_id VARCHAR(255) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    value NUMERIC(5, 2) NOT NULL,
    received_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id) ON DELETE CASCADE
);
ALTER TABLE equipment_data
ALTER COLUMN received_at SET DEFAULT CURRENT_TIMESTAMP;


/*Seed*/
INSERT INTO users (name, email, password) VALUES
('Jane Doe', 'jane.doe@gmail.com', 'password123');
INSERT INTO equipment (equipment_id, name) VALUES
('EQ-001', 'Temperature Sensor'),
('EQ-002', 'Pressure Sensor'),
('EQ-003', 'Humidity Sensor');*/

INSERT INTO equipment_data (equipment_id, timestamp, value) VALUES
('EQ-001', '2024-06-28T14:00:00+00:00', 22.50),
('EQ-001', '2024-06-28T17:00:00+00:00', 23.10),
('EQ-002', '2024-06-28T15:00:00+00:00', 78.30),
('EQ-003', '2024-06-28T16:00:00+00:00', 45.75);


INSERT INTO equipment_data (equipment_id, timestamp, value)
VALUES ('EQ-003', '2024-06-28T18:00:00+00:00', 34.56);
SELECT * FROM equipment_data WHERE equipment_id = 'EQ-003' AND timestamp = '2024-06-28T18:00:00+00:00';

SELECT * FROM users
SELECT * FROM equipments
SELECT * FROM equipment_data
