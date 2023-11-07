#!/usr/bin/env python3

import argparse

from gendiff.gendiff import generate_diff


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
    
    print(generate_diff(first_file_name, second_file_name))
    
if __name__ == '__main__':
    main()