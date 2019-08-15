from flask import render_template, Blueprint
from flask_login import login_required, current_user

from . import whale

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
  name = current_user.name
  return render_template('profile.html', name=current_user.name)

@main.route('/whale')
def whale_page():
    game_id = whale.game.id
    room_id = whale.game.add_room()
    player_id = whale.game.add_player(room_id)
    return render_template("whale.html", game_id=game_id, room_id=room_id, player_id=player_id)
