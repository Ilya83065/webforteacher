from flask import Blueprint
from flask import render_template
from models import mod

stuff = Blueprint('stuff', __name__, template_folder='templates')

@stuff.route('/')
def index():
    stf = mod.query.all()
    return render_template('blue/index.html', stf=stf)