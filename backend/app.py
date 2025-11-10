from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Inicializar a aplicação Flask
app = Flask(__name__)

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "termo_db")

# Conectar ao MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Coleções de documentos
collections = {
    "termo": db["termo"],
    "dueto": db["dueto"],
    "quarteto": db["quarteto"],
}

@app.route('/', methods=['GET'])
def health_check():
    return 'API do brabo ta on', 200

@app.route('/termo', methods=['POST'])
def create_termo():
    data = request.json
    try:
        response = add_termo(collections, data)
        return jsonify(response), 201
    except TermoError as e:
        abort(400, description=str(e))

@app.route('/termo', methods=['GET'])
def list_termos():
    return jsonify(get_termos(collections)), 200

@app.route('/dueto', methods=['POST'])
def create_dueto():
    data = request.json
    try:
        response = add_dueto(collections, data)
        return jsonify(response), 201
    except DuetoError as e:
        abort(400, description=str(e))

@app.route('/dueto', methods=['GET'])
def list_duetos():
    return jsonify(get_duetos(collections)), 200

@app.route('/quarteto', methods=['POST'])
def create_quarteto():
    data = request.json
    try:
        response = add_quarteto(collections, data)
        return jsonify(response), 201
    except QuartetoError as e:
        abort(400, description=str(e))

@app.route('/quarteto', methods=['GET'])
def list_quartetos():
    return jsonify(get_quartetos(collections)), 200

if __name__ == "__main__":
    app.run(debug=True)