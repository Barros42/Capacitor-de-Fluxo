from Shared.Controllers.ChronosWatcher.ChronosWatcher import ChronosWatcherController
from Shared.Framework.Repositories.LetterRepository import LetterRepository
from Shared.Framework.Services.AzureServiceBusQueueService import AzureServiceBusQueueService
from Shared.UseCases.PublishLetters.PublishLettersUseCase import PublishLetterUseCase

repository = LetterRepository()
queue_service = AzureServiceBusQueueService()
use_case = PublishLetterUseCase(repository, queue_service)
controller = ChronosWatcherController(use_case)
