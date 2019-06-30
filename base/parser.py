from __future__ import annotations
from .utilities import utilities
import re


class Parser:
    def __init__(self) -> None:
        self.output = []
        self.tab_bumps = 0
        self.tab_loop = False
        self.tab = '\t'
        self.tab_spaces = 4

    def one_line(self, __line: str, refresh: bool=False) -> None:
        self.line = __line

        if utilities.count_tabs(self.line, self.tab_spaces) and self.tab_bumps:
            if utilities.count_tabs(self.line, self.tab_spaces) > self.tab_bumps:
                self.tabbump()
                self.one_line(self.line.strip(), True)
            else:
                self.one_line(self.line.strip(), True)
            return None

        if not refresh and not utilities.count_tabs(self.line, self.tab_spaces) and self.tab_bumps:
            for i in range(self.tab_bumps):
                self.tabdownbump()
                self.add_line('}')
        elif not refresh and utilities.count_tabs(self.line, self.tab_spaces) < self.tab_bumps:
            self.tabdownbump()
            self.add_line('}')

        if utilities.validate.valid_if(self.line):
            self.update_line(utilities.defaults.keywords(self.line))
            params = re.findall(r'[( ](.*)[:)]', self.line)[0]
            self.add_line(f'if({params})'+'{')
            return self.tabbump()

        elif utilities.validate.valid_function(self.line):
            self.update_line(utilities.defaults.functions(self.line))
            return self.add_line(f'{self.line};')

        elif utilities.validate.valid_variable(self.line):
            return self.add_line(f'var {self.line};')

    def add_line(self, __line: str) -> None:
        if self.tab_bumps:
            self.output.append(f'{self.tab*self.tab_bumps}{__line}\n')
        else:
            self.output.append(f'{__line}\n')

    def update_line(self, new: str) -> None:
        self.line = new

    def tabbump(self) -> None:
        self.tab_bumps += 1

    def tabdownbump(self) -> None:
        self.tab_bumps -= 1

    def clearbumps(self) -> None:
        self.tab_bumps = 0


parse = Parser()
