from src.game.configuration.MongoConfiguration import MongoConfiguration
from pymongo.database import Database


class TestMongoConfiguration:

    def setup(self):
        self.__mongo_configuration = MongoConfiguration()

    def test_should_return_an_database_type(self):
        database = self.__mongo_configuration.database
        assert type(database) is Database
