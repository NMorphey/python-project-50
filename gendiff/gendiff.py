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
    if file_extension == 'json':
        with open(file_path) as file:
            return loads(file.read(), parse_constant=True)
    elif file_extension == 'yaml':
        with open(file_path) as file:
            return safe_load(file.read())
    raise ValueError(f"Incorrect file extension: (.{file_extension})")


def generate_diff(file_path_1, file_path_2) -> str:
    data_1 = collect_data(file_path_1)
    data_2 = collect_data(file_path_2)
    all_keys = set(data_1.keys()) | set(data_2.keys())
    all_keys_sorted = sorted(list(all_keys))

    changes = []
    for key in all_keys_sorted:
        key_in_data_1 = key in data_1
        key_in_data_2 = key in data_2
        if key_in_data_1:
            if key_in_data_2:
                data_1_value = data_1[key]
                data_2_value = data_2[key]
                if data_1_value == data_2_value:
                    changes.append(('remained', key, data_1_value))
                else:
                    changes.append(('removed', key, data_1_value))
                    changes.append(('added', key, data_2_value))
            else:
                changes.append(('removed', key, data_1[key]))
        else:
            changes.append(('added', key, data_2[key]))
            #  If there's no key in JSON 1, then
            #  the only way it appeared in all_keys - it IS in JSON 2

    result = '{\n'
    for ident, key, value in changes:
        value = remove_incorrectly_parsable(value)
        result += f'{IDENTS[ident]}{key}: {value}\n'
    result += '}'

    return result
