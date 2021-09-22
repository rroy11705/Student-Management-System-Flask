from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


DEBUG = True
try:
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('username', 'password'))
    DATABASE = client['Student-Management-System']                            # DB_NAME

except ConnectionFailure as e:
    print("Connection Error:", e)

