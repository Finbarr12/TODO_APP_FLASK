# from _init_ import db


# class Todo(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     name= db.Column(db.String(255),nullable=False)
#     description=db.Column(db.String(255),nullable=False)
#     user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
#     iscompleted = db.Column(db.Boolean,default= False)


#     def __repr__(self):
#         return f'Todo ({self.name})'