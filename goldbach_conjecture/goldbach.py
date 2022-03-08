import sys
import math

def prime_sieve(limit):
    prime = [True] * limit
    prime[0] = prime[1] = False

    for i, is_prime in enumerate(prime):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                prime[n] = False

def prime_nums():
    return list(prime_sieve(32000))

def goldbach(num):
    p=2
    limit = math.floor(num/2)
    for p in primes:
        q = num - p
        if p > q:
            break
        if q in primes:
            out.extend([p,q])
    print(f'{num} has {round(len(out)/2)} representation(s)')
    for i,j in zip(out[0::2], out[1::2]):
        print(f'{i}+{j}')
    
    print()


primes = prime_nums()
if __name__=="__main__":
    # with open('samples/goldbach.in') as file:
    #     lines = file.read().splitlines()

    lines = sys.stdin.read().splitlines()
    lines = list(map(lambda x: int(x), lines))
    even_nums = lines[1:]
    out = []

    for num in even_nums:
        goldbach(num)
        out = []
    

