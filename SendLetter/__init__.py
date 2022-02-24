import json
import logging
from typing import Any

import azure.functions as func

from SendLetter.FunctionSettings import controller
from Shared.Controllers.CreateLetter.CreateLetterInput import CreateLetterInput


def extract_data_from_request(json: Any) -> CreateLetterInput:
    return CreateLetterInput(
        json.get("message"),
        json.get("email"),
        json.get("date"),
        json.get("id")
    )


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('# SendLetter Started #')
    try:
        request_body = req.get_json()
        logging.info('# SendLetter Body', request_body)
        data_input = extract_data_from_request(request_body)
        controller.run(data_input)
        return func.HttpResponse(json.dumps({
            "send": True
        }), status_code=200, headers={
            "Content-Type": "application/json"
        })
    except Exception as e:
        return func.HttpResponse({"Error": str(e)}, status_code=400)
