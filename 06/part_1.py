import os
from pathlib import Path
from itertools import groupby, product
import math
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            for i in range(len(self.lines)):
                l = self.lines[i]
                l = l.split(' ')
                l = [i for i in l if i != '']
                self.lines[i] = l
            for l in self.lines:
                print(len(l))
            res = 0
            for i in range(len(self.lines[0])):
                res += eval(
                    self.lines[-2][i].join([self.lines[j][i] for j in range(len(self.lines)-2)]
                ))
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
