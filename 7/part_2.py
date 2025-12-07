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
            for i in range(len(lines[0])):
                if lines[0][i] == 'S':
                    lines[0][i] = 1
            for i in range(1, len(lines)):
                for j in range(len(lines[i])):
                    if isinstance(lines[i-1][j], int):
                        if lines[i][j] == '^':
                            if j > 0:
                                if not isinstance(lines[i][j-1], int):
                                    lines[i][j-1] = 0
                                lines[i][j-1] += lines[i-1][j]
                            if j < len(lines[i]) - 1:
                                if not isinstance(lines[i][j+1], int):
                                    lines[i][j+1] = 0
                                lines[i][j+1] += lines[i-1][j]
                        else:
                            if not isinstance(lines[i][j], int):
                                lines[i][j] = 0
                            lines[i][j] += lines[i-1][j]
            print('result:', sum([a for a in lines[-2] if isinstance(a, int)]))

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
