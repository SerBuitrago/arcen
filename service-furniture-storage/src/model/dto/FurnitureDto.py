from pydantic import BaseModel

class FurnitureDto(BaseModel):
    id_block: int
    id_type_furniture: int
    number_furniture: int