from json import loads, dumps


IDENTS = {
    'removed': '  - ',
    'added': '  + ',
    'remained': '    '
}


INCORRENT_PARSABLE_CONSTANTS = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def generate_diff(file_path_1, file_path_2) -> str:
    with open(file_path_1) as file_1:
        json_1 = loads(file_1.read(), parse_constant=True)
    with open(file_path_2) as file_2:
        json_2 = loads(file_2.read(), parse_constant=True)
    all_keys = set(json_1.keys()) | set(json_2.keys())
    all_keys_sorted = sorted(list(all_keys))
    
    changes = []
    for key in all_keys_sorted:
        key_in_json_1 = key in json_1
        key_in_json_2 = key in json_2
        if key_in_json_1 and not key_in_json_2:
            changes.append( ('removed', key, json_1[key]) )
        elif key_in_json_2 and not key_in_json_1:
            changes.append( ('added', key, json_2[key]) )
        elif key_in_json_1 and key_in_json_2:
            json_1_value = json_1[key]
            json_2_value = json_2[key]
            if json_1_value == json_2_value:
                changes.append( ('remained', key, json_1_value) )
            else:
                changes.append( ('removed', key, json_1_value) )
                changes.append( ('added', key, json_2_value) )
    
    result = '{\n'
    for ident, key, value in changes:
        if value in INCORRENT_PARSABLE_CONSTANTS:
            value = INCORRENT_PARSABLE_CONSTANTS[value]
        result += f'{IDENTS[ident]}{key}: {value}\n'
    result += '}'
    
    return result
