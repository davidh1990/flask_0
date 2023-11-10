from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')

def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message":"pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre): #se utiliza la convencion snake case es con guion bajo
    return jsonify({"name" : nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):#se utiliza la convencion snake case es con guion bajo
    return jsonify({"id" : id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# GET de todos los 'recursos'
@app.route('/recurso', methods= ['GET'])
def get_recursos():
    return jsonify({"data":"lista de todos los items de este recurso"})

# POST de todos los 'recursos'
@app.route('/recurso', methods = ['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    #insertar en la BD
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})

@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #buscar en la BD un registro con ese id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})


if __name__== '__main__':
    app.run(debug=True, port=5000)