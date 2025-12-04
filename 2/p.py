import copy
import sys
from pathlib import Path
import re
#########################################

def is_doubled(n: int):
    s = str(n)
    if len(s)%2 == 1:
        return False
    return s[:len(s)//2] == s[len(s)//2:]

# Defining main function
def main():
    with (open('/Users/pchapon/projects/aoc/2025/2/input.txt') as f):
        lines = f.read().split("\n")
        print(lines)
        res = 0
        for iter in lines[0].split(','):
            s, e = [int(a) for a in iter.split('-')]
            print('s:', s, 'e:', e)
            for n in range(s, e+1):
                if is_doubled(n):
                    print(n)
                    res += n
        print(res)




#########################################
if __name__=="__main__":
    main()
