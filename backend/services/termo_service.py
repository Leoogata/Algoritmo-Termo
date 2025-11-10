from typing import Dict, Any, List

def add_termo(collections: Dict[str, str], data: Dict[str, str]) -> Dict[str, Any]:
    if "palavra" not in data:
        raise ValueError("Campo 'palavra' é obrigatório.")

    result = collections["termo"].insert_one(data)
    return {
        "message": "Palavra adicionada com sucesso",
        "_id": str(result.inserted_id)
    }

def get_termos(collections: Dict[str, str]) -> List[Dict[str, str]]:
    termos = list(collections["termo"].find())
    for termo in termos:
        termo["_id"] = str(termo["_id"])
    return termos
