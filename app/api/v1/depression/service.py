from .schema import DepressionRequest

def get_depression(data: DepressionRequest):
    return {
        "query": data.query,
        "type": data.type,
        "top_k": data.top_k,
        "message": "Assessment received"
    }
