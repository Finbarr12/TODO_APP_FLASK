from _init_ import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False,unique=True)
    password = db.Column(db.String(2555),nullable=False)
    todo = db.relationship('Todo', backref = 'user', lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(255),nullable=False)
    description=db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    iscompleted = db.Column(db.Boolean,default= False)
    

    def __repr__(self):
        return f'User ({self.name}, {self.email})'