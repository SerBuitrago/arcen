from fastapi import APIRouter

from src.service.audit.FindAllAuditService import FindAllAuditService as ServiceArcen
from src.util.constant import ENDPOINT_APP, ENDPOINT_APP_AUDIT, ENDPOINT_GENERIC_FIND_ALL
from src.util.constant import RESPONSE_MODEL_AUDIT_FIND_ALL, RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

router_find_all_audit = APIRouter()

endpoint = ENDPOINT_APP+ENDPOINT_APP_AUDIT+ENDPOINT_GENERIC_FIND_ALL
response = RESPONSE_MODEL_AUDIT_FIND_ALL
status = RESPONSE_STATUS_CODE_GENERIC_FIND_ALL

@router_find_all_audit.get(endpoint, response_model = response, status_code= status)
async def find_all():
    service = ServiceArcen()
    return service.execute(dict())