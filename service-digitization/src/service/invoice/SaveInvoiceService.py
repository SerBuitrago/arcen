from fastapi import HTTPException

from src.feign.AuditFeign import AuditFeign

from src.persistence.repository.invoice.SaveInvoiceRepository import SaveInvoiceRepository
from src.persistence.schema.InvoiceSchema import InvoiceSchema

from src.service.IService import IService
from src.service.invoice.FindByIdInvoiceService import FindByIdInvoiceService

from src.util.constant import COLUMN_INVOICE, COLUMN_INVOICE_ID_TWO
from src.util.constant import RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_DOCUMENT_SAVE_ERROR_SAVE
from src.util.constant import AUDIT_INVOICE_SERVICE, AUDIT_INVOICE_OPERATION_SAVE
from src.util.constant import DATA_COMMON_ERROR_CODE, DATA_COMMON_ERROR_MSG
from src.util.common import generate_date, get_http_exception, get_response_audit

class SaveInvoiceService(IService):

    def __init__(self):
        self.repository = SaveInvoiceRepository()
        self.findByIdAudit = FindByIdInvoiceService()
        self.schema = InvoiceSchema()
        self.feign_audit = AuditFeign()

    def execute(self, data:dict):
        try:
            document = self.schema.dict(dict(data[COLUMN_INVOICE]), generate_date())
            data = dict({COLUMN_INVOICE: self.schema.request(dict(document))})
            element = self.repository.execute(data)
        except HTTPException as error_http:
            self.error(error_http.status_code, error_http.detail)
        except:
            self.error(RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE, RESPONSE_MSG_DOCUMENT_SAVE_ERROR_SAVE)
        # Find document by id
        data = dict({COLUMN_INVOICE_ID_TWO: str(element)})
        element = self.findByIdAudit.execute(data)
        self.audit(element)
        return element

    def audit(self, response):
        return self.feign_audit.save(self.feign_audit.build(AUDIT_INVOICE_SERVICE, AUDIT_INVOICE_OPERATION_SAVE, get_response_audit(response)))
    
    def error(self, code, error):
        self.audit({
            DATA_COMMON_ERROR_CODE: code,
            DATA_COMMON_ERROR_MSG: error
        })
        raise get_http_exception(code, error)