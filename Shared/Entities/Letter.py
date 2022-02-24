import datetime


class Letter:
    def __init__(self,
                 message,
                 email,
                 deliveryDate,
                 sendDate,
                 letterHash):
        self.message = message
        self.email = email
        self.deliveryDate = deliveryDate
        self.sendDate = sendDate
        self.letterHash = letterHash
