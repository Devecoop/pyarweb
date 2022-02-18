import logging
import urllib.parse

import requests
from django.conf import settings

TELEGRAM_API_URL = 'https://api.telegram.org/bot'
ERROR_LOG_MESSAGE = (
    'Falló al querer publicar a telegram con las siguientes credenciales=%s Error: %s'
)


def _repr_credentials():
    """Show a string representation of telegram credentials."""
    credentials_repr = (
        f' TELEGRAM_BOT_TOKEN: {settings.TELEGRAM_BOT_TOKEN} '
        f' TELEGRAM_MODERATORS_CHAT_ID: {settings.TELEGRAM_MODERATORS_CHAT_ID} '
        f' TELEGRAM_PUBLIC_CHAT_ID: {settings.TELEGRAM_PUBLIC_CHAT_ID} '
    )

    return credentials_repr


def _compose_message(message: str):
    """Santitize, escape and add environment prefix to message."""
    message_with_prefix = " ".join((settings.TELEGRAM_MESSAGE_PREFIX, message))
    safe_message = urllib.parse.quote_plus(message_with_prefix)
    return safe_message


def _get_request_url(message: str, chat_id: int):
    """Compose url for telegram."""
    bot_token = settings.TELEGRAM_BOT_TOKEN
    url = f'{TELEGRAM_API_URL}{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    return url


def send_message(message: str, chat_id: int):
    """Send a message to a chat using a bot."""
    safe_message = _compose_message(message)
    url = _get_request_url(safe_message, chat_id)
    status = requests.get(url)

    if status.status_code != requests.codes.ok:
        logging.error(ERROR_LOG_MESSAGE, _repr_credentials(), status.text)

    return status.status_code
