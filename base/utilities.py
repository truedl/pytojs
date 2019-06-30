from __future__ import annotations
from .exceptions import *
from .defaults import *
import re


class Validate:

    @staticmethod
    def valid_arguments(argv: list, endpoint) -> None:
        if len(argv) > 1:
            if '.py' in argv[1]:
                endpoint(argv[1])
            else:
                raise InvalidFileFormat('Only "py" file format is supported.')
        else:
            raise FileArgumentIsMissingError('File argument is missing.')

    @staticmethod
    def valid_variable(line: str) -> bool:
        if re.search(r'(.*)=(.*)', line):
            return True
        return False

    @staticmethod
    def valid_function(line: str) -> bool:
        if re.search(r'(.*)\((.*)\)', line):
            return True
        return False

    @staticmethod
    def valid_if(line: str) -> bool:
        if re.search(r'^if[ (](.*):$', line):
            return True
        return False

    @staticmethod
    def starts_with_tab(line: str) -> bool:
        if line[0] == ' ':
            return True
        return False

class Defaults:

    @staticmethod
    def functions(line: str) -> str:
        for func in default_functions:
            if func in line:
                return line.replace(func, default_functions[func], 1)

    @staticmethod
    def keywords(line: str) -> str:
        for keyword in default_keywords:
            if keyword in line:
                line = line.replace(keyword, default_keywords[keyword])

        return line


class Utilities:
    def __init__(self) -> None:
        self.validate = Validate()
        self.defaults = Defaults()

    @staticmethod
    def write_output(filename: str, output: list) -> None:
        with open(f'{filename}.js', 'w') as f:
            for line in output:
                f.write(line)
            f.close()

    @staticmethod
    def count_tabs(line:str, tab_spaces: int) -> int:
        if re.search(r'^ +', line):
            return int(len(re.findall(r'^ +', line)[0])/tab_spaces)
        return 0


utilities = Utilities()
