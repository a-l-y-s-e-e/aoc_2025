import copy
import sys
from pathlib import Path
import re
#########################################
def main():
    with (open('/Users/pchapon/projects/aoc/2025/3/input.txt') as f):
        lines = f.read().split("\n")
        print(lines)
        res = 0
        for l in lines:
            print('-----')
            if l == '':
                break
            print(l)
            max_l = l[0]
            max_l_i = 0
            for i in range(len(l)-1):
                if max_l < l[i]:
                    max_l = l[i]
                    max_l_i = i
            max_r = l[-1]
            max_r_i = len(l)-1
            for i in range(len(l)-2, max_l_i, -1):
                if max_r < l[i]:
                    max_r = l[i]
                    max_r_i = i
            print(max_l+max_r)
            res += int(max_l+max_r)
        print('result:', res)

#########################################
if __name__=="__main__":
    main()
