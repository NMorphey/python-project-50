from gendiff import generate_diff
from gendiff.formaters.stylish import stylish


FIXTURES_PATH = 'tests/fixtures/flat_yaml'


def test_empty():
    yaml_path = f'{FIXTURES_PATH}/empty.yaml'
    result_path = f'{FIXTURES_PATH}/empty_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(yaml_path, yaml_path, stylish) == result

def test_strings_format():
    yaml_1_path = f'{FIXTURES_PATH}/strings_format_1.yaml'
    yaml_2_path = f'{FIXTURES_PATH}/strings_format_2.yaml'
    result_path = f'{FIXTURES_PATH}/any_format_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(yaml_1_path, yaml_2_path, stylish) == result

def test_strings_format():
    yaml_1_path = f'{FIXTURES_PATH}/one_line_format_1.yaml'
    yaml_2_path = f'{FIXTURES_PATH}/one_line_format_2.yaml'
    result_path = f'{FIXTURES_PATH}/any_format_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(yaml_1_path, yaml_2_path, stylish) == result

def test_similar():
    yaml_path = f'{FIXTURES_PATH}/strings_format_1.yaml'
    result_path = f'{FIXTURES_PATH}/similar_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(yaml_path, yaml_path, stylish) == result
