import datetime

from Shared.Framework.Configurations.__main__ import CONFIG_SERVICE_BUS_EMAIL_QUEUE
from Shared.UseCases.Interfaces.Repositories.ILetterRepository import ILetterRepository
from Shared.UseCases.Interfaces.Services.IQueueService import IQueueService
from Shared.UseCases.PublishLetters.IPublishLettersUseCase import IPublishLettersUseCase


class PublishLetterUseCase(IPublishLettersUseCase):
    def __init__(
            self,
            letterRepository: ILetterRepository,
            queueService: IQueueService,
    ):
        self.letterRepository = letterRepository
        self.queueService = queueService
        self.queue_name = CONFIG_SERVICE_BUS_EMAIL_QUEUE

    def run(self):
        letters_ids_to_send = self.get_letters_id_to_send()
        for letter_id in letters_ids_to_send:
            self.queueService.send_message(letter_id, self.queue_name)

    def get_letters_id_to_send(self):
        return self.letterRepository.get_letters_by_delivery_date(datetime.date.today().strftime("%Y-%m-%d"))
