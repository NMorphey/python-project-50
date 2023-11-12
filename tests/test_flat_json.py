from gendiff import generate_diff


def test_example_files():
    json_1_path = 'tests/fixtures/flat_json/example_files_1.json'
    json_2_path = 'tests/fixtures/flat_json/example_files_2.json'
    result_path = 'tests/fixtures/flat_json/example_files_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(json_1_path, json_2_path) == result

def test_empty():
    json_path = 'tests/fixtures/flat_json/empty.json'
    result_path = 'tests/fixtures/flat_json/empty_result'
    with open(result_path) as file:
        result = file.read()
    assert generate_diff(json_path, json_path) == result

def test_similar():
    json_path = 'tests/fixtures/flat_json/similar.json'
    result_path = 'tests/fixtures/flat_json/similar_result'
    with open(result_path) as file:
        result = file.read()
    assert generate_diff(json_path, json_path) == result

def test_empty_and_filled():
    json_1_path = 'tests/fixtures/flat_json/empty.json'
    json_2_path = 'tests/fixtures/flat_json/similar.json'
    result_path = 'tests/fixtures/flat_json/empty_and_filled_result'
    with open(result_path) as file:
      result = file.read()
    assert generate_diff(json_1_path, json_2_path) == result
