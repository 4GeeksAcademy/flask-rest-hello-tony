"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Usuario, Personaje, Planeta, Favorito
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#GET PEOPLE

@app.route('/personaje', methods=['GET'])
def get_people():
    resultado = Personaje.query.all() #Traigo de la base de datos toda la info de la tabla Personaje
    if resultado == [] : 
        return jsonify({"msg": "No existen personajes" })
    body = list(map(lambda personaje : personaje.serialize(), resultado)) #mapea la info de los personaje y la serializa
    return jsonify(body), 200

@app.route('/personaje/<int:people_id>', methods=['GET', 'DELETE']) 
def get_one_person(people_id):
    resultado = Personaje.query.filter_by(id = people_id).first() #Traigo la informacion de la tabla segun el ID proporcionado, es decir la fila.
    if resultado is None : 
        return jsonify({"msg": "No existe el personaje" })
    if request.method == 'GET':
        return jsonify(resultado.serialize()), 200
    if request.method == 'DELETE':
        db.session.delete(resultado)
        db.session.commit()
        return jsonify({"msg": "El personaje fue eliminado" }), 404

@app.route('/personaje', methods=['POST'])
def add_people():
    body = json.loads(request.data)
    nuevo_personaje = Personaje(
        name = body["name"],
        race = body["race"]
    )
    db.session.add(nuevo_personaje)
    db.session.commit()
    return jsonify(nuevo_personaje.serialize()), 200


# #GET PLANETS

@app.route('/planeta', methods=['GET'])
def get_planets():
    resultado = Planeta.query.all() #Traigo de la base de datos toda la info de la tabla Personaje
    if resultado == [] : 
        return jsonify({"msg": "No existen planetas" })
    body = list(map(lambda planeta : planeta.serialize(), resultado)) #mapea la info de los personaje y la serializa
    return jsonify(body), 200

@app.route('/planeta', methods=['POST'])
def add_planets():
    body = json.loads(request.data)
    nuevo_planeta = Planeta(
        name = body["name"]
    )
    db.session.add(nuevo_planeta)
    db.session.commit()
    return jsonify(nuevo_planeta.serialize()), 200

@app.route('/planeta/<int:planet_id>', methods=['GET', 'DELETE']) #no se como hacer que aparezca solo ese id
def get_one_planet(planet_id):
    resultado = Planeta.query.filter_by(id = planet_id).first() #Traigo la informacion de la tabla segun el ID proporcionado, es decir la fila.
    if resultado is None : 
        return jsonify({"msg": "No existe el planeta" })
    # body = resultado.serialize() #como es un solo registro, solo especifico que me serialice ese
    if request.method == 'GET':
        return jsonify(resultado.serialize()), 200
    if request.method == 'DELETE':
        db.session.delete(resultado)
        db.session.commit()
        return jsonify({"msg": "El planeta fue eliminado" }), 404

# #GET USER

@app.route('/usuario', methods=['GET'])
def get_user():
    resultado = Usuario.query.all() 
    if resultado == [] : 
        return jsonify({"msg": "No existen usuarios" })
    body = list(map(lambda usuario : usuario.serialize(), resultado))
    return jsonify(body), 200

@app.route('/usuario/<int:user_id>', methods=['GET', 'DELETE']) 
def get_one_user(user_id):
    resultado = Usuario.query.filter_by(id = user_id).first()
    if resultado is None : 
        return jsonify({"msg": "No existe el usuario" })
    if request.method == 'GET':
        return jsonify(resultado.serialize()), 200
    if request.method == 'DELETE':
        db.session.delete(resultado)
        db.session.commit()
        return jsonify({"msg": "El usuario fue eliminado" }), 404

@app.route('/usuario', methods=['POST'])
def add_user():
    body = json.loads(request.data) #basicamente lo mismo que request.get_json()
    nuevo_usuario = Usuario(
        name = body["name"],
        last_name = body["last_name"],
        email = body["email"],
        password = body["password"],
        subscription_date = body["subscription_date"]
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.serialize()), 200

#GET FAVORITE

@app.route('/favorito', methods=['GET'])
def get_favorite():
    resultado = Favorito.query.all() 
    if resultado == [] : 
        return jsonify({"msg": "No existen favoritos" })
    body = list(map(lambda favorito : favorito.serialize(), resultado))
    return jsonify(body), 200

@app.route('/favorito', methods=['POST'])
def add_favorite():
    body = json.loads(request.data) #basicamente lo mismo que request.get_json()
    nuevo_favorito = Favorito(
        id_usuario = body["id_usuario"],
        id_planeta = body["id_planeta"],
        id_personaje = body["id_personaje"]
    )
    db.session.add(nuevo_favorito)
    db.session.commit()
    return jsonify(nuevo_favorito.serialize()), 200

@app.route('/usuario/favorito', methods=['GET'])
def get_favorites():
    body = json.loads(request.data)
    user_id = body["user_id"] #atrapamos el id del usuario
    resultado = Favorito.query.filter_by(id_usuario = user_id).all()
    if resultado == [] : 
        return jsonify({"msg": "No existen favoritos" })
    body = list(map(lambda favorito : favorito.serialize(), resultado))
    return jsonify(body), 200
    
#POSTS

# @app.route('/favorito/planeta/<int:planet_id>', methods=['POST'])
# def add_new_planet():
#     body = request.get_json()
#     new_planet.append(body)
#     return jsonify(new_planet), 200

# @app.route('/favorito/personaje/<int:people_id>', methods=['POST'])
# def add_new_people():
#     body = request.get_json()
#     new_people.append(body)
#     return jsonify(new_people), 200

#DELETES

# @app.route('/favorito/planeta/<int:planet_id>', methods=['DELETE'])
# def delete_planet(planet_id):
#     del new_planet[planet_id - 1]
#     return jsonify(new_planet), 200

# @app.route('/favorito/personaje/<int:people_id>', methods=['DELETE'])
# def delete_people(people_id):
#     del new_people[people_id - 1]
#     return jsonify(new_people), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
