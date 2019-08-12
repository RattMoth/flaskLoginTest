from flask import render_template, Blueprint
from flask_login import login_required, current_user

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
def whale():
  return render_template('whale.html')