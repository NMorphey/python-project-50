import pytest

from gendiff.dataset import create_dataset
from gendiff.stylish import stylish


FIXTURES_PATH = 'tests/fixtures/stylish'


def test_uncompared_datasets():
    dataset_1 = create_dataset(
        data={'key_1':
        {'key_3': 'value_3',
         'key_2': 'value_2'}}
        )
    with open(f'{FIXTURES_PATH}/result_1') as file:
        result_1 = file.read()
    assert stylish(dataset_1) == result_1
