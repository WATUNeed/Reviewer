from os import path as os_path


SCRIPT_PATH = os_path.dirname(os_path.realpath(__file__))

SETTINGS = {
    'csv_file': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['reviews', 'data.csv']),

    'csv_output_file': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['reviews', 'output_data.csv']),

    'csv_analyzed_file': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['reviews', 'data_analyzed.csv']),

    'logger_config': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['logger_config.json']),

    'test_csv_file': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['tests', 'tests_csv', 'test_data.csv']),

    'test_analytics_file': '\\'.join(SCRIPT_PATH.split(sep='\\')[:-1] + ['tests', 'tests_csv', 'test_analytics.csv']),

    'prompt':
        "You own a stress and heart rate variability tracking app::"
        "You need to identify the intonation of the review "
        "and Rate the user's review on a ten-point scale, where 10 is 'Most enthusiastic' and 1 is 'Most negative'::"
        "Do not explain your response::"
        "The answer should look like this: ['rating', 'intonation']::"
        "Review: ",

    'openai_api_key': 'OpenAI_API',

    'logger_init': 'Logger was initialized.',

    'try_connect': 'Try connect...',

    'api_key_received': 'API key successful received.',

    'result_received': 'Successfully received a response from CHATGPT.',

    'read_csv': 'Try to read CSV file...',

    'write_csv': 'Try to write CSV file...',

    'changes_write': 'The changes are written down.',

    'completed': 'Work in completed.'
}
