from app import app, db
from flask import render_template, request, json
from models import Coordinate


@app.route('/', methods=['GET'])
def index():
    name = 'Tinder for Treasure'
    coordinates = Coordinate.query.all()
    return render_template('home.html', name=name,
                           coordinates=json.dumps(
                               [c.serialize() for c in coordinates]
                           ))


@app.route('/health', methods=['GET'])
def health():
    return 'Never been better!', 200


@app.route('/coordinates', methods=['POST'])
def coordinates():
    data = request.json
    print data['coordinates']
    coordinates = data['coordinates']
    for coord in coordinates:
        newCoord = Coordinate(coord['latitude'], coord['longitude'],
                              coord['notes'])
        db.session.add(newCoord)

    db.session.commit()
    return 'Yum!', 200
