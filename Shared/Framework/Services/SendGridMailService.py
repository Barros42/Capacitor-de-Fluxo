import json
import requests

from Shared.Framework.Configurations.__main__ import CONFIG_EMAIL_SERVICE_API_URL, CONFIG_EMAIL_SERVICE_API_KEY, \
    CONFIG_EMAIL_SERVICE_SENDER_EMAIL, CONFIG_EMAIL_SERVICE_TEMPLATE_ID
from Shared.UseCases.Interfaces.Services.IEmailService import IEmailService


class SendGridMailService(IEmailService):
    def __init__(self):
        self.api_url = CONFIG_EMAIL_SERVICE_API_URL
        self.api_key = CONFIG_EMAIL_SERVICE_API_KEY
        self.email_template_id = CONFIG_EMAIL_SERVICE_TEMPLATE_ID
        self.from_email = CONFIG_EMAIL_SERVICE_SENDER_EMAIL

    def send_future_email(
            self,
            message,
            email,
            send_date,
            days_in_past
    ):
        response = requests.post(
            url=self.api_url,
            data=self.get_payload(message, email, send_date, days_in_past),
            headers={
                "Authorization": "Bearer {}".format(self.api_key),
                "Content-Type": "application/json"
            }
        )
        print(response)

    def get_payload(self, message, email, send_date, days_in_past):
        return json.dumps({
            "from": {
                "email": self.from_email
            },
            "personalizations": [
                {
                    "to": [
                        {
                            "email": email
                        }
                    ],
                    "dynamic_template_data": {
                        "message": message,
                        "days_in_past": days_in_past,
                        "send_date": send_date
                    }
                }
            ],
            "template_id": self.email_template_id
        })
