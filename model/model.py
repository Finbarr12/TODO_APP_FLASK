from _init_ import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False,unique=True)
    password = db.Column(db.String(2555),nullable=False)


    def __repr__(self):
        return f'User ({self.name}, {self.email})'