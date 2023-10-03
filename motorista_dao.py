from database import Database
from motorista import Motorista

from bson import ObjectId

class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def criar_motorista(self, motorista: Motorista):
        try:
            corridas = [corrida.to_dict() for corrida in motorista.corridas]
            res = self.db.collection.insert_one({"nota": motorista.nota, "corridas": corridas})
            print(f"Driver created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occured while creating driver: {e}")
            return None

    def ler_dados_motorista(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Driver found: {res}")
            return res
        except Exception as e:
            print(f"An error occured while reading driver data: {e}")
            return None

    def atualizar_motorista(self, id: str, nota: int):
        try:
            res = self.db.collection.update_one({
                "_id": ObjectId(id)}, 
                {"$set": {"nota": nota}}
            )

            print(f"Driver updated: {res.modified_count} document(s) modified")
        except Exception as e:
            print(f"An error occured while updating driver: {e}")
            return None

    def deletar_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Driver deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occured while deleting driver: {e}")
            return None
