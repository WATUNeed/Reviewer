import pytest

from moduls import csv_handler
from moduls import settings

import pandas as pd
from pandas.testing import assert_frame_equal
from pandas import DataFrame

import numpy as np


SUCCESS_CASES_READ_CSV = [
    (
        settings.SETTINGS['test_csv_file'],
        pd.DataFrame({'email': ['bryantjames@example.com',
                                'lgreen@example.net',
                                'ryanryan@example.com'],
                      'review text': ["As someone who has struggled with anxiety and stress for years, I've found "
                                      "Welltory to be incredibly helpful. The app's stress tracking and HRV analysis "
                                      "have helped me better understand my body's response to stress, and the guided "
                                      "meditations and breathing exercises have been a lifesaver when I'm feeling "
                                      "overwhelmed.",
                                      "Welltory is a decent app overall. I appreciate the stress tracking and HRV "
                                      "analysis, but I do wish there were more personalized recommendations based on "
                                      "my data. The guided meditations and breathing exercises are helpful, but I wish "
                                      "there were more of them.",
                                      "I like using Welltory to track my stress levels and HRV, but I find the app a "
                                      "bit clunky and difficult to navigate at times. It can also be a bit "
                                      "overwhelming with all the data and graphs. I think the app could benefit from a "
                                      "simpler, more streamlined design."],
                      'date': ['2023-01-15',
                               '2023-02-01',
                               '2023-01-02'],
                      'rate': np.nan})
    )
]

SUCCESS_CASES_INSERT_DATA = [
    (
        pd.DataFrame({'email': ['bryantjames@example.com',
                                'lgreen@example.net',
                                'ryanryan@example.com'],
                      'review text': ["As someone who has struggled with anxiety and stress for years, I've found "
                                      "Welltory to be incredibly helpful. The app's stress tracking and HRV analysis "
                                      "have helped me better understand my body's response to stress, and the guided "
                                      "meditations and breathing exercises have been a lifesaver when I'm feeling "
                                      "overwhelmed.",
                                      "Welltory is a decent app overall. I appreciate the stress tracking and HRV "
                                      "analysis, but I do wish there were more personalized recommendations based on "
                                      "my data. The guided meditations and breathing exercises are helpful, but I wish "
                                      "there were more of them.",
                                      "I like using Welltory to track my stress levels and HRV, but I find the app a "
                                      "bit clunky and difficult to navigate at times. It can also be a bit "
                                      "overwhelming with all the data and graphs. I think the app could benefit from a "
                                      "simpler, more streamlined design."],
                      'date': ['2023-01-15',
                               '2023-02-01',
                               '2023-01-02'],
                      'rate': np.nan}),
        [1, 7, 10],
        ['Negative', 'Neutral', 'Positive'],
        pd.DataFrame({'email': ['ryanryan@example.com',
                                'lgreen@example.net',
                                'bryantjames@example.com'],
                      'review text': ["I like using Welltory to track my stress levels and HRV, but I find the app a "
                                      "bit clunky and difficult to navigate at times. It can also be a bit "
                                      "overwhelming with all the data and graphs. I think the app could benefit from a "
                                      "simpler, more streamlined design.",
                                      "Welltory is a decent app overall. I appreciate the stress tracking and HRV "
                                      "analysis, but I do wish there were more personalized recommendations based on "
                                      "my data. The guided meditations and breathing exercises are helpful, but I wish "
                                      "there were more of them.",
                                      "As someone who has struggled with anxiety and stress for years, I've found "
                                      "Welltory to be incredibly helpful. The app's stress tracking and HRV analysis "
                                      "have helped me better understand my body's response to stress, and the guided "
                                      "meditations and breathing exercises have been a lifesaver when I'm feeling "
                                      "overwhelmed."],
                      'date': ['2023-01-02',
                               '2023-02-01',
                               '2023-01-15'],
                      'rate': [10, 7, 1],
                      'analytics': ['Positive', 'Neutral', 'Negative']}, index=[2, 1, 0])
    )
]

SUCCESS_CASES_WRITE_CSV = [
    (
        settings.SETTINGS['test_analytics_file'],
        pd.DataFrame({'email': ['ryanryan@example.com',
                                'lgreen@example.net',
                                'bryantjames@example.com'],
                      'review text': ["I like using Welltory to track my stress levels and HRV, but I find the app a "
                                      "bit clunky and difficult to navigate at times. It can also be a bit "
                                      "overwhelming with all the data and graphs. I think the app could benefit from a "
                                      "simpler, more streamlined design.",
                                      "Welltory is a decent app overall. I appreciate the stress tracking and HRV "
                                      "analysis, but I do wish there were more personalized recommendations based on "
                                      "my data. The guided meditations and breathing exercises are helpful, but I wish "
                                      "there were more of them.",
                                      "As someone who has struggled with anxiety and stress for years, I've found "
                                      "Welltory to be incredibly helpful. The app's stress tracking and HRV analysis "
                                      "have helped me better understand my body's response to stress, and the guided "
                                      "meditations and breathing exercises have been a lifesaver when I'm feeling "
                                      "overwhelmed."],
                      'date': ['2023-01-02',
                               '2023-02-01',
                               '2023-01-15'],
                      'rate': [10, 7, 1],
                      'analytics': ['Positive', 'Neutral', 'Negative']}, index=[0, 1, 2])
    )
]


@pytest.mark.parametrize('filename, result', SUCCESS_CASES_READ_CSV)
def test_read_csv(filename: str, result: DataFrame):
    assert_frame_equal(result, csv_handler._read_csv_review(filename))


@pytest.mark.parametrize('review_data, rating, analytics, result', SUCCESS_CASES_INSERT_DATA)
def test__insert_rate_in_dataframe(review_data, rating: list[int], analytics: list[str], result: DataFrame):
    assert_frame_equal(result, csv_handler._insert_rate_in_dataframe(review_data, rating, analytics))


@pytest.mark.parametrize('filename, review_data', SUCCESS_CASES_WRITE_CSV)
def test__write_csv_review(filename: str, review_data: DataFrame):
    assert_frame_equal(csv_handler._read_csv_review(filename), review_data)
