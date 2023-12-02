from gendiff import generate_diff
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json


FIXTURES_PATH = 'tests/fixtures/recursive'


def test_example_files():
    
    json_1_path = f'{FIXTURES_PATH}/example_1.json'
    json_2_path = f'{FIXTURES_PATH}/example_2.json'
    
    yaml_1_path = f'{FIXTURES_PATH}/example_1.yaml'
    yaml_2_path = f'{FIXTURES_PATH}/example_2.yaml'
    
    result_path_stylish = f'{FIXTURES_PATH}/example_result'
    with open(result_path_stylish) as file:
      result_stylish = file.read()
      
    result_path_plain = f'{FIXTURES_PATH}/example_result_plain'
    with open(result_path_plain) as file:
      result_plain = file.read()
    
    assert generate_diff(json_1_path, json_2_path, stylish) == result_stylish
    assert generate_diff(yaml_1_path, yaml_2_path, stylish) == result_stylish
    
    assert generate_diff(json_1_path, json_2_path, plain) == result_plain
    
    with open(f'{FIXTURES_PATH}/example_result_plain') as file:
        result_json = file.read()
    assert generate_diff(json_1_path, json_2_path, json) == result_json
