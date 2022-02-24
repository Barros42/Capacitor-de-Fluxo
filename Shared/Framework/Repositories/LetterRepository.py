from bson import ObjectId

from Shared.Entities.Letter import Letter
from Shared.Framework.Repositories.CosmosConnection import getDatabase
from Shared.UseCases.Interfaces.Repositories.ILetterRepository import ILetterRepository


class LetterRepository(ILetterRepository):
    def __init__(self):
        self.database = getDatabase()
        self.collection = self.database["Letters"]
        pass

    def createLetter(self, letter: Letter):
        return self.collection.insert_one({
            "message": letter.message,
            "email": letter.email,
            "deliveryDate": letter.deliveryDate,
            "sendDate": letter.sendDate,
            "letterHash": letter.letterHash
        })

    def get_letter_by_id(self, letter_id):
        return self.collection.find_one({
           "_id": ObjectId(letter_id)
        })

    def get_letters_by_delivery_date(self, delivery_date):
        cursor = self.collection.find({
            "deliveryDate": delivery_date
        })
        letters_ids = []
        for letter in cursor:
            letters_ids.append(str(letter["_id"]))

        return letters_ids
