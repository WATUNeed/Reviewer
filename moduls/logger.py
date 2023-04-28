from moduls import settings

import logging
import logging.config
import logging.handlers

import json


LOGGER = logging.getLogger('main.logger')


class Logger:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Logger.__instance:
            Logger.__instance[cls] = super().__new__(cls)
        return Logger.__instance[cls]

    @staticmethod
    def init_logging():
        logging.config.dictConfig(Logger._get_log_config())
        LOGGER.debug(settings.SETTINGS['logger_init'])

    @staticmethod
    def _get_log_config() -> dict:
        with open(settings.SETTINGS['logger_config'], 'r') as config:
            return json.load(config)
