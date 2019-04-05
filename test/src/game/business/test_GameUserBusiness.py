from src.game.business.GameUserBusiness import GameUserBusiness
from src.game.business.GameUserBusiness import GameUserRepository
from src.game.models.models import GameUser
from pytest_mock import mocker
import pytest


class TestGameUserBusiness:

    @pytest.fixture(autouse=True)
    def mock_dependencies(self, mocker):
        mocker.patch.object(GameUserRepository, "add_game_user")

    def setup(self):
        self.__game_user_business = GameUserBusiness()

    def test_should_add_new_game_user(self):
        game_user = GameUser("user_id", "login", list())
        self.__game_user_business.add_game_user(game_user)
        GameUserRepository.add_game_user.assert_called_with(game_user)

