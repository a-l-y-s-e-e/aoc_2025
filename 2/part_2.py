import os
from pathlib import Path
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def is_doubled(self, n: int):
        s = str(n)
        for i in range(2, len(s)+1):
            if len(s)%i == 0:
                res = True
                c = 1
                while res and c*len(s)//i < len(s):
                    if s[:len(s)//i] != s[c*len(s)//i:(c+1)*len(s)//i]:
                        res = False
                    c += 1
                if res:
                    return True
        return False

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            lines = f.read().split("\n")
            print(lines)
            res = 0
            for iter in lines[0].split(','):
                s, e = [int(a) for a in iter.split('-')]
                #print('s:', s, 'e:', e)
                for n in range(s, e+1):
                    if self.is_doubled(n):
                        #print(n, 'is doubled')
                        res += n
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
