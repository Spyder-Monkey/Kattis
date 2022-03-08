import math
from functools import reduce

def main():
    N = int(input())
    # Get the first list of products
    A = input()
    A = list(map(lambda x: int(x), A.split(' ')))
    # Get second list
    M = int(input())
    B = input()
    B = list(map(lambda x: int(x), B.split(' ')))

    prod1 = reduce(lambda x, y: x*y, A)
    prod2 = reduce(lambda x, y: x*y, B)

    print(str(math.gcd(prod1, prod2))[-9:])

if __name__=="__main__":
    main()