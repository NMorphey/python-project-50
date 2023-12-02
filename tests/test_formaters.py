from gendiff.dataset import create_dataset
from gendiff.formaters.stylish import stylish


def test_uncompared_datasets():
    data = {'key_1': {'key_3': 'value_3', 'key_2': 'value_2'}}
    dataset_1 = create_dataset(data=data)
    with open('tests/fixtures/stylish/result_1') as file:
        result_1 = file.read()
    assert stylish(dataset_1) == result_1


def test_empty_dataset():
    assert stylish(create_dataset()) == '{\n}'
