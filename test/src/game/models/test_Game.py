from src.game.models.model.Game import Game


class TestGame:

    def setup(self):
        self.__game = Game({"name": "name", "category": "category", "year": "year"})

    def test_should_set_correct_data(self):
        assert self.__game.name == "name"
        assert self.__game.category == "category"
        assert self.__game.year == "year"
