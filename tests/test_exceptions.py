import pytest

from gendiff import generate_diff


def test_incorrect_extension():
    with pytest.raises(ValueError):
        assert generate_diff('file.error', 'file.json', 'stylish')
    with pytest.raises(ValueError):
        assert generate_diff('json', 'yaml', 'stylish')
