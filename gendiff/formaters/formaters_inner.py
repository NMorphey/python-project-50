INCORRENTLY_PARSABLE_CONSTANTS = {
    True: 'true',
    False: 'false',
    None: 'null'
}


def remove_incorrectly_parsable(value):
    for constant in INCORRENTLY_PARSABLE_CONSTANTS:
        if value is constant:
            return INCORRENTLY_PARSABLE_CONSTANTS[constant]
    return value


def add_quotation_marks_if_needed(value):
    if value in INCORRENTLY_PARSABLE_CONSTANTS.keys():
        return value
    if value != '[complex value]':
        return f"'{value}'"
    return value
