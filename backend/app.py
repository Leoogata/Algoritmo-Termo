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

# Rota health check
@app.route('/', methods=['GET'])
def health_check():
    return 'API do brabo ta on', 200

# Rota para adicionar palavra do termo
@app.route('/termo', methods=['POST'])
def create_termo():
    data = request.json

    if "palavra" not in data:
        abort(400, description="Campo 'palavra' é obrigatório.")

    result = collections["termo"].insert_one(data)
    return jsonify({
        "message": "Palavra adiciona com suceso",
        "_id": str(result.inserted_id)
        }), 201

# Rota para obter todas palavras do termo
@app.route('/termo', methods=['GET'])
def get_termos():
    termos = list(collections["termo"].find())
    for termo in termos:
        termo["_id"] = str(termo["_id"])
    return jsonify(termos), 200

# Rota para adicionar palavras do dueto
@app.route('/dueto', methods=['POST'])
def create_dueto():
    data = request.json

    if len(data) != 2:
        abort(400, description="É necessário fornecer exatamente duas palavras para o dueto.") 

    result = collections["dueto"].insert_one(data)
    return jsonify({
        "message": "Dueto adicionado com sucesso",
        "_id": str(result.inserted_id)
        }), 201

# Rota para obter todas palavras do dueto
@app.route('/dueto', methods=['GET'])
def get_duetos():
    duetos = list(collections["dueto"].find())
    for dueto in duetos:
        dueto["_id"] = str(dueto["_id"])
    return jsonify(duetos), 200

# Rota para adicionar palavras do quarteto
@app.route('/quarteto', methods=['POST'])
def create_quarteto():
    data = request.json

    if len(data) != 4:
        abort(400, description="É necessário fornecer exatamente quatro palavras para o quarteto.") 

    result = collections["quarteto"].insert_one(data)
    return jsonify({
        "message": "Quarteto adicionado com sucesso",
        "_id": str(result.inserted_id)
        }), 201

# Rota para obter todas palavras do quarteto
@app.route('/quarteto', methods=['GET'])
def get_quartetos():   
    quartetos = list(collections["quarteto"].find())
    for quarteto in quartetos:
        quarteto["_id"] = str(quarteto["_id"])
    return jsonify(quartetos), 200