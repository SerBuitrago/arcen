from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.model.dto.UserDto import UserDto
from src.model.response.UserResponse import UserResponse as ResponseArcen
from src.service.user.UpdateUserService import UpdateUserService as ServiceArcen
from src.persistence.database.table.UserTable import UserTable as TableArcen
from src.util.constant import COLUMN_USER, COLUMN_USER_ID,RESPONSE_STATUS_CODE_GENERIC_UPDATE, ENDPOINT_APP, ENDPOINT_APP_USER, ENDPOINT_GENERIC_UPDATE

router_update_user = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_USER+ENDPOINT_GENERIC_UPDATE
response = ResponseArcen
status=RESPONSE_STATUS_CODE_GENERIC_UPDATE

@router_update_user.put(endpoint ,response_model = response ,status_code=status,tags=["User"])
async def update(id: str, user: UserDto, db: Session = Depends(table.execute)):
    data = dict({
        COLUMN_USER_ID: id, 
        COLUMN_USER: user
    })
    service = ServiceArcen(db)
    return service.execute(data)