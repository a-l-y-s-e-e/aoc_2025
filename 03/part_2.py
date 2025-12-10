import os
from pathlib import Path
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def get_max(self, l, iter):
        if iter <= 0:
            return ''
        max_l = l[0]
        max_l_i = 0
        for i in range(len(l)-iter+1):
            if max_l < l[i]:
                max_l = l[i]
                max_l_i = i
        return max_l + self.get_max(l[max_l_i+1:], iter-1)

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            lines = f.read().split("\n")
            print(lines)
            res = 0
            for l in lines:
                if l == '':
                    break
                m = int(self.get_max(l, 12))
                res += m
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
