
# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_TRAY = "/tray"
ENDPOINT_APP_BOX = "/box"
ENDPOINT_APP_TYPE_BOX = "/type-box"

ENDPOINT_GENERIC_FIND_BY_ID = "/{id}"
ENDPOINT_GENERIC_FIND_ALL = "/"
ENDPOINT_GENERIC_SAVE = "/"
ENDPOINT_GENERIC_UPDATE= "/{id}"
ENDPOINT_GENERIC_DELETE_BY_ID = "/{id}"

# DATABASE VARS
DATABASE_POSTGRESQL_USER = "arcen";
DATABASE_POSTGRESQL_PASSWORD = "arcen";
DATABASE_POSTGRESQL_HOST = "localhost";
DATABASE_POSTGRESQL_PORT = "";
DATABASE_POSTGRESQL_DATABASE = "arcen_box";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://arcen:arcen@arcen-postgresql:5432/arcen"

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_TRAY = "tray"
DATABASE_POSTGRESQL_TABLE_BOX = "box"
DATABASE_POSTGRESQL_TABLE_TYPE_BOX = "type_box"

# COLUMNA TRAY
COLUMN_TRAY = "tray"
COLUMN_TRAY_ID = "id"
COLUMN_TRAY_ID_SHELF = "id_shelf"
COLUMN_TRAY_HEIGHT = "height"
COLUMN_TRAY_WIDTH = "width"
COLUMN_TRAY_DEPTH = "depth"
COLUMN_TRAY_CREATION_DATE = "date"

# COLUMNA BOX
COLUMN_BOX = "box"
COLUMN_BOX_ID = "id"
COLUMN_BOX_NUMBER_BOX = "number_box"
COLUMN_BOX_ID_TRAY = "id_tray"
COLUMN_BOX_ID_TYPE_BOX = "id_type_box"
COLUMN_BOX_CREATION_DATE = "date"

# COLUMNA TYPE BOX
COLUMN_TYPE_BOX = "type_box"
COLUMN_TYPE_BOX_ID = "id"
COLUMN_TYPE_BOX_NUMBER_TYPE_BOXF = "number_type_box"
COLUMN_TYPE_BOX_DEPTH = "depth"
COLUMN_TYPE_BOX_HEIGHT = "height"
COLUMN_TYPE_BOX_WIDTH= "width"
COLUMN_TYPE_BOX_CREATION_DATE = "date"

# FEIGN
FEIGN_TYPE_POST = "POST"
FEIGN_TYPE_GET = "GET"
FEIGN_TYPE_PUT = "PUT"
FEIGN_TYPE_DELETE = "DELETE"

FEIGN_ENDPOINT = "endpoint"
FEIGN_ENDPOINT_AUDIT = "http://arcen-service-audit:8001/api/audit"
FEIGN_ENDPOINT_AUDIT_SAVE = "/"

FEIGN_ENDPOINT_SHELF = "http://arcen-service-shelf-storage:8008/api/shelf"
FEIGN_ENDPOINT_SHELF_SAVE = "/"

# RESPONSE STATUS
RESPONSE_STATUS_CODE_GET = 200
RESPONSE_STATUS_CODE_POST = 201
RESPONSE_STATUS_CODE_PUT = 202
RESPONSE_STATUS_CODE_DELETE = 204

# RESPONSE MODEL
RESPONSE_MODEL_TRAY_FIND_ALL = list
RESPONSE_MODEL_TRAY_DELETE_BY_ID = bool

RESPONSE_MODEL_BOX_FIND_ALL = list
RESPONSE_MODEL_BOX_DELETE_BY_ID = bool

RESPONSE_MODEL_TYPE_BOX_FIND_ALL = list
RESPONSE_MODEL_TYPE_BOX_DELETE_BY_ID = bool

# RESPONSE STATUS
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_ALL_BY_RANGE_DATE_ERROR_FORMAT = 400
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID = 200
RESPONSE_STATUS_CODE_GENERIC_FIND_BY_ID_NOT_CONTENT = 424
RESPONSE_STATUS_CODE_GENERIC_SAVE = 201
RESPONSE_STATUS_CODE_GENERIC_SAVE_ERROR_SAVE = 423
RESPONSE_STATUS_CODE_GENERIC_DELETE = 204
RESPONSE_STATUS_CODE_GENERIC_UPDATE = 202

RESPONSE_STATUS_CODE_AUDIT_ERROR_SAVE = 423



# RESPONSE MSG
RESPONSE_MSG_AUDIT_ERROR_SAVE = "Ups hemos tenido un problema interno! vuelva a intentar mas tarde."

RESPONSE_MSG_SHELF_ERROR_SAVE = "No se encontro ningun estante con el id suministrado."

RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT = "Por favor verificar las fechas no son validas."

RESPONSE_MSG_BOX_FIND_BY_ID_NOT_CONTENT =  "No se encontro una caja con el id suministrado."
RESPONSE_MSG_BOX_SAVE_ERROR_SAVE =  "No se registro la caja, vuelvalo a intentar mas tarde."

RESPONSE_MSG_TYPE_BOX_FIND_BY_ID_NOT_CONTENT =  "No se encontro ningun tipo de caja con el id suministrado."
RESPONSE_MSG_TYPE_BOX_SAVE_ERROR_SAVE =  "No se registro el tipo de caja, vuelvalo a intentar mas tarde."

RESPONSE_MSG_TRAY_FIND_BY_ID_NOT_CONTENT = "No se encontro ninguna bandeja con el id suministrado."
RESPONSE_MSG_TRAY_SAVE_ERROR_SAVE =  "No se registro la bandeja, vuelvalo a intentar mas tarde."

RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT = "No se encontro ningun estante con el id suministrado."

# AUDIT
AUDIT_TRAY_SERVICE = "TRAY"
AUDIT_BOX_SERVICE = "BOX"
AUDIT_TYPE_BOX_SERVICE = "TYPE_BOX"

AUDIT_GENERIC_OPERATION_SAVE = "SAVE"
AUDIT_GENERIC_OPERATION_UPDATE = "UPDATE"
AUDIT_GENERIC_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"




# DATA
DATA_REMOVE = "isRemove"
DATA_REMOVE_VALUE_DEFAULT = False

SHELF_SERVICE_HOST_URL = 'http://localhost:8004/api/shelf/'