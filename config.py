import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = "mongodb://mongo:27017/customer_app_db"
    SECRET_KEY = "your_secret_key"

