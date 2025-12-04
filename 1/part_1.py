import copy
import sys
from pathlib import Path
import re
#########################################
def main():
    with (open('/Users/pchapon/projects/aoc/2025/1/input.txt') as f):
        lines = f.read().split("\n")
        print(lines)
        res = 0
        p = 50
        mod = 100
        for l in lines:
            if l == '':
                break
            d = l[0]
            n = int(l[1:])
            print(d, n)
            if d == 'L':
                n = -n
            p = (p+n)%mod
            if p == 0:
                res += 1
        print(res)

#########################################
if __name__=="__main__":
    main()
