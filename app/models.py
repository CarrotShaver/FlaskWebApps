from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Creates an ID column as the primary key
    username = db.Column(db.String(32), unique=True) # Creates a username column of max character size 64, with unique names
    email = db.Column(db.String(64), unique=True) # Creates an email column of max character six 80, with unique names
    password_hash = db.Column(db.String(128)) # Creates a password_hash column to store our hashed passwords

    def __repr(self):
        return "<User {}>".format(self.username)