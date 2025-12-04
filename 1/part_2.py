import os
from pathlib import Path
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            lines = f.read().split("\n")
            print(lines)
            res = 0
            p = 50
            mod = 100
            for l in lines:
                print('------')
                if l == '':
                    break
                d = l[0]
                n = int(l[1:])
                print('d', d, ' n', n)
                res += n//mod
                n = n%mod
                if d == 'L':
                    n = -n
                p = (p+n)
                if p-n!=0 and (p != p%mod or p == 0):
                    res += 1
                print('p', p, 'res', res)
                p = p%mod
            print('------')
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
