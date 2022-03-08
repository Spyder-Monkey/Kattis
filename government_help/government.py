
# Take the smallest difference between A and B
def maximal_diff(lst):
    if all(element == lst[0] for element in lst):
        return lst

    packs = lst.copy()
    
    A = packs.pop(packs.index(min(packs)))
    B = packs.pop(packs.index(max(packs)))

    print(A - B)
    print(packs)


def main():
    packages = []

    while True:
        N = int(input())
        if N == 0: break
        package = list(map(int, input().split(' ')))
        packages.append(package)


    for i in packages:
        maximal_diff(i)

    print(packages)

if __name__=="__main__":
    main()