from moduls import settings
from moduls import prompt_handler
from moduls import reconnect_decorator

from time import sleep

import os

import openai

import logging.handlers


LOGGER = logging.getLogger('main.chat_gpt_handler')


class ReviewRanger:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in ReviewRanger.__instance:
            ReviewRanger.__instance[cls] = super().__new__(cls)
        return ReviewRanger.__instance[cls]

    def __init__(self):
        openai.api_key = os.environ.get(settings.SETTINGS['openai_api_key'])
        LOGGER.info(settings.SETTINGS['api_key_received'])

    def get_result_of_prompt(self, reviews_text: list[str]) -> list:
        for index, review in enumerate(reviews_text):
            prompt = prompt_handler.build_prompt(review)
            responese = self._receive_responses(prompt)
            result = prompt_handler.convert_text_to_code(responese['choices'][0]['text'])
            reviews_text[index] = result
            LOGGER.debug(settings.SETTINGS['result_received'])
            sleep(1)

        return reviews_text

    @staticmethod
    @reconnect_decorator.reconnect
    def _receive_responses(prompt: str):
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=64,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
