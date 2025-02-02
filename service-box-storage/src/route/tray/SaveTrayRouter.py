from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.TrayDto import TrayDto
from src.model.response.TrayResponse import TrayResponse as ResponseArcen
from src.service.tray.SaveTrayService import SaveTrayService as ServiceArcen
from src.persistence.database.table.TrayTable import TrayTable as TableArcen
from src.util.constant import COLUMN_TRAY, ENDPOINT_APP, ENDPOINT_APP_TRAY,RESPONSE_STATUS_CODE_GENERIC_SAVE, ENDPOINT_GENERIC_SAVE

router_save_tray = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TRAY+ENDPOINT_GENERIC_SAVE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_SAVE

@router_save_tray.post(endpoint, response_model = response, status_code=status ,tags=["Tray"])
async def save(tray: TrayDto, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TRAY: tray})
    service = ServiceArcen(db)
    return service.execute(data)