from app import app, db
from flask import render_template, request
from models import Coordinate


@app.route('/', methods=['GET'])
def index():
    name = 'Tinder for Treasure'
    coords = [Coordinate(-12, -77, "testing"), Coordinate(-12.01, -77.0001, "test2")]
    return render_template('home.html', name=name, coordinates=coords)


@app.route('/health', methods=['GET'])
def health():
    return 'Never been better!', 200


@app.route('/coordinates', methods=['POST'])
def coordinates():
    return '???', 200
