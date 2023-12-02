from collections import defaultdict

from gendiff.dataset import get_name, get_children, get_change, get_value
from gendiff.dataset import has_children
from gendiff.dataset import REMOVED, ADDED
from gendiff.formaters.formaters import remove_incorrectly_parsable
from gendiff.formaters.formaters import add_quotation_marks_if_needed


UPDATED = 'updated'


def parse_plain(dataset, path=[]):
    change = get_change(dataset)
    if change in [REMOVED, ADDED]:
        return [{
            'path': path,
            'action': change,
            'value':
                '[complex value]' if has_children(dataset)
                else get_value(dataset)
        }]
    elif has_children(dataset):
        result = []
        for child in get_children(dataset):
            result += parse_plain(child, path + [get_name(child)])
        return result
    return []


def get_modification_string(change):
    path = change['path']
    action = change['action']
    if action in [ADDED, REMOVED]:
        value = change['value']
        value = add_quotation_marks_if_needed(value)
        value = remove_incorrectly_parsable(value)

    # match-case isn't used due to "Irrefutable pattern is allowed ..." error

    if action == ADDED:
        return f"Property '{path}' was added with value: {value}"

    elif action == REMOVED:
        return f"Property '{path}' was removed"

    elif action == UPDATED:
        removed_value = change['removed_value']
        removed_value = add_quotation_marks_if_needed(removed_value)
        removed_value = remove_incorrectly_parsable(removed_value)

        added_value = change['added_value']
        added_value = add_quotation_marks_if_needed(added_value)
        added_value = remove_incorrectly_parsable(added_value)

        mid_text = 'was updated. From'
        return f"Property '{path}' {mid_text} {removed_value} to {added_value}"


def plain(dataset):
    changes = parse_plain(dataset)
    updated_paths = defaultdict(list)
    for change in changes:
        new_path = '.'.join(change['path'])
        updated_paths[new_path].append(change)
        change['path'] = new_path

    for path in updated_paths:
        updates = updated_paths[path]
        if len(updates) == 1:
            continue
        removed_value = list(filter(lambda x: x['action'] == REMOVED,
                                    updates))[0]['value']
        added_value = list(filter(lambda x: x['action'] == ADDED,
                                  updates))[0]['value']
        updated_paths[path] = [{
            'path': updates[0]['path'],
            'action': UPDATED,
            'removed_value': removed_value,
            'added_value': added_value
        }]
    changes = updated_paths.values()
    changes = list(map(lambda x: x[0], changes))
    changes = list(map(get_modification_string, changes))
    changes.sort()

    return '\n'.join(changes)
