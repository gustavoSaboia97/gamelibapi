from flask import Flask

from src.game.routes.game_routes import game_blueprint


app = Flask(__name__)

app.register_blueprint(game_blueprint)
