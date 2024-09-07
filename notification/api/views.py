import json
from abc import ABC, abstractmethod

from django.core.exceptions import EmptyResultSet
from django.db import DatabaseError
from rest_framework import serializers, status

from notification.models import BackendUser, Channel, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging

logger = logging.getLogger('api.views')

logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s at %(asctime)s (%(levelname)s) :: %(message)s')
sh = logging.StreamHandler()

sh.setFormatter(formatter)
logger.addHandler(sh)


def generate_log_message(user_name, user_id, message_category, channel_type, message_content):
    log_message = (f"A message was sent to the user {user_name} with id {user_id}, the message category is "
                   f"{message_category} and was sent via the channel {channel_type}. "
                   f"\n\tThe message contents are: '{message_content}'.")
    return log_message


class AbstractChannel(ABC):
    @abstractmethod
    def send_message(self, message_content: str, user: BackendUser, message_category: str) -> None:
        pass


class SMSChannel(AbstractChannel):
    def send_message(self, message_content: str, user: BackendUser, message_category: str) -> None:
        channel_type = "SMS"
        log_message = generate_log_message(user.name, user.id, message_category.capitalize(), channel_type,
                                           message_content)
        logger.info(log_message)


class PushChannel(AbstractChannel):
    def send_message(self, message_content: str, user: BackendUser, message_category: str) -> None:
        channel_type = "Push"
        log_message = generate_log_message(user.name, user.id, message_category.capitalize(), channel_type,
                                           message_content)
        logger.info(log_message)


class EmailChannel(AbstractChannel):
    def send_message(self, message_content: str, user: BackendUser, message_category: str) -> None:
        channel_type = "Email"
        log_message = generate_log_message(user.name, user.id, message_category.capitalize(), channel_type,
                                           message_content)
        logger.info(log_message)


class MessageSender:
    def __init__(self, channel_strategy: AbstractChannel) -> None:
        self._channel_strategy = channel_strategy

    def send_message(self, message_content: str, user: BackendUser, message_category: str) -> None:
        self._channel_strategy.send_message(message_content, user, message_category)
        return


def create_sender_by_channel_type(channel):
    message_sender = None
    if channel == "sms":
        message_sender = MessageSender(SMSChannel())
    elif channel == "email":
        message_sender = MessageSender(EmailChannel())
    elif channel == "push":
        message_sender = MessageSender(PushChannel())
    else:
        raise serializers.ValidationError({'message_channel': 'Invalid message channel.'})
    return message_sender


@api_view(['POST'])
def send_message(request):
    if request.method == 'POST':

        message_category = request.data['message_category'].lower()
        message_content = request.data['message_content']
        message_channel_counter = dict()
        # Now we will get the list of subscribers to the category
        try:
            users = BackendUser.objects.filter(subscribed_categories__name=message_category)
            if not users:
                raise serializers.ValidationError({'User': 'No subscribed users were found for that category.'})
            for user in users:
                # We get the channels that the user is subscribed to
                subscribed_channels = user.channels.all()
                for channel in subscribed_channels:
                    sender = create_sender_by_channel_type(channel.name.lower())
                    sender.send_message(message_content, user, message_category)
                    message_channel_counter[channel.name.lower()] = message_channel_counter.get(channel.name.lower(), 0) + 1
            json_response = {"Number of times each channel type was used to send the message to the users": sorted(message_channel_counter.items())}
            return Response(json_response, status.HTTP_200_OK)
        except DatabaseError as e:
            logger.error(f"There was an error while retrieving data from the database: {str(e)}")
