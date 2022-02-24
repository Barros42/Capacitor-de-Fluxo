from Shared.UseCases.PublishLetters.IPublishLettersUseCase import IPublishLettersUseCase


class ChronosWatcherController:
    def __init__(
            self,
            publishLetterUseCase: IPublishLettersUseCase
    ):
        self.publishLetterUseCase = publishLetterUseCase
        pass

    def run(self):
        return self.publishLetterUseCase.run()
