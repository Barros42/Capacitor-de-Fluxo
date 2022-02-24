import re
from datetime import datetime


class CreateLetterInput:
    def __init__(
            self,
            message,
            email,
            deliveryDate,
            letterHash
    ):
        self.message = self._is_valid_message(message)
        self.email = self._is_valid_email(email)
        self.deliveryDate = self._is_valid_delivery_date(deliveryDate)
        self.letterHash = self._is_valid_letter_hash(letterHash)

    def _is_valid_message(self, message):
        if len(message) <= 0:
            raise ValueError("It's not an valid message")
        return message

    def _is_valid_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            raise ValueError("It's not an email address.")
        return email

    def _is_valid_letter_hash(self, letterHash):
        regex = '[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}'
        if not (re.fullmatch(regex, letterHash)):
            raise ValueError("It's not an valid letter hash.")
        return letterHash

    def _is_valid_delivery_date(self, deliveryDate):
        date_time_obj = datetime.strptime(deliveryDate, "%Y-%m-%d")
        if date_time_obj < datetime.now():
            raise ValueError("It's not an valid delivery date")
        return date_time_obj
