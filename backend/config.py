REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

class Settings:

    REDIS_BROKER_URL = "redis://localhost:6379/0"

    REDIS_RESULT_BACKEND = "redis://localhost:6379/1"


settings = Settings()