import argparse


def parse_input():
    parser = argparse.ArgumentParser(
        description='TODO'
    )

    parser.add_argument(
        'file_path',
        type=str,
    )

    parser.add_argument(
        '--output',
        help='TODO',
        # choices=[STYLISH, PLAIN, JSON],
        # default=STYLISH,
    )
    args = parser.parse_args()

    return args
