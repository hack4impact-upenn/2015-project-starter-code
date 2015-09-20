from app import db, models

db.drop_all()  # drop all tables
db.session.commit()
