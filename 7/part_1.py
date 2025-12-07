import os
from pathlib import Path
from itertools import groupby
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.fresh = []
            tmp = []
            for k, g in groupby(self.lines, lambda x: x == ''):
                if not k:
                    tmp.append(list(g))
            for l in tmp[0]:
                s, e = l.split('-')
                self.fresh.append([int(s), int(e)])
            print('fresh ids:', self.fresh)
            res = 0
            for l in [int(l) for l in tmp[1]]:
                for i in self.fresh:
                    if i[0] <= l <= i[1]:
                        res += 1
                        break
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
