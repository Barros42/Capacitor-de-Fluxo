from Shared.Entities import Letter


class ILetterRepository:
    def createLetter(self, letter: Letter):
        raise NotImplementedError()

    def get_letter_by_id(self, letter_id):
        raise NotImplementedError()

    def get_letters_by_delivery_date(self, delivery_date):
        raise NotImplementedError()
