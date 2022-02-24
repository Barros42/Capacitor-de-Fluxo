from Shared.UseCases.CreateLetter.CreateLetterUseCaseInput import CreateLetterUseCaseInput


class ICreateLetterUseCase:
    def run(self, data_input: CreateLetterUseCaseInput):
        raise NotImplementedError()
