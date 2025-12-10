import os
from pathlib import Path
from itertools import groupby
from collections import deque
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def check_perimeter(self, a, b):
        for i in range(min(a[0], b[0]), max(a[0], b[0])):
            if self.grid[i][a[1]] not in ['#', 'X']:
                return False
            if self.grid[i][b[1]] not in ['#', 'X']:
                return False
        for i in range(min(a[1], b[1]), max(a[1], b[1])):
            if self.grid[a[0]][i] not in ['#', 'X']:
                return False
            if self.grid[b[0]][i] not in ['#', 'X']:
                return False
        return True

    def get_area(self, a, b):
        if self.check_perimeter(a, b):
            return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
        return 0

    def create_grid(self):
        self.R = max([int(a[0]) for a in self.lights]) + 1
        self.C = max([int(a[1]) for a in self.lights]) + 1
        print('R:', self.R, 'C:', self.C)
        self.grid = []
        for i in range(self.R):
            self.grid.append(['.'] * self.C)
        for i in range(len(self.lights)):
            l = self.lights[i]
            self.grid[l[0]][l[1]] = '#'
            for j in range(i+1, len(self.lights)):
                l2 = self.lights[j]
                if l[0] == l2[0]:
                    for k in range(min(l[1], l2[1]) + 1, max(l[1], l2[1])):
                        self.grid[l[0]][k] = 'X'
                if l[1] == l2[1]:
                    for k in range(min(l[0], l2[0]) + 1, max(l[0], l2[0])):
                        self.grid[k][l[1]] = 'X'
        self.color_outside()
        self.color_inside()

    def color_outside(self):
        print('Coloring outside')
        q = deque()
        q.append([0,0])
        while len(q) > 0:
            P = q.popleft()
            if self.grid[P[0]][P[1]] != ' ':
                self.grid[P[0]][P[1]] = ' '
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i == 0 and j == 0):
                            p = [P[0]+i, P[1]+j]
                            if -1 < p[0] < self.R and -1 < p[1] < self.C and self.grid[p[0]][p[1]] not in ['#', 'X', ' ']:
                                q.append(p)

    def color_inside(self):
        print('Coloring inside')
        for i in range(self.R):
            for j in range(self.C):
                if self.grid[i][j] == '.':
                    self.grid[i][j] = 'X'

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.lights = []
            for l in self.lines:
                if l == '':
                    break
                self.lights.append([int(a) for a in l.split(',')])
            self.create_grid()
            print('grid created')
            res = 0
            for i in range(len(self.lights)):
                for j in range(i+1, len(self.lights)):
                    res = max(res, self.get_area(self.lights[i], self.lights[j]))
            print('-------------\nResult:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
