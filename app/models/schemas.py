from pydantic import BaseModel

class ClientRequest(BaseModel):
    name: str
    service: str
    message: str 