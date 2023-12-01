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


def parse_plain(dataset, path=[]):
    change = get_change(dataset)
    if change in [REMOVED, ADDED]:
        return {
            'path': path + [get_name(dataset)],
            'action': change,
            'value':
                '[complex value]' if has_children(dataset)
                else get_value(dataset)
        }
    elif has_children(dataset):
        result = []
        for child in get_children(dataset):
            result += parse_plain(child, path + get_name(dataset))
        return result
    return []
  

def plain(dataset):
    changes = parse_plain(dataset)
    for change in changes:
        change['path'] = '.'.join(change['path'])
    changes.sort(key=lambda x: x['path'])
