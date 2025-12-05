import os
from pathlib import Path
from itertools import groupby
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def get_all_overlapping_interval(self, s, e):
        res = [[s, e]]
        for f in self.fresh:
            if f[0] <= s <= f[1] or f[0] <= e <= f[1] or s <= f[0] <= e or s <= f[1] <= e:
                res.append(f)
        return res

    def get_merged_interval(self, intervals):
        min_s, max_e = intervals[0]
        for i in intervals:
            min_s = min(i[0], min_s)
            max_e = max(i[1], max_e)
        return [min_s, max_e]

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.fresh = []
            tmp = []
            for k, g in groupby(self.lines, lambda x: x == ''):
                if not k:
                    tmp.append(list(g))
            for l in tmp[0]:
                print('------')
                s, e = [int(a) for a in l.split('-')]
                intervals = self.get_all_overlapping_interval(s, e)
                print(s, e, intervals)
                for i in intervals:
                    if i in self.fresh:
                        self.fresh.remove(i)
                self.fresh.append(self.get_merged_interval(intervals))
            print('fresh ids:', self.fresh)
            res = 0
            for i in self.fresh:
                res += i[1]-i[0]+1
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
