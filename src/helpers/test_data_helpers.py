import json
import os


def get_test_data_from_json(test_data_file_name: str) -> list | dict:
    json_path = os.path.join(test_data_file_name)
    with open(json_path, "r", encoding='utf-8') as json_file:
        test_data = json.load(json_file)
    return test_data
