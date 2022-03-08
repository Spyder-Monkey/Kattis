def check_line(lst):
    change_x = lst[1][0] - lst[0][0]
    change_y = lst[1][1] - lst[0][1]

    x_change_n, y_change_n = 0, 0
    for i in range(2, len(lst)):
        x_change_n = lst[i][0] - lst[i-1][0]
        y_change_n = lst[i][1] - lst[i-1][1]

        if (change_x * y_change_n) != (change_y * x_change_n):
            return False
    return True

def get_input():
    n = int(input())
    coords = []
    for _ in range(n):
        line = input().split(' ')
        x, y = int(line[0]), int(line[1])
        coords.append((x, y))

    return coords

def main():
    coords = get_input()
    if len(coords) <= 4:
        print("success")

    found = False

    # Go through and check each slope for each coord
    # Must be a straight line
    # Only have 2 shots, need to find two lines AT MOST
    # A single line is acceptable
    

    print(check_line(coords))

if __name__=="__main__":
    main()