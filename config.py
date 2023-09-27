import os
from dotenv import load_dotenv

load_dotenv()

database_host = os.getenv('database_host')
database_port = os.getenv('database_port')
database_username = os.getenv('database_username')
database_password = os.getenv('database_password')
database_name = os.getenv('database_name')

minio_url = os.getenv('minio_url')
minio_access = os.getenv('minio_access')
minio_secret = os.getenv('minio_secret')