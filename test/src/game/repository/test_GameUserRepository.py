from src.game.repository.GameUserRepository import GameUserRepository, MongoConfiguration
from src.game.models.models import GameUser
import pytest
from pytest_mock import mocker


class TestGameUserRepository:

    @pytest.fixture(autouse=True)
    def mock_dependencies(self, mocker):
        mocker.patch.object(MongoConfiguration, "database")

    def setup(self):
        self.__repository = GameUserRepository()

    def test_should_add_new_user_on_collection(self):
        game_user = GameUser("5c82e3f3258bc5091f406307", "login", list())
        self.__repository.add_game_user(game_user)
        MongoConfiguration.database.game_user_collection.insert_one.assert_called_with(game_user.to_mongo_dict())

