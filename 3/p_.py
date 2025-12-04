import copy
import sys
from pathlib import Path
import re
#########################################
def get_max(l, iter):
    if iter <= 0:
        return ''
    max_l = l[0]
    max_l_i = 0
    for i in range(len(l)-iter+1):
        if max_l < l[i]:
            max_l = l[i]
            max_l_i = i
    return max_l + get_max(l[max_l_i+1:], iter-1)

# Defining main function
def main():
    with (open('/Users/pchapon/projects/aoc/2025/3/input.txt') as f):
        lines = f.read().split("\n")
        print(lines)
        res = 0
        for l in lines:
            if l == '':
                break
            m = int(get_max(l, 12))
            res += m
        print('result:', res)

#########################################
if __name__=="__main__":
    main()
