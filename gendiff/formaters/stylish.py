from gendiff.dataset import get_name, get_children, get_change, get_value
from gendiff.dataset import has_children
from gendiff.dataset import REMOVED, ADDED


IDENTS = {
    REMOVED: '- ',
    ADDED: '+ ',
    None: '  '
}

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


def stylish(dataset, depth=0) -> str:

    name = get_name(dataset)
    result = ''

    if has_children(dataset) or depth == 0:
        if depth > 0:
            result += f'{name}: '
        result += '{\n'
        children = get_children(dataset)
        for child in sorted(children, key=get_name):
            result += ' ' * (2 + 4 * depth)
            result += IDENTS[get_change(child)]
            result += stylish(child, depth + 1)
            result += '\n'
        result += (' ' * depth * 4) + '}'
    else:
        result = f'{name}: {remove_incorrectly_parsable(get_value(dataset))}'

    return result
