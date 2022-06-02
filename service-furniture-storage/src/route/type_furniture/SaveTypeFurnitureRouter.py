from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeFurnitureDto import TypeFurnitureDto
from src.model.response.TypeFurnitureResponse import TypeFurnitureResponse as ResponseArcen
from src.service.type_furniture.SaveTypeFurnitureService import SaveTypeFurnitureService as ServiceArcen
from src.persistence.database.table.TypeFurnitureTable import TypeFurnitureTable as TableArcen
from src.util.constant import COLUMN_TYPE_FURNITURE, ENDPOINT_APP, ENDPOINT_APP_TYPE_FURNITURE, ENDPOINT_GENERIC_SAVE
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE

router_save_type_furniture = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_FURNITURE+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status = RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_type_furniture.post(endpoint, response_model = response, status_code= status)
async def save(type_furniture: TypeFurnitureDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_FURNITURE: type_furniture})
    service = ServiceArcen(db)
    return service.execute(data)