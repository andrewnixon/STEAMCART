#! /usr/bin/python3
import argparse

from pathlib import Path
from sc_input import ip_parse

def setup():
    parser = argparse.ArgumentParser()

    parser.add_argument('input_file', help="Input file help")
    parser.add_argument('model', help="Model file help")
    parser.add_argument('-c', '--code', required=True, help="code: options topas or gate")
    parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")

    args = parser.parse_args()

    input_file = Path(args.input_file)
    model = Path(args.model)

    if not input_file.is_file():
        raise Exception("Input file is not file")

    if not model.is_file():
        raise Exception("Model does not point to a run file")

    if not (args.code == 'topas' or args.code == 'gate'):
        raise Exception("Code should be 'topas' or 'gate'")

    if args.verbose:
        print("Verbose not yet implemented")

    return {'input_file': args.input_file, 'model': args.model,
    'code': args.code, 'verbose': args.verbose}

if __name__ == '__main__':
    args = setup()

    ip_parse.hello()
