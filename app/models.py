from . import db


class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    notes = db.Column(db.String(120))

    def __init__(self, latitude, longitude, notes):
        self.latitude = latitude
        self.longitude = longitude
        self.notes = notes

    def __repr__(self):
        return '<Coordinate (%r, %r)>' % (self.latitude, self.longitude)
