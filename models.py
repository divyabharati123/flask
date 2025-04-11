from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Employee (db.model):
    id=db.column(db.integer,primary_kry=True)
    name=db.column(db.string(30),nullable=False)
    age=db.column(db.integer,nullable=False)
# WE ARE DEFINNING THE TABLE