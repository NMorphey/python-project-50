from gendiff import generate_diff
from gendiff.formaters.stylish import stylish


FIXTURES_PATH = 'tests/fixtures/flat_json'


def test_example_files():
    json_1_path = f'{FIXTURES_PATH}/example_files_1.json'
    json_2_path = f'{FIXTURES_PATH}/example_files_2.json'
    result_path = f'{FIXTURES_PATH}/example_files_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(json_1_path, json_2_path, stylish) == result

def test_empty():
    json_path = f'{FIXTURES_PATH}/empty.json'
    result_path = f'{FIXTURES_PATH}/empty_result'
    with open(result_path) as file:
        result = file.read()
    assert generate_diff(json_path, json_path, stylish) == result

def test_similar():
    json_path = f'{FIXTURES_PATH}/similar.json'
    result_path = f'{FIXTURES_PATH}/similar_result'
    with open(result_path) as file:
        result = file.read()
    assert generate_diff(json_path, json_path, stylish) == result

def test_empty_and_filled():
    json_1_path = f'{FIXTURES_PATH}/empty.json'
    json_2_path = f'{FIXTURES_PATH}/similar.json'
    result_path = f'{FIXTURES_PATH}/empty_and_filled_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(json_1_path, json_2_path, stylish) == result
