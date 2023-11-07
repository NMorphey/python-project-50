from gendiff.gendiff import generate_diff


FILE_1_JSON_NAME = 'file1.json'
FILE_2_JSON_NAME = 'file2.json'


def test_example_files_comparision():
    assert generate_diff(FILE_1_JSON_NAME, FILE_2_JSON_NAME) == (
        """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    )
    