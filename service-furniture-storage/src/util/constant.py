# UVICORN
APP_UVICORN_NAME= "main:app"
APP_UVICORN_HOST = "http://127.0.0.1/"
APP_UVICORN_PORT = 4000
APP_UVICORN_LOG = "info"

# ENDPOINT
ENDPOINT_APP = "/api"
ENDPOINT_APP_BLOCK = "/block"
ENDPOINT_APP_FURNITURE = "/furniture"
ENDPOINT_APP_TYPE_FURNITURE = "/type-furniture"

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
DATABASE_POSTGRESQL_DATABASE = "arcen_furniture";

# DATABASE CONNECT
DATABASE_POSTGRESQL_URL = "postgresql://{0}:{1}@{2}{3}/{4}".format(
    DATABASE_POSTGRESQL_USER,
    DATABASE_POSTGRESQL_PASSWORD,
    DATABASE_POSTGRESQL_HOST,
    DATABASE_POSTGRESQL_PORT,
    DATABASE_POSTGRESQL_DATABASE
)

# DATABASE TABLE
DATABASE_POSTGRESQL_TABLE_BLOCK = "block"
DATABASE_POSTGRESQL_TABLE_FURNITURE = "furniture"
DATABASE_POSTGRESQL_TABLE_TYPE_FURNITURE = "type_furniture"

# COLUMNA BLOCK
COLUMN_BLOCK = "block"
COLUMN_BLOCK_ID = "id"
COLUMN_BLOCK_LETTER = "letter"
COLUMN_BLOCK_FLAT = "flat"
COLUMN_BLOCK_CREATION_DATE = "date"

# COLUMNA FURNITURE
COLUMN_FURNITURE = "furniture"
COLUMN_FURNITURE_ID = "id"
COLUMN_FURNITURE_ID_BLOCK = "id_block"
COLUMN_FURNITURE_ID_TYPE_FURNITURE = "id_type_furniture"
COLUMN_FURNITURE_NUMBER_FURNITURE = "number_furniture"
COLUMN_FURNITURE_CREATION_DATE = "date"

# COLUMNA TYPE FURNITURE
COLUMN_TYPE_FURNITURE = "type_furniture"
COLUMN_TYPE_FURNITURE_ID = "id"
COLUMN_TYPE_FURNITURE_NUMBER_TYPE_FURNITURE = "number_type_furniture"
COLUMN_TYPE_FURNITURE_COUNT_RACK = "count_rack"
COLUMN_TYPE_FURNITURE_COUNT_ROW = "count_row"
COLUMN_TYPE_FURNITURE_DEPTH = "depth"
COLUMN_TYPE_FURNITURE_HEIGHT = "height"
COLUMN_TYPE_FURNITURE_WIDTH= "width"
COLUMN_TYPE_FURNITURE_CREATION_DATE = "date"
