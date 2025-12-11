import os
from pathlib import Path
from collections import deque
#########################################

class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def count_total_paths_dp(self, start, end):
        if start in self.dp:
            return self.dp[start]
        if start == end:
            return 1
        if start not in self.devices:
            return 0
        res = 0
        for a in self.devices[start]:
            res += self.count_total_paths_dp(a, end)
        self.dp[start] = res
        return res

    def count_total_paths(self, start, end):
        res = 0
        q = deque()
        q.append(start)
        while not len(q) == 0:
            p = q.popleft()
            if p == end:
                res += 1
            elif p in self.devices:
                for a in self.devices[p]:
                    q.append(a)
        return res

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            self.devices = {}
            for l in self.lines:
                self.devices[l[:3]] = l[5:].split(' ')
            # path svr->dac->fft->out
            self.dp = {}
            p1 = self.count_total_paths_dp('svr', 'dac')
            self.dp = {}
            p1 *= self.count_total_paths_dp('dac', 'fft')
            self.dp = {}
            p1 *= self.count_total_paths_dp('fft', 'out')
            # path svr->fft->dac->out
            self.dp = {}
            p2 = self.count_total_paths_dp('svr', 'fft')
            self.dp = {}
            p2 *= self.count_total_paths_dp('fft', 'dac')
            self.dp = {}
            p2 *= self.count_total_paths_dp('dac', 'out')
            print('-------------\nResult:', p1 + p2)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
