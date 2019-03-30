class Game:

    def __init__(self, game_dict: dict):
        self.__name = game_dict["name"]
        self.__category = game_dict["category"]
        self.__year = game_dict["year"]

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def year(self):
        return self.__year

    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "category": self.__category,
            "year": self.__year
        }
