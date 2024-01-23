from flask_sqlalchemy import SQLAlchemy #, relationship, ForeignKey

db = SQLAlchemy()


class Usuario(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(250), unique=False, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    subscription_date = db.Column(db.Integer, unique=False, nullable=True)
    favorito = db.relationship('Favorito') # agregar db.relationship
                                           # Favorito con mayuscula

def __repr__(self):                     
        return '<Usuario %r>' % self.email

    def serialize(self):
        return {
              "id": self.id,
              "name": self.name,
              "last_name": self.last_name,
              "email": self.email,
              "subscription_date": self.subscription_date
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    race = db.Column(db.String(250), unique=False, nullable=False)
    favorito = db.relationship("Favorito")

def __repr__(self):                     
        return '<Personaje %r>' % self.email

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name, 
            "race" : self.race
        }

class Planeta(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    favorito = relationship("favorito")

def __repr__(self):                    
        return '<Planeta %r>' % self.email

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class Favorito(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    id_usuario= db.Column(db.Integer, db.ForeignKey("usuario.id"))
    id_planeta= db.Column(db.Integer, db.ForeignKey("planeta.id"))
    id_personaje= db.Column(db.Integer, db.ForeignKey("personaje.id"))

    def __repr__(self):                    
        return '<Favorito %r>' % self.email

    def serialize(self):
        return {
            "id_planeta" : self.id_planeta,
            "id_personaje" : self.id_personaje
        }