import os
import math
from pathlib import Path
#########################################

def distance(a, b):
    return abs(a[0]-b[0])*abs(a[0]-b[0]) + abs(a[1]-b[1])*abs(a[1]-b[1]) + abs(a[2]-b[2])*abs(a[2]-b[2])

class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def print_boxes(self):
        print('Boxes: total', sum([len(a) for a in self.boxes]))
        for b in self.boxes:
            print(len(b), ':', b)

    def merge_closest(self):
        min_d, min_a, min_b = math.inf, 0, 1
        for i in range(len(self.boxes)):
            for j in range(i+1, len(self.boxes)):
                for bi in self.boxes[i]:
                    for bj in self.boxes[j]:
                        if min_d > distance(bi, bj):
                            min_d = distance(bi, bj)
                            min_a = i
                            min_b = j
        self.boxes[min_a].extend(self.boxes[min_b])
        self.boxes.pop(min_b)

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.CYCLES = 1000
            self.BIGGEST_BOXES = 3
            self.boxes = []
            for l in self.lines:
                if l == '':
                    break
                self.boxes.append([[int(a) for a in l.split(',')]])
            self.print_boxes()
            for i in range(self.CYCLES):
                if i%100 == 0:
                    print(i)
                self.merge_closest()
            self.print_boxes()
            print(sorted([len(a) for a in self.boxes], reverse=True))
            print(sorted([len(a) for a in self.boxes], reverse=True)[:3])
            res = math.prod(sorted([len(a) for a in self.boxes], reverse=True)[:3])
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
