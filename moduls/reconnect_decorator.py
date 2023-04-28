from moduls import settings

import openai

from time import sleep

import logging.handlers


LOGGER = logging.getLogger('main.reconnect_decorator')


def reconnect(func):
    timeout = 60

    def get_response(*args, **kwargs):
        try:
            LOGGER.debug(settings.SETTINGS['try_connect'])
            return func(*args, **kwargs)
        except openai.error.APIError as e:
            LOGGER.exception(f"OpenAI API returned an API Error: {e}")
            sleep(timeout)
            get_response(*args, **kwargs)
        except openai.error.APIConnectionError as e:
            LOGGER.exception(f"Failed to connect to OpenAI API: {e}")
            sleep(timeout)
            get_response(*args, **kwargs)
        except openai.error.RateLimitError as e:
            LOGGER.exception(e)
            raise f"OpenAI API request exceeded rate limit: {e}"

    return get_response
