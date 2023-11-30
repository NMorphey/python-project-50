from copy import deepcopy


REMOVED = 'removed'
ADDED = 'added'


def create_dataset(*, name=None, data={}, value=None, change=None):
    dataset = {
        'name': name,
        'children': [],
        'value': value,
        'change': change
    }

    if isinstance(data, dict):  # Also true by default (in cases w/o any data)
        for key in data.keys():
            dataset['children'].append(create_dataset(
                name=key,
                data=data[key]
            ))
    else:
        dataset['value'] = data

    return dataset


def get_name(dataset):
    return dataset['name']


def has_children(dataset):
    return bool(dataset['children'])


def get_children(dataset):
    return dataset['children']


def get_change(dataset):
    return dataset['change']


def get_value(dataset):
    return dataset['value']


def is_dataset(var):
    if not isinstance(var, dict):
        return False
    if list(var.keys()) != ['name', 'children', 'change']:
        return False
    return True


def has_subtrees(dataset):
    children = get_children(dataset)
    if not children:
        return False
    for child in children:
        if is_dataset(child):
            return True
    return False


def copy_dataset(dataset):
    return deepcopy(dataset)


def set_value(dataset, value) -> None:
    dataset['value'] = value


def add_child(dataset, child) -> None:
    dataset['children'].append(child)


def set_change(dataset, change) -> None:
    dataset['change'] = change


def compare_datasets(dataset_1, dataset_2, *, name=None):
    result_dataset = create_dataset(name=name)
    dataset_1_has_children = has_children(dataset_1)
    dataset_2_has_children = has_children(dataset_2)

    if dataset_1 == dataset_2:
        return dataset_1

    match dataset_1_has_children, dataset_2_has_children:

        case False, False:
            if dataset_1 == dataset_2:
                add_child(result_dataset, copy_dataset(dataset_1))
            else:
                dataset_1_copy = copy_dataset(dataset_1)  # WET?
                dataset_2_copy = copy_dataset(dataset_2)
                set_change(dataset_1_copy, REMOVED)
                set_change(dataset_2_copy, ADDED)
                add_child(result_dataset, dataset_1_copy)
                add_child(result_dataset, dataset_2_copy)

        case True, False:
            dataset_1_copy = copy_dataset(dataset_1)  # WET?
            if get_name(dataset_2) is None:
                for child in get_children(dataset_1_copy):
                    set_change(child, REMOVED)
                return dataset_1_copy
            dataset_2_copy = copy_dataset(dataset_2)
            set_change(dataset_1_copy, REMOVED)
            set_change(dataset_2_copy, ADDED)
            add_child(result_dataset, dataset_1_copy)
            add_child(result_dataset, dataset_2_copy)

        case False, True:
            dataset_2_copy = copy_dataset(dataset_2)  # WET?
            if get_name(dataset_1) is None:
                for child in get_children(dataset_2_copy):
                    set_change(child, ADDED)
                return dataset_2_copy
            dataset_1_copy = copy_dataset(dataset_1)
            set_change(dataset_1_copy, REMOVED)
            set_change(dataset_2_copy, ADDED)
            add_child(result_dataset, dataset_1_copy)
            add_child(result_dataset, dataset_2_copy)

        case True, True:
            children_1 = {get_name(child): child
                          for child in get_children(dataset_1)}
            children_2 = {get_name(child): child
                          for child in get_children(dataset_2)}
            removed_keys = set(children_1) - set(children_2)
            remained_keys = set(children_1) & set(children_2)
            added_keys = set(children_2) - set(children_1)

            for key in removed_keys:
                removed_dataset = copy_dataset(children_1[key])
                set_change(removed_dataset, REMOVED)
                add_child(result_dataset, removed_dataset)

            for key in added_keys:
                added_dataset = copy_dataset(children_2[key])
                set_change(added_dataset, ADDED)
                add_child(result_dataset, added_dataset)

            for key in remained_keys:
                child_1 = children_1[key]
                child_2 = children_2[key]
                if child_1 == child_2:
                    add_child(result_dataset, child_1)
                elif not (has_children(child_1) and has_children(child_2)):
                    comparing = compare_datasets(child_1, child_2, name=key)
                    for child in get_children(comparing):
                        add_child(result_dataset, child)
                else:
                    branch = create_dataset(name=get_name(child_1))
                    comparing = compare_datasets(child_1, child_2, name=key)
                    for child in get_children(comparing):
                        add_child(branch, child)
                    add_child(result_dataset, branch)

    return result_dataset
