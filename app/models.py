from . import db
import json

class Coordinates(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	latitude = db.Column(db.Float())
	longitude = db.Column(db.Float())
	notes = db.Column(db.String(1000))

	def __init__ (self, lat, long, note): 
		self.latitude = lat
		self.longitude = long
		self.notes = note

	def __repr__(self):
		return '<Coordinates (%r, %r)>' % (self.latitude, self.longitude)

	def listCoordinates(self):
		return {
			'latitude' : self.latitude,
			'longitude' : self.longitude,
			'notes' : self.notes
		}