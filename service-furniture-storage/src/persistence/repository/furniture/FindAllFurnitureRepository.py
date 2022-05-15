from src.persistence.repository.IRepository import IRepository

from src.persistence.repository.IRepository import IRepository
from src.persistence.database.StorageDB import StorageDB

class FindAllFurnitureRepository(IRepository):

    def __init__(self):
        self.db = StorageDB()
        self.collection = self.db.get_db_furniture()

    def execute(self, data:dict):
        return self.collection.find()