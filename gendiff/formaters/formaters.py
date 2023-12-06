from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json


FORMATERS = {
    None: stylish,
    'stylish': stylish,
    'plain': plain,
    'json': json
}
