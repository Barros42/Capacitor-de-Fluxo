import logging
import azure.functions as func
from FutureMailer.FunctionSettings import controller


def main(msg: func.ServiceBusMessage):
    message_body = msg.get_body().decode('utf-8')
    logging.info('FutureMailer started with this letter id: [%s]', message_body)
    controller.run(message_body)
