import os
from pathlib import Path
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def count_adjacent(self, r, c):
        total = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if not (dr==0 and dc==0):
                    if -1 < dr+r < self.R and -1 < dc+c < self.C and self.grid[dr+r][dc+c] == '@':
                        total += 1
        return total

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.grid = f.read().split("\n")
            self.grid = self.grid[:-1]
            print(self.grid)
            self.R = len(self.grid)
            self.C = len(self.grid[0])
            res = 0
            for r in range(self.R):
                for c in range(self.C):
                    if self.grid[r][c] == '@' and self.count_adjacent(r, c) < 4:
                        print('r:', r, 'c:', c, 'adjacent:', self.count_adjacent(r, c))
                        res += 1
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
