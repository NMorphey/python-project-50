from gendiff import generate_diff


def test_example_files():
    json_1_path = 'tests/fixtures/flat_json/example_files_1.json'
    json_2_path = 'tests/fixtures/flat_json/example_files_2.json'
    result_path = 'tests/fixtures/flat_json/example_files_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(json_1_path, json_2_path) == result
    