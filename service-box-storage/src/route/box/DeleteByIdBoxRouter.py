from fastapi import APIRouter, Depends, Response
from http import HTTPStatus

from sqlalchemy.orm import Session

from src.service.box.DeleteByIdBoxService import DeleteByIdBoxService as DeleteService
from src.persistence.database.table.BoxTable import BoxTable as TableArcen
from src.util.constant import COLUMN_BOX_ID, ENDPOINT_APP, ENDPOINT_APP_BOX,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_box = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_BOX+ENDPOINT_GENERIC_DELETE_BY_ID
status = RESPONSE_STATUS_CODE_GENERIC_DELETE

@router_detele_by_id_box.delete(endpoint,status_code=status,tags=["Box"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_BOX_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)