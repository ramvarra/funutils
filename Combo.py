# Author: Ram Varra
# Description: Find subset integers that can generate all values in an integer sequence
import itertools

def test(s, n):
    combos = dict()
    for sn in range(1, len(s)+1):
        for subl in itertools.combinations(s, sn):
            total = sum(subl)
            if total <= n and total not in combos:
                combos[total] = list(subl)
    if len(combos) == n:
        return combos
    return None

def find_solution(R, N):
    for solution in itertools.combinations(range(1, R + 1), N):
        combos = test(solution, R)
        if combos:
            print("Solution = {}".format(",".join(str(i) for i in solution)))
            for k, v in combos.items():
                print('{:2d} = {}'.format(k, '+'.join(str(i) for i in v)))
            return True
    else:
        print ('Not Found')        
        return False


R = 31   # integer sequence size
N = 5    # size of set needed to produce 1 .. R integers
find_solution(R, N)




