from sqlalchemy.orm import Session

from src.persistence.repository.IRepository import IRepository
from src.util.constant import COLUMN_DEPENDENCE

class DeleteByIdDependenceRepository(IRepository):

    def __init__(self, db: Session):
        self.db = db

    def execute(self, data:dict):
        element = data[COLUMN_DEPENDENCE]
        self.db.delete(element)
        self.db.commit()
        return True