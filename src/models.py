from flask_sqlalchemy import SQLAlchemy, relationship, ForeignKey

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    subscription_date = db.Column(db.Integer, unique=False, nullable=True)
    favorito = relationship('Favorito')

class Personaje(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    race = db.Column(db.String(250), unique=False, nullable=False)
    favorito = relationship("favorito")

class Planeta(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    favorito = relationship("favorito")

class Favorito(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    id_usuario= db.Column(db.Integer, ForeignKey("usuario.id"))
    id_planeta= db.Column(db.Integer, ForeignKey("planeta.id"))
    id_personaje= db.Column(db.Integer, ForeignKey("personaje.id"))
