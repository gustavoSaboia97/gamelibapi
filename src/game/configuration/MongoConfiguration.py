from pymongo import MongoClient

import os

from pymongo.database import Database


class MongoConfiguration:

    def __init__(self):
        self.__database_uri = os.environ.get("DATABASE_URI")
        self.__mongo_client = MongoClient(self.__database_uri)
        self.__database = self.__mongo_client.game_database

    @property
    def database(self) -> Database:
        return self.__database
