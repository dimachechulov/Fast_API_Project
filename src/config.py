from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.environ.get('DB_HOST')
DB_NAME=os.environ.get('DB_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASS=os.environ.get('DB_PASS')
DB_PORT=os.environ.get('DB_PORT')
JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')


EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT=os.environ.get('EMAIL_PORT')
