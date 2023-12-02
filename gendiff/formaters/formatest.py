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