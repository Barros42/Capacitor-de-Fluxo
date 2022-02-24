class CreateLetterUseCaseInput:
    def __init__(
            self,
            message,
            email,
            deliveryDate,
            letterHash
    ):
        self.message = message
        self.email = email
        self.deliveryDate = deliveryDate
        self.letterHash = letterHash
