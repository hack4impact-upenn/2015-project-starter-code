import os.path
import jinja2
from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy

initDB = not os.path.exists('app/coors.db')
app = Flask(__name__)

app.config.from_object(app.config.from_object(config['development']))
db = SQLAlchemy(app)

from app import routes, models

if initDB:
	db.create_all()
	db.session.commit()
	print "Made a Database Instance for you :)"
else:
	#use db from last session
	print "using db from last session"