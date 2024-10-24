from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
BOOTSTRAP_SERVER = config("BOOTSTRAP_SERVER", cast=str)
KAFKA_NOTIFICATION_TOPIC = config("KAFKA_NOTIFICATION_TOPIC", cast=str)
KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT = config("KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT", cast=str)

# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)


ADMIN_USERNAME= config("ADMIN_USERNAME", cast=Secret)
ADMIN_EMAIL= config("ADMIN_EMAIL", cast=Secret)
ADMIN_PASSWORD= config("ADMIN_PASSWORD")