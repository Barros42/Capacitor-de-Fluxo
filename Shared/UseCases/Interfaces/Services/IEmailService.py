class IEmailService:
    def send_future_email(
            self,
            message,
            email,
            send_date,
            days_in_past
    ):
        raise NotImplementedError()
