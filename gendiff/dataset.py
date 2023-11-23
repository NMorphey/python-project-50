from operator import or_
from functools import reduce


# INIT

def create_dataset(*, name='!root', data={}, change=None):
    dataset = {
        'name': name,
        'children': [],
        'change': change
    }
    
    if type(data) == dict:  # Also true by default i.e. in cases w/o any data
        for key in data.keys():
            dataset['children'].append(create_dataset(
                name=key,
                data=data[key]
            ))
    else:
        dataset['children'].append(data)
    
    return dataset


# GETTERS

def get_name(dataset):
    return dataset['name']

def get_children(dataset):
    return dataset['children']

def get_change(dataset):
    return dataset['change']

def has_subtrees(dataset):
    children = get_children(dataset)
    if not children:
        return False
    return reduce(or_, map(lambda child: get_children(child), children))
