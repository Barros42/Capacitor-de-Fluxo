from datetime import datetime

from Shared.Helpers.GetBrazilDateFromString import get_brazil_date_from_string
from Shared.UseCases.Interfaces.Repositories.ILetterRepository import ILetterRepository
from Shared.UseCases.Interfaces.Services.IEmailService import IEmailService
from Shared.UseCases.SendLetter.ISendLetterUseCase import ISendLetterUseCase


class SendLetterUseCase(ISendLetterUseCase):

    def __init__(
            self,
            letterRepository: ILetterRepository,
            mailService: IEmailService
    ):
        self.letterRepository = letterRepository
        self.mailService = mailService

    def run(self, letter_id):
        letter_to_send = self.letterRepository.get_letter_by_id(letter_id)
        send_date = datetime.strptime(letter_to_send['sendDate'], "%Y-%m-%d")
        delivery_date = datetime.strptime(letter_to_send['deliveryDate'], "%Y-%m-%d")
        days_in_past = str((delivery_date - send_date).days)
        send_date_formatted = get_brazil_date_from_string(send_date.strftime("%d/%m/%Y"))

        return self.mailService.send_future_email(
            message=letter_to_send['message'],
            email=letter_to_send['email'],
            days_in_past=days_in_past,
            send_date=send_date_formatted
        )
