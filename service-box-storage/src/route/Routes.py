from fastapi import FastAPI

# ROUTES BOX
from src.route.box.DeleteByIdBoxRouter import router_detele_by_id_box
from src.route.box.FindAllBoxRouter import router_find_all_box
from src.route.box.FindByIdBoxRouter import router_find_by_id_box
from src.route.box.SaveBoxRouter import router_save_box
from src.route.box.UpdateBoxRouter import router_update_box


# ROUTES TYPE BOX
from src.route.type_box.DeleteByIdTypeBoxRouter import router_detele_by_id_type_box
from src.route.type_box.FindAllTypeBoxRouter import router_find_all_type_box
from src.route.type_box.FindByIdTypeBoxRouter import router_find_by_id_type_box
from src.route.type_box.SaveTypeBoxRouter import router_save_type_box
from src.route.type_box.UpdateTypeBoxRouter import router_update_type_box

# ROUTES TRAY
from src.route.tray.DeleteByIdTrayRouter import router_detele_by_id_tray
from src.route.tray.FindAllTrayRouter import router_find_all_tray
from src.route.tray.FindByIdTrayRouter import router_find_by_id_tray
from src.route.tray.SaveTrayRouter import router_save_tray
from src.route.tray.UpdateTrayRouter import router_update_tray

routes = FastAPI()
# ADD ROUTES


routes.include_router(router_detele_by_id_type_box)
routes.include_router(router_find_all_type_box)
routes.include_router(router_find_by_id_type_box)
routes.include_router(router_save_type_box)
routes.include_router(router_update_type_box)

routes.include_router(router_detele_by_id_box)
routes.include_router(router_find_all_box)
routes.include_router(router_find_by_id_box)
routes.include_router(router_save_box)
routes.include_router(router_update_box)

routes.include_router(router_detele_by_id_tray)
routes.include_router(router_find_all_tray)
routes.include_router(router_find_by_id_tray)
routes.include_router(router_save_tray)
routes.include_router(router_update_tray)