from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from http import HTTPStatus

from src.service.type_shelf.DeleteByIdTypeShelfService import DeleteByIdTypeShelfService as DeleteService
from src.persistence.database.table.TypeShelfTable import TypeShelfTable as TableArcen
from src.util.constant import COLUMN_TYPE_SHELF_ID, ENDPOINT_APP,RESPONSE_STATUS_CODE_GENERIC_DELETE, ENDPOINT_APP_TYPE_SHELF, ENDPOINT_GENERIC_DELETE_BY_ID

router_detele_by_id_type_shelf = APIRouter()
table = TableArcen()

endpoint = ENDPOINT_APP+ENDPOINT_APP_TYPE_SHELF+ENDPOINT_GENERIC_DELETE_BY_ID
status=RESPONSE_STATUS_CODE_GENERIC_DELETE

@router_detele_by_id_type_shelf.delete(endpoint,status_code=status,tags=["TypeShelf"])
async def delete_by_id(id: str, db: Session = Depends(table.execute)):
    data = dict({COLUMN_TYPE_SHELF_ID:id})
    service = DeleteService(db)
    service.execute(data)
    return Response(status_code=HTTPStatus.NO_CONTENT.value)