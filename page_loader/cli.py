import argparse
import os


def parse_input():
    parser = argparse.ArgumentParser(
        description='TODO'
    )

    parser.add_argument(
        'url',
        type=str,
    )

    parser.add_argument(
        '-o', '--output',
        help='TODO',
        default=os.getcwd(),
    )
    args = parser.parse_args()

    return args
