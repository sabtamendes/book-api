from dotenv import load_dotenv

load_dotenv()

import os

ENV = os.getenv("ENV")
IS_TEST_ENV = ENV and ENV in ("test") # test é o valor da variável de ambiente no .env
db_hostname = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USERNAME")

print(IS_TEST_ENV, ENV, db_hostname, db_port, db_password, db_name, db_user )