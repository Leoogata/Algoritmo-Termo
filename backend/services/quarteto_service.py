from typing import Dict, Any, List

class ServiceError(Exception):
    pass

def add_quarteto(collections: Dict[str, Any], data):
    if len(data) != 4:
        raise ServiceError("É necessário fornecer exatamente quatro palavras para o quarteto.")
    result = collections["quarteto"].insert_one({"palavras": data})
    return {"message": "Quarteto adicionado com sucesso", "_id": str(result.inserted_id)}

def get_quartetos(collections: Dict[str, Any]) -> List[Dict[str, Any]]:
    quartetos = list(collections["quarteto"].find())
    for q in quartetos:
        q["_id"] = str(q["_id"])
    return quartetos
