from Shared.Controllers.CreateLetter.CreateLetterController import CreateLetterController
from Shared.Framework.Repositories.LetterRepository import LetterRepository
from Shared.UseCases.CreateLetter.CreateLetterUseCase import CreateLetterUseCase

repository = LetterRepository()
use_case = CreateLetterUseCase(repository)
controller = CreateLetterController(use_case)
