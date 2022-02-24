from Shared.Controllers.SendLetter.SendLetterController import SendLetterController
from Shared.Framework.Repositories.LetterRepository import LetterRepository
from Shared.Framework.Services.SendGridMailService import SendGridMailService
from Shared.UseCases.SendLetter.SendLetterUseCase import SendLetterUseCase

repository = LetterRepository()
mail_service = SendGridMailService()
use_case = SendLetterUseCase(repository, mail_service)
controller = SendLetterController(use_case)
