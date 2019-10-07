class Development:
    #                         databasename://username:password@host:port/dbname
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sevani@127.0.0.1:5432/project'
    DEBUG = True
    SECRET_KEY = 'some secrets'

class Production:
    pass