from moduls import settings


def build_prompt(review_text: str) -> str:
    return f"{settings.SETTINGS['prompt']}'{review_text}'"


def convert_text_to_code(text: str) -> list:
    result = eval(text.replace('\n', ''))

    if not isinstance(result, list):
        raise ValueError

    if not len(result) == 2:
        raise ValueError

    for i in result:
        if not isinstance(i, str):
            raise ValueError

    return result
