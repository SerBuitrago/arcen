from sqlalchemy.orm import Session

from src.service.IService import IService
from src.persistence.repository.block.SaveBlockRepository import SaveBlockRepository
from src.persistence.schema.BlockSchema import BlockSchema

class SaveBlockService(IService):

    def __init__(self, db: Session):
        self.repository = SaveBlockRepository(db)
        self.schema = BlockSchema()

    def execute(self, data:dict):
        try:
            element = self.repository.execute(data)
            element = self.schema.block(element)
        except:
            element = None
        return element