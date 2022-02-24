from Shared.UseCases.SendLetter.ISendLetterUseCase import ISendLetterUseCase


class SendLetterController:
    def __init__(
            self,
            sendLetterUseCase: ISendLetterUseCase
    ):
        self.sendLetterUseCase = sendLetterUseCase

    def run(self, letter_id):
        return self.sendLetterUseCase.run(letter_id)



