from flask import Flask, render_template
from .blue.blueprint import stuff
from flask_sqlalchemy import SQLAlchemy


class config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///D:\\web projects\\web\\dbo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
app.register_blueprint(stuff, url_prefix="/stuff")

@app.route('/')
def page():
    return render_template('index.html',)


if __name__ == '__main__':
    app.run()
