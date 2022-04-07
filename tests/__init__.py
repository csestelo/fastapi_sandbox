from config import settings

# disable echo for running tests
settings.DB_ECHO = False

# use a different schema to run tests
settings.DB_DATABASE = "template1"
