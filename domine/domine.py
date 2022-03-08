

def main():
    line = input().split(' ')
    rows = int(line[0])
    dominos = int(line[1])
    board = []

    for _ in range(rows):
        board.append(list(map(int, input().split(' '))))

    print(board)

if __name__=="__main__":
    main()