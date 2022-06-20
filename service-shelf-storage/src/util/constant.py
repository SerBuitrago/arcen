
# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_DEPENDENCE = "/dependence"
ENDPOINT_APP_SHELF = "/shelf"
ENDPOINT_APP_TYPE_SHELF = "/type-shelf"

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
DATABASE_POSTGRESQL_DATABASE = "arcen_shelf";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://arcen:arcen@arcen-postgresql:5432/arcen"

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_DEPENDENCE = "dependence"
DATABASE_POSTGRESQL_TABLE_SHELF = "shelf"
DATABASE_POSTGRESQL_TABLE_TYPE_SHELF = "type_shelf"

# COLUMNA DEPENDENCE
COLUMN_DEPENDENCE = "dependence"
COLUMN_DEPENDENCE_ID = "id"
COLUMN_DEPENDENCE_NAME = "name"
COLUMN_DEPENDENCE_CODE = "code"

# COLUMNA SHELF
COLUMN_SHELF = "shelf"
COLUMN_SHELF_ID = "id"
COLUMN_SHELF_ID_DEPENDENCE = "id_dependence"
COLUMN_SHELF_ID_TYPE_SHELF = "id_type_shelf"
COLUMN_SHELF_ID_FURNITURE = "id_furniture"
COLUMN_SHELF_NUMBER_SHELF = "number_shelf"
COLUMN_SHELF_CREATION_DATE = "date"

# COLUMNA TYPE SHELF
COLUMN_TYPE_SHELF = "type_shelf"
COLUMN_TYPE_SHELF_ID = "id"
COLUMN_TYPE_SHELF_NUMBER_TYPE_SHELF = "number_type_shelf"
COLUMN_TYPE_SHELF_DEPTH = "depth"
COLUMN_TYPE_SHELF_HEIGHT = "height"
COLUMN_TYPE_SHELF_WIDTH= "width"
COLUMN_TYPE_SHELF_CREATION_DATE = "date"

# FEIGN
FEIGN_TYPE_POST = "POST"
FEIGN_TYPE_GET = "GET"
FEIGN_TYPE_PUT = "PUT"
FEIGN_TYPE_DELETE = "DELETE"

FEIGN_ENDPOINT = "endpoint"
FEIGN_ENDPOINT_AUDIT = "http://arcen-service-audit:8001/api/audit"
FEIGN_ENDPOINT_AUDIT_SAVE = "/"

FEIGN_ENDPOINT_FURNITURE = "http://arcen-service-furniture-storage:8004/api/furniture"
FEIGN_ENDPOINT_FURNITURE_SAVE = "/"

# RESPONSE STATUS
RESPONSE_STATUS_CODE_GET = 200
RESPONSE_STATUS_CODE_POST = 201
RESPONSE_STATUS_CODE_PUT = 202
RESPONSE_STATUS_CODE_DELETE = 204

# RESPONSE MODEL
RESPONSE_MODEL_DEPENDENCE_FIND_ALL = list
RESPONSE_MODEL_DEPENDENCE_DELETE_BY_ID = bool

RESPONSE_MODEL_SHELF_FIND_ALL = list
RESPONSE_MODEL_SHELF_DELETE_BY_ID = bool

RESPONSE_MODEL_TYPE_SHELF_FIND_ALL = list
RESPONSE_MODEL_TYPE_SHELF_DELETE_BY_ID = bool

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

RESPONSE_MSG_FURNITURE_ERROR_SAVE = "No se encontro ningun mueble con el id suministrado."


RESPONSE_MSG_GENERIC_DATE_ERROR_FORMAT = "Por favor verificar las fechas no son validas."

RESPONSE_MSG_SHELF_FIND_BY_ID_NOT_CONTENT =  "No se encontro un estante con el id suministrado."
RESPONSE_MSG_SHELF_SAVE_ERROR_SAVE =  "No se registro el estante, vuelvalo a intentar mas tarde."

RESPONSE_MSG_TYPE_SHELF_FIND_BY_ID_NOT_CONTENT =  "No se encontro ningun tipo de estante con el id suministrado."
RESPONSE_MSG_TYPE_SHELF_SAVE_ERROR_SAVE =  "No se registro tipo de estante, vuelvalo a intentar mas tarde."

RESPONSE_MSG_DEPENDENCE_FIND_BY_ID_NOT_CONTENT = "No se encontro ninguna dependencia con el id suministrado."
RESPONSE_MSG_DEPENDENCE_SAVE_ERROR_SAVE =  "No se registro la dependencia, vuelvalo a intentar mas tarde."

RESPONSE_MSG_FURNITURE_FIND_BY_ID_NOT_CONTENT = "No se encontro ningun mueble con el id suministrado."

# AUDIT
AUDIT_DEPENDENCE_SERVICE = "DEPENDENCE"
AUDIT_SHELF_SERVICE = "SHELF"
AUDIT_TYPE_SHELF_SERVICE = "TYPE_SHELF"

AUDIT_GENERIC_OPERATION_SAVE = "SAVE"
AUDIT_GENERIC_OPERATION_UPDATE = "UPDATE"
AUDIT_GENERIC_OPERATION_DELETE_BY_ID = "DELETE_BY_ID"




# DATA
DATA_REMOVE = "isRemove"
DATA_REMOVE_VALUE_DEFAULT = False

FURNITURE_SERVICE_HOST_URL = 'http://arcen-service-furniture-storage:8004/api/furniture/'