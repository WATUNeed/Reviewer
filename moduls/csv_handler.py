from moduls import settings

import pandas as pd
from pandas import DataFrame

from enum import Enum

import logging.handlers


LOGGER = logging.getLogger('main.csv_handler')


class NamesColumns(Enum):
    email = 'email'
    review_text = 'review text'
    date = 'date'
    rate = 'rate'


def get_review(filename: str, column: NamesColumns) -> DataFrame:
    return _read_csv_review(filename)[column.value]


def _read_csv_review(filename: str) -> DataFrame:
    LOGGER.info(settings.SETTINGS['read_csv'])
    return pd.read_csv(filename)


def write_result_in_dataframe(rating: list[int], analytics: list[str]):
    review_data = _read_csv_review(settings.SETTINGS['csv_file'])
    review_data = _insert_rate_in_dataframe(review_data, rating, analytics)
    _write_csv_review(settings.SETTINGS['csv_analyzed_file'], review_data)
    LOGGER.info(settings.SETTINGS['changes_write'])


def _insert_rate_in_dataframe(review_data: DataFrame, rating: list[int], analytics: list[str]) -> DataFrame:
    rating = pd.DataFrame({NamesColumns.rate.value: rating})
    analytics = pd.DataFrame({'analytics': analytics})
    review_data[NamesColumns.rate.value] = rating[NamesColumns.rate.value].values
    review_data['analytics'] = analytics['analytics'].values
    return review_data.sort_values(by=[NamesColumns.rate.value], ascending=False)


def _write_csv_review(filename: str, review_data: DataFrame):
    LOGGER.info(settings.SETTINGS['write_csv'])
    review_data.to_csv(filename, mode='w', index=False)
