import os
from pathlib import Path
from collections import deque
#########################################

class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.shapes = []
            self.trees = []
            i = 0
            while i < len(self.lines):
                l = self.lines[i]
                if l == '':
                    continue
                if len(l) == 2:
                    i += 1
                    b = self.lines[i:i+3]
                    n = sum([a.count('#') for a in b])
                    self.shapes.append([n, b])
                    i += 3
                else:
                    r, c = [int(a) for a in l.split(':')[0].split('x')]
                    s = [int(a) for a in l.split(':')[1].split(' ')[1:]]
                    self.trees.append([r, c, s])
                i += 1
            print(self.shapes)
            print(self.trees)
            res = 0
            for t in self.trees:
                s = 0
                for i in range(len(t[2])):
                    s += t[2][i] * self.shapes[i][0]
                if t[0] * t[1] < s:
                    print('Cant fit')
                elif t[0] * t[1] >= 9 * sum(t[2]):
                    print('obvious fit')
                    res += 1
                else:
                    print('##################################### NP hard here')
            print('-------------\nResult:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
