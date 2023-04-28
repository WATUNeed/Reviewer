from moduls import settings
from moduls import chat_gpt_handler
from moduls import csv_handler
from moduls import logger

import logging.handlers


logger.Logger().init_logging()
LOGGER = logging.getLogger('main')

if __name__ == '__main__':
    try:
        review_ranger = chat_gpt_handler.ReviewRanger()

        review_text = csv_handler.get_review(settings.SETTINGS['csv_file'],
                                             csv_handler.NamesColumns.review_text).values.tolist()

        review_data = review_ranger.get_result_of_prompt(review_text)

        rating = [int(e[0]) for e in review_data]

        analytics = [e[1] for e in review_data]

        csv_handler.write_result_in_dataframe(rating, analytics)

        LOGGER.info(settings.SETTINGS['completed'])
    except Exception as e:
        LOGGER.exception(e)
