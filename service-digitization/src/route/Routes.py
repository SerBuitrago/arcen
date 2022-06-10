from fastapi import FastAPI

# ROUTES AUDIT
from src.route.audit.FindAllAuditRouter import router_find_all_audit
from src.route.audit.FindAllByRangeDateCreationAuditRouter import router_find_all_by_range_date_creation_audit
from src.route.audit.FindByIdAuditRouter import router_find_by_id_audit
from src.route.audit.SaveAuditRouter import router_save_audit

# ROUTES CONTROL AUDIT CLOSURE
from src.route.control_audit.FindAllControlAuditRouter import router_find_all_control_audit
from src.route.control_audit.FindByIdControlAuditRouter import router_find_by_id_control_audit
from src.route.control_audit.FindByNameControlAuditRouter import router_find_by_name_control_audit

# ROUTES AUDIT CLOSURE
from src.route.audit_closure.FindAllAuditClosureRouter import router_find_all_audit_closure
from src.route.audit_closure.FindByIdAuditClosureRouter import router_find_by_id_audit_closure
from src.route.audit_closure.SaveAuditClosureRouter import router_save_audit_closure

routes = FastAPI()

# ADD ROUTES
routes.include_router(router_find_all_audit)
routes.include_router(router_find_all_by_range_date_creation_audit)
routes.include_router(router_find_by_id_audit)
routes.include_router(router_save_audit)

routes.include_router(router_find_all_control_audit)
routes.include_router(router_find_by_id_control_audit)
routes.include_router(router_find_by_name_control_audit)

routes.include_router(router_find_all_audit_closure)
routes.include_router(router_find_by_id_audit_closure)
routes.include_router(router_save_audit_closure)