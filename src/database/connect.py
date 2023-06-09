from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')
port = config.get('DB', 'PORT')

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{domain}:{port}/{db_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# if __name__ == '__main__':
#     print(get_db())
