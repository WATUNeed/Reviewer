import pytest

from moduls.prompt_handler import build_prompt
from moduls.prompt_handler import convert_text_to_code


SUCCESS_CASES_BUILD_PROMPT = [
    (
        "test review.",
        "You own a stress and heart rate variability tracking app::You need to identify the intonation of the review "
        "and Rate the user's review on a ten-point scale, where 10 is 'Most enthusiastic' and 1 is 'Most negative'::"
        "Do not explain your response::The answer should look like this: ['rating', 'intonation']::Review: "
        "'test review.'"
    ),
    (
        "",
        "You own a stress and heart rate variability tracking app::You need to identify the intonation of the review "
        "and Rate the user's review on a ten-point scale, where 10 is 'Most enthusiastic' and 1 is 'Most negative'::"
        "Do not explain your response::The answer should look like this: ['rating', 'intonation']::Review: ''"
    )
]

SUCCESS_CASES_CONVERT_TEXT_TO_CODE = [
    (
        "['10', 'Positive']",
        ['10', 'Positive']
    ),
    (
        "['7', 'Neutral']",
        ['7', 'Neutral']
    ),
    (
        "['1', 'Negative']",
        ['1', 'Negative']
    ),
]

EXCEPTION_CASES_CONVERT_TEXT_TO_CODE = [
    (
        "",
        SyntaxError
    ),
    (
        "['1', 'Negative'",
        SyntaxError
    ),
    (
        "'Negative'",
        ValueError
    ),
    (
        "['1', 'Negative', 'os.del']",
        ValueError
    ),
    (
        "[None, 'Negative']",
        ValueError
    ),
]


@pytest.mark.parametrize('text, result', SUCCESS_CASES_BUILD_PROMPT)
def test_normal_cases_build_prompt(text: str, result: str):
    assert result == build_prompt(text)


@pytest.mark.parametrize('text, result', SUCCESS_CASES_CONVERT_TEXT_TO_CODE)
def test_normal_cases_convert_text_to_code(text: str, result: list):
    assert result == convert_text_to_code(text)


@pytest.mark.parametrize('text, e', EXCEPTION_CASES_CONVERT_TEXT_TO_CODE)
def test_exception_cases_convert_text_to_code(text: str, e: str):
    with pytest.raises(e):
        convert_text_to_code(text)
