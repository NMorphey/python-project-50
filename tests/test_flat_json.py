from gendiff import generate_diff


def test_example_files():
    json_1 = 'tests/fixtures/flat_json/example_files_1.json'
    json_2 = 'tests/fixtures/flat_json/example_files_2.json'
    result = 'tests/fixtures/flat_json/example_files_result'
    assert generate_diff(json_1, json_2) == result
    