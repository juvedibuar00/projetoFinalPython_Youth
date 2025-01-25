# app/config.py
class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@localhost/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "your_jwt_secret_key"
