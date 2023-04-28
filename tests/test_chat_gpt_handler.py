import pytest

from moduls import chat_gpt_handler
from moduls import prompt_handler


SUCCESS_CASE_ONE_RESPONSE = [
    (
        prompt_handler.build_prompt("Welltory to be incredibly helpful. The app's stress tracking and HRV analysis "
                                    "have helped me better understand my body's response to stress, and the guided "
                                    "meditations and breathing exercises have been a lifesaver when I'm feeling "
                                    "overwhelmed."),
        "\n\n['10', 'positive']"
    )
]

SUCCESS_CASE_MULTY_RESPONSES = [
    (
        ["Welltory is a decent app overall. I appreciate the stress tracking and HRV analysis, but I do wish there "
        "were more personalized recommendations based on my data. The guided meditations and breathing exercises are "
        "helpful, but I wish there were more of them.",
        "I found Welltory to be a bit of a letdown. While the app provides some interesting data about my health, I "
        "didn't find it particularly useful in terms of making meaningful changes in my life. The guided meditations "
        "and breathing exercises were okay, but I didn't find them to be any better than other meditation apps out "
        "there."],
        [['7', 'Neutral'], ['3', 'Negative']]
    )
]


@pytest.mark.parametrize('prompt, result', SUCCESS_CASE_ONE_RESPONSE)
def test__receive_responses(prompt: str, result: str):
    assert chat_gpt_handler.ReviewRanger()._receive_responses(prompt)['choices'][0]['text'] == result


@pytest.mark.parametrize('reviews_list, result', SUCCESS_CASE_MULTY_RESPONSES)
def test_get_result_of_prompt(reviews_list: list[str], result: list):
    assert chat_gpt_handler.ReviewRanger().get_result_of_prompt(reviews_list) == result
