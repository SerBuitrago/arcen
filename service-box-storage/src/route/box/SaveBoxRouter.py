from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.BoxDto import BoxDto
from src.model.response.BoxResponse import BoxResponse as ResponseArcen
from src.service.box.SaveBoxService import SaveBoxService as ServiceArcen
from src.persistence.database.table.BoxTable import BoxTable as TableArcen
from src.util.constant import COLUMN_BOX, ENDPOINT_APP, ENDPOINT_APP_BOX,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_GENERIC_SAVE

router_save_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BOX+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_box.post(endpoint, response_model = response, status_code=status ,tags=["Box"])
async def save(box: BoxDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BOX: box})
    service = ServiceArcen(db)
    return service.execute(data)