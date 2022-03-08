import sys

def fill_options(n):
    lst = [[0] * n for _ in range(n)]
    options = []
    for i in range(n):
        options.append(input().split(', '))
        for j in range(i):
            d = sum(a != b for a, b in zip(options[i], options[j]))
            lst[i][j] = d
            lst[j][i] = d
    return lst, options

def find_best(options):
    least, least_i = sys.maxsize, []
    for i, row in enumerate(options):
        s = max(row)
        if s == least:
            least_i.append(i)
        elif s < least:
            least_i = [i]
            least = s
    return least_i

def main():
    input()
    n = int(input())
    lst, options = fill_options(n)
    best = find_best(lst)
    print('\n'.join((', '.join(options[i]) for i in best)))

if __name__=="__main__":
    main()