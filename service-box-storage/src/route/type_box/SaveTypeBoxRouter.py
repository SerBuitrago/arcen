from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TypeBoxDto import TypeBoxfDto
from src.model.response.TypeBoxResponse import TypeBoxResponse as ResponseArcen
from src.service.type_box.SaveTypeBoxService import SaveTypeBoxService as ServiceArcen
from src.persistence.database.table.TypeBoxTable import TypeBoxTable as TableArcen
from src.util.constant import COLUMN_TYPE_BOX, ENDPOINT_APP, ENDPOINT_APP_TYPE_BOX,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_GENERIC_SAVE

router_save_type_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_BOX+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_type_box.post(endpoint, response_model = response, status_code=status ,tags=["Type_Box"])
async def save(typeBox: TypeBoxfDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_BOX: typeBox})
    service = ServiceArcen(db)
    return service.execute(data)