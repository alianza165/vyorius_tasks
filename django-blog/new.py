import os

db_user = os.getenv('DB_USER')
db_password = os.environ.get('DB_PASS')

print(os.environ)
print(db_password)