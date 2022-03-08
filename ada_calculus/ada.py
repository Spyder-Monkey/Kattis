import sys

def compute_diff(lst, exp, next):
    if all(i==lst[0] for i in lst):
        return exp, next

    new_lst = []
    for i in range(len(lst)-1):
        new_lst.append(lst[i+1]-lst[i])

    return compute_diff(new_lst, exp+1, next+new_lst[-1])

def main():
    # path = sys.argv[1]
    # with open(rf"{path}") as file:
    #     user_input = file.readline()

    user_input = list(map(int, input().split()))

    poly_lst = user_input[1:]
    exp, next = compute_diff(poly_lst, 0, poly_lst[-1])

    print(exp, next)



if __name__=="__main__":
    main()