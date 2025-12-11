import os
from pathlib import Path
from collections import deque
#########################################

class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def count_total_paths(self):
        self.total_paths = 0
        q = deque()
        q.append('you')
        while not len(q) == 0:
            p = q.popleft()
            if p == 'out':
                self.total_paths += 1
            elif p in self.devices:
                for a in self.devices[p]:
                    q.append(a)

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.devices = {}
            for l in self.lines:
                self.devices[l[:3]] = l[5:].split(' ')
            self.count_total_paths()
            print('-------------\nResult:', self.total_paths)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
