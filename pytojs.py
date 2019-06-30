from __future__ import annotations
from base.utilities import utilities
from base.parser import parse
import sys


class PyToJs:
    def __init__(self, __file) -> None:
        self.file = __file
        self.filename = __file.split('.')[0]
        with open(self.file, 'r') as f:
            for line in [x for x in f.read().split('\n') if x]:
                parse.one_line(line)
        utilities.write_output(self.filename, parse.output)


if __name__ == '__main__':
    utilities.validate.valid_arguments(sys.argv, PyToJs)
