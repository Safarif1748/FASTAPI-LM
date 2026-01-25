from pydantic import BaseModel, Field

class DepressionRequest(BaseModel):
    query: str
    type: str
    top_k: int
