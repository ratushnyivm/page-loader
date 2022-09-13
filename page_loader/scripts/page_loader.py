#!/usr/bin/env python


from page_loader.cli import parse_input
from page_loader.page_loader import download


def main():
    args = parse_input()
    print(download(args.url, args.output))


if __name__ == '__main__':
    main()
