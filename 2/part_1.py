import os
import sys
import copy
from pathlib import Path
#########################################
class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def is_doubled(self, n: int):
        s = str(n)
        if len(s)%2 == 1:
            return False
        return s[:len(s)//2] == s[len(s)//2:]

    # Defining main function
    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            lines = f.read().split("\n")
            print(lines)
            res = 0
            for iter in lines[0].split(','):
                s, e = [int(a) for a in iter.split('-')]
                print('s:', s, 'e:', e)
                for n in range(s, e+1):
                    if self.is_doubled(n):
                        print(n)
                        res += n
            print('result:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
