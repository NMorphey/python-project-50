#!/usr/bin/env python3

import argparse
from datetime import datetime

from gendiff.gendiff import generate_diff
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json import json


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    first_file_name = args.first_file
    second_file_name = args.second_file

    try:
        result = generate_diff(first_file_name, second_file_name, args.format)
        if args.format == 'json':
            filename = f'{datetime.today().strftime("%d%m%Y-%H%M")}-gendiff.json'
            with open(filename, 'w') as file:
                file.write(result)
        else:
            print(result)
    except Exception as e:
        print(f'An error occured: "{e.args[0]}"! See documentation.')

if __name__ == '__main__':
    main()
