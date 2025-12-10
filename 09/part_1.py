import os
from pathlib import Path
from itertools import groupby
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def get_area(self, a, b):
        return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.lights = []
            for l in self.lines:
                if l == '':
                    break
                self.lights.append([int(a) for a in l.split(',')])
            res = 0
            for i in range(len(self.lights)):
                for j in range(i+1, len(self.lights)):
                    res = max(res, self.get_area(self.lights[i], self.lights[j]))
            print('-------------\nResult:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
