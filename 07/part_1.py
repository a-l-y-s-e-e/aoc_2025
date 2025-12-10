import os
from pathlib import Path
from itertools import groupby
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            lines = f.read().split("\n")
            lines = [list(l) for l in lines]
            res = 0
            for i in range(1, len(lines)):
                for j in range(len(lines[i])):
                    if lines[i-1][j] in ['|', 'S']:
                        if lines[i][j] == '^':
                            res += 1
                            if j > 0:
                                lines[i][j-1] = '|'
                            if j < len(lines[i]) - 1:
                                lines[i][j+1] = '|'
                        else:
                            lines[i][j] = '|'
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
