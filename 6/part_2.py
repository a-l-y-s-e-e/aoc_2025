import os
from pathlib import Path
from itertools import groupby, product
import math
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def equalize_lengths(self):
        max_l = 0
        for l in self.lines:
            max_l = max(max_l, len(l))
        for i in range(len(self.lines)):
            for _ in range(max_l - len(self.lines[i])):
                self.lines[i] += ' '

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.lines = self.lines[:-1]
            self.equalize_lengths()
            operator = '+'
            values = ['0', ' ']
            res = 0
            for i in range(len(self.lines[0])):
                if self.lines[-1][i] != ' ':
                    res += eval(operator.join(values[:-1]))
                    operator = self.lines[-1][i]
                    values = []
                values.append(''.join([self.lines[j][i] for j in range(len(self.lines)-1)]))
            res += eval(operator.join(values))
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
