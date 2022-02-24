from Shared.Controllers.CreateLetter.CreateLetterInput import CreateLetterInput
from Shared.UseCases.CreateLetter.CreateLetterUseCaseInput import CreateLetterUseCaseInput
from Shared.UseCases.CreateLetter.ICreateLetterUseCase import ICreateLetterUseCase


class CreateLetterController:
    def __init__(
            self,
            letterUseCase: ICreateLetterUseCase
    ):
        self.letterUseCase = letterUseCase
        pass

    def run(self, data_input: CreateLetterInput):
        use_case_input = self._get_use_case_input(data_input)
        return self.letterUseCase.run(use_case_input)

    def _get_use_case_input(self, data_input: CreateLetterInput) -> CreateLetterUseCaseInput:
        return CreateLetterUseCaseInput(
            message=data_input.message,
            email=data_input.email,
            deliveryDate=data_input.deliveryDate,
            letterHash=data_input.letterHash
        )
