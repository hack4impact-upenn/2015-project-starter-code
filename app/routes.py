from app import app, db
from flask import request, json, render_template
from models import Coordinates


@app.route('/', methods=['GET'])
def index():
    coors = Coordinates.query.all()
    return render_template('index.html', 
    	coordinates = json.dumps(
    		[coord.listCoordinates() for coord in coors]
    	))


@app.route('/health',methods=['GET'])
def health():
	return 'OK', 200

@app.route('/coordinates',methods=['POST'])
def coordinates():
	data = request.json
	coordinates = data['coordinates']
	for c in coordinates:
		singleCoordinate = Coordinates(c['latitude'],c['longitude'],c['notes'])
		db.session.add(singleCoordinate)
	db.session.commit()
	return 'Added', 200
