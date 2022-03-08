import sys

def get_coast(lst):
    counter = 0

    unvisted = {(0,0)}

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while unvisted:
        y_pos, x_pos = unvisted.pop()
        lst[y_pos][x_pos] = 2
        for offset in offsets:
            target = (y_pos + offset[0], x_pos + offset[1])

            if not 0 <= target[0] < len(lst) or not 0 <= target[1] < len(lst[0]):
                continue
            else:
                if lst[target[0]][target[1]] == 0 \
                    and (target[0], target[1]) not in unvisted:
                    unvisted.add((target[0], target[1]))
                elif lst[target[0]][target[1]] == 1:
                    counter += 1
    return counter


if __name__=="__main__":
    # with open('samples/coast-sample-1.in') as file:
    #     input = file.read().splitlines()

    user_input = input()
    input_lst = user_input.split(' ')

    rows = int(input_lst[0]) + 2
    cols = int(input_lst[1]) + 2

    coast_map = [[0] * cols]

    for count in range(1, rows-1):
        curr_input = input()

        curr_row = [0]
        curr_row.extend(list(curr_input))
        curr_row = [int(index) for index in curr_row]
        curr_row.append(0)

        coast_map.append(curr_row)
    coast_map.append([0]*cols)

    print(get_coast(coast_map))

    # print(get_coast(input[1:]))