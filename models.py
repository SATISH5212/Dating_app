from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    hobbies = db.Column(db.ARRAY(db.String(100)))
