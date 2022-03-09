from itertools import permutations
import numpy as np


def get_input():
    lst = []
    while True:
        N = int(input())
        if N == 0: break

        temp = list(map(int, input().split(' ')))
        lst.append(temp)
    return lst

def get_diff(lst):
    max_diff = []
    A, B = 0, 0

    for i in range(len(lst)):
        temp = []
        for x in range(len(lst[0])):
            if x % 2 == 0: A += lst[i][x]
            else: B += lst[i][x]

            temp.append(abs(A-B))
        max_diff.append(max(temp))
        A, B = 0, 0

    return max_diff.index(min(max_diff))

def main():
    packages = get_input()
    maximal_diff = []

    for i in range(len(packages)):
        temp = packages[i].copy()
        perms = [a for a in permutations(temp, len(temp))]
        maximal_diff.append(perms[get_diff(perms)])

    for i in range(len(maximal_diff)):
        str = ''
        for j in range(len(maximal_diff[i])):
            str+= f"{maximal_diff[i][j]}-A " if j%2==0 else f"{maximal_diff[i][j]}-B "
        print(str)

if __name__=="__main__":
    main()  