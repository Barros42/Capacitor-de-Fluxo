from azure.servicebus import ServiceBusClient, ServiceBusMessage

from Shared.Framework.Configurations.__main__ import CONFIG_SERVICE_BUS_CONNECTION_STRING
from Shared.UseCases.Interfaces.Services.IQueueService import IQueueService


class AzureServiceBusQueueService(IQueueService):
    def __init__(self):
        pass

    def send_message(self, message, queue):
        servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONFIG_SERVICE_BUS_CONNECTION_STRING,
                                                                    logging_enable=True)
        with servicebus_client:
            sender = servicebus_client.get_queue_sender(queue_name=queue)
            with sender:
                self.send_single_message(sender, message)

    def send_single_message(self, sender, message):
        message = ServiceBusMessage(message)
        return sender.send_messages(message)
