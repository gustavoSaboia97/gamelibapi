from flask import Blueprint


game_blueprint = Blueprint("game_blueprint", __name__)


@game_blueprint.route("/api/game/", methods=['POST', ])
def new_game():
    return "New Game Route"


@game_blueprint.route("/api/game/", methods=['GET', ])
def get_games():
    return "All user games"


@game_blueprint.route("/api/game/<string:game_id>/", methods=['PUT', ])
def update_game(game_id: str):
    return f"UPDATE game {game_id}"


@game_blueprint.route("/api/game/<string:game_id>/", methods=['DELETE', ])
def delete_game(game_id: str):
    return f"DELETE game {game_id}"
