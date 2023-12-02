from json import loads
from yaml import safe_load

from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json
from gendiff.dataset import create_dataset, compare_datasets


def collect_data(file_path):
    file_extension = file_path.split('.')[-1].lower()
    value_error = ValueError(f"Incorrect file extension: (.{file_extension})")
    if file_path == file_extension:
        raise value_error
    if file_extension == 'json':
        with open(file_path) as file:
            return loads(file.read(), parse_constant=True)
    elif file_extension in ['yml', 'yaml']:
        with open(file_path) as file:
            decoded_result = safe_load(file.read())
            return decoded_result if decoded_result else {}
    raise value_error


def parse_dataset(dataset, formater):
    return formater(dataset)


def generate_diff(file_path_1, file_path_2, formater_name) -> str:
    
    if type(formater_name) == str:
        formater_name = formater_name.lower()
    
    match formater_name:
        case 'plain':
            formater = plain
        case 'json':
            formater = json
        case 'stylish':
            formater = stylish
        case None:
            formater = stylish
        case _:
            raise ValueError('Wrong formater')
        
    data_1 = collect_data(file_path_1)
    data_2 = collect_data(file_path_2)

    dataset_1 = create_dataset(data=data_1)
    dataset_2 = create_dataset(data=data_2)

    return parse_dataset(compare_datasets(dataset_1, dataset_2), formater)
