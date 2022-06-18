"""
    @description - Entidad documento
    @version - 1.0.0
    @creation-date - 2022-06-14
    @author-creation - Sergio Stives Barrios Buitrago
    @modification-date - 2022-06-18
    @author-modification -  Sergio Stives Barrios Buitrago
"""
from pydantic import BaseModel

class Document(BaseModel):
    id:str
    id_document_location: str
    name: str
    document: str
    path_document: str
    date:str