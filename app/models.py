from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin
from datetime import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # Creates an ID column as the primary key
    username = db.Column(db.String(32), unique=True) # Creates a username column of max character size 64, with unique names
    email = db.Column(db.String(64), unique=True) # Creates an email column of max character six 80, with unique names
    password_hash = db.Column(db.String(128)) # Creates a password_hash column to store our hashed passwords

    def __repr(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     def __repr__(self):
#         return "<Post {}>".format(self.body)