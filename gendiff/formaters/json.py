from json import dumps

from gendiff.dataset import get_name, get_children, get_change, get_value
from gendiff.dataset import has_children
from gendiff.dataset import REMOVED, ADDED


def parse_name(name, change):
    if change == REMOVED:
        return f'- {name}'
    elif change == ADDED:
        return f'+ {name}'
    return name


def parse_dataset(dataset):
    if has_children(dataset):
        children = sorted(get_children(dataset), key=get_name)
        return {
            parse_name(get_name(child), get_change(child)): parse_dataset(child)
            for child in children
        }
    return get_value(dataset)


def json(dataset):
    result = parse_dataset(dataset)
    return dumps(result, separators=(',', ':'))
