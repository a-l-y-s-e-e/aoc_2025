import os
from pathlib import Path
from itertools import groupby
#########################################
def parse_buttons(b_list: str):
    buttons = []
    for b in b_list:
        buttons.append([int(a) for a in b[1:-1].split(',')])
    return buttons

def swap_light(c):
    if c == '.':
        return '#'
    elif c == '#':
        return '.'
    return None

def press_button(button, state):
    for i in button:
        state[i] = swap_light(state[i])

class Sol:
    BASE_DIR = Path(__file__).parent.resolve()

    def find_solution(self, state: list, objective: list, buttons: list, i: int):
        if i < 0:
            return state == objective
        for b in buttons:
            press_button(b, state)
            if self.find_solution(state, objective, buttons, i-1):
                return True
            press_button(b, state)
        return False

    def get_min_pushes(self, objective, buttons):
        for i in range(10000000):
            if self.find_solution(['.']*len(objective), objective, buttons, i):
                return i+1
        return None

    def main(self):
        with (open(os.path.join(self.BASE_DIR, 'input.txt')) as f):
            self.lines = f.read().split("\n")
            res = 0
            for l in self.lines:
                if l == '':
                    break
                l = l.split(' ')
                res += self.get_min_pushes(list(l[0])[1:-1], parse_buttons(l[1:-1]))
            print('-------------\nResult:', res)

#########################################
if __name__=="__main__":
    sol = Sol()
    sol.main()
