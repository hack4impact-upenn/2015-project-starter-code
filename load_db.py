from app import db, models

db.create_all()  # initializes the tables
db.session.commit()

alex = models.User('aharelick', 'alexharelick@gmail.com')
not_alex = models.User('notalex', 'notalex@gmail.com')
db.session.add(alex)
db.session.add(not_alex)

post = models.Post(title='Sloths Rule', body='dat body', author=alex)
db.session.add(post)

db.session.commit()  # commit the transaction

####################

# Popular Queries

####################

# models.User.query.all()
# models.User.query.get(1)
# models.User.query.filter_by(username='aharelick')
