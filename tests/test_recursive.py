from gendiff import generate_diff


FIXTURES_PATH = 'tests/fixtures/flat_json'


def test_example_files():
    
    json_1_path = f'{FIXTURES_PATH}/example_1.json'
    json_2_path = f'{FIXTURES_PATH}/example_2.json'
    
    yaml_1_path = f'{FIXTURES_PATH}/example_1.yaml'
    yaml_2_path = f'{FIXTURES_PATH}/example_2.yaml'
    
    result_path = f'{FIXTURES_PATH}/example_result'
    with open(result_path) as file:
      result = file.read()
    
    assert generate_diff(json_1_path, json_2_path) == result
    assert generate_diff(yaml_1_path, yaml_2_path) == result
