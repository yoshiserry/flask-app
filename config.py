import os

# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'l\xbb|N\xa3@j\xf6\x06\x10\x8fU\x86\xa1\xe5\xdf\x04\x15D?B\xe0KB' #os.urandom(24)
    #update from database name hardcoded to Database_URL environment variable.
    # Then update the environment variable in the virtualenv Flask Environment via terminal with export command.
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
