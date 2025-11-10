from typing import Dict, Any, List

def add_dueto(collections: Dict[str, Any], data):
    if len(data) != 2:
        raise ValueError("É necessário fornecer exatamente duas palavras para o dueto.")
    
    result = collections["dueto"].insert_one({"palavras": data})
    return {"message": "Dueto adicionado com sucesso", "_id": str(result.inserted_id)}

def get_duetos(collections: Dict[str, Any]) -> List[Dict[str, Any]]:
    duetos = list(collections["dueto"].find())
    for d in duetos:
        d["_id"] = str(d["_id"])
    return duetos
