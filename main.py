from database import Database
from motorista_dao import MotoristaDAO
from motorista_cli import MotoristaCLI

db = Database(database="atividade_avaliativa_1", collection="motoristas")
driverModel = MotoristaDAO(database=db)

driverCLI = MotoristaCLI(driverModel)
driverCLI.run()
