"""
    @description - Dto ubicacion documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class DocumentLocationDto(BaseModel):
    name: str
    ib_object: str
    id_invoice: str