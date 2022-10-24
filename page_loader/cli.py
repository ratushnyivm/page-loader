import argparse
import os


def parse_input():
    parser = argparse.ArgumentParser(
        description='Downloads web-pages and save locally'
    )

    parser.add_argument(
        'url',
        type=str,
    )

    parser.add_argument(
        '-o', '--output',
        help='output dir (default: current directory)',
        default=os.getcwd(),
    )
    args = parser.parse_args()

    return args
