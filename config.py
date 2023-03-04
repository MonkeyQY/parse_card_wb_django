import os

from dotenv import load_dotenv

load_dotenv()


database_name = os.getenv('DATABASE_NAME', 'djangotestdb')
database_user = os.getenv('DATABASE_USER', 'postgres')
database_password = os.getenv('DATABASE_PASSWORD', 'postgres')
database_host = os.getenv('DATABASE_HOST', 'localhost')
database_port = os.getenv('DATABASE_PORT', '5432')


django_secret_key = os.getenv('DJANGO_SECRET_KEY')