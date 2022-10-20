#!/usr/bin/env python

import sys

from page_loader.cli import parse_input
from page_loader.loader import download, logger


def main():
    args = parse_input()

    try:
        print(download(args.url, args.output))
    except RuntimeError:
        logger.critical('crash!!!')
        sys.exit(1)


if __name__ == '__main__':
    main()
