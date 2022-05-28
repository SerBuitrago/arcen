from pydantic import BaseModel

class Audit(BaseModel):
    id:str
    service:str
    operation:str
    id_user:str
    ip_address:str
    response:str
    date:str