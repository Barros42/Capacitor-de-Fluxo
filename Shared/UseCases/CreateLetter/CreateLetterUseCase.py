import datetime

from Shared.Entities.Letter import Letter
from Shared.UseCases.CreateLetter.CreateLetterUseCaseInput import CreateLetterUseCaseInput
from Shared.UseCases.CreateLetter.ICreateLetterUseCase import ICreateLetterUseCase
from Shared.UseCases.Interfaces.Repositories.ILetterRepository import ILetterRepository


class CreateLetterUseCase(ICreateLetterUseCase):
    def __init__(self, letterRepository: ILetterRepository):
        self.letterRepository = letterRepository

    def run(self, data_input: CreateLetterUseCaseInput):
        letter = self._build_letter(data_input)
        return self.letterRepository.createLetter(letter)

    def _build_letter(self, data_input: CreateLetterUseCaseInput) -> Letter:
        return Letter(
            data_input.message,
            data_input.email,
            data_input.deliveryDate.strftime("%Y-%m-%d"),
            datetime.date.today().strftime("%Y-%m-%d"),
            data_input.letterHash
        )
