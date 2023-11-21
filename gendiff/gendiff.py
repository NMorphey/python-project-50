from json import loads
from yaml import safe_load


IDENTS = {
    'removed': '  - ',
    'added': '  + ',
    'remained': '    '
}


INCORRENTLY_PARSABLE_CONSTANTS = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def remove_incorrectly_parsable(value):
    if value in INCORRENTLY_PARSABLE_CONSTANTS:
        return INCORRENTLY_PARSABLE_CONSTANTS[value]
    return value


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


def compare_datasets(dataset_1, dataset_2):
    all_keys = set(dataset_1.keys()) | set(dataset_2.keys())
    all_keys_sorted = sorted(list(all_keys))

    changes = []
    for key in all_keys_sorted:
        key_in_dataset_1 = key in dataset_1
        key_in_dataset_2 = key in dataset_2
        if key_in_dataset_1:
            if key_in_dataset_2:
                data_1_value = dataset_1[key]
                data_2_value = dataset_2[key]
                if data_1_value == data_2_value:
                    changes.append(('remained', key, data_1_value))
                else:
                    changes.append(('removed', key, data_1_value))
                    changes.append(('added', key, data_2_value))
            else:
                changes.append(('removed', key, dataset_1[key]))
        else:
            changes.append(('added', key, dataset_2[key]))
            #  If there's no key in JSON 1, then
            #  the only way it appeared in all_keys - it IS in JSON 2
    
    return changes


def generate_diff(file_path_1, file_path_2) -> str:
    data_1 = collect_data(file_path_1)
    data_2 = collect_data(file_path_2)
    
    changes = compare_datasets(data_1, data_2)
    result = '{\n'
    for ident, key, value in changes:
        value = remove_incorrectly_parsable(value)
        result += f'{IDENTS[ident]}{key}: {value}\n'
    result += '}'

    return result
