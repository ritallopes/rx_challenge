import os

import dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()
PGPASSWORD = os.getenv('PGPASSWORD')
if not PGPASSWORD:
    raise ValueError(
        'Uma ou mais variáveis de ambiente necessárias não estão definidas.'
    )

DATABASE_URL = f'postgresql://neondb_owner:{PGPASSWORD}@ep-lively-surf-a57l4i04.us-east-2.aws.neon.tech/neondb?sslmode=require'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
