def make_move(n, ai_turn):
    if n in (97, 98):
        new_n = 99 - n
    elif n % 3 == 0:
        new_n = 2 - int(ai_turn)
    elif (n+1) % 3 == 0:
        new_n = 1
    else:
        new_n = 2
    return new_n


if __name__=="__main__":
    n = 0
    my_turn = True
    ai_turn = False

    while n < 99:
        if my_turn:
            n+=make_move(n, ai_turn)
            print(n, flush=True)
            ai_turn = not ai_turn
        else:
            n = int(input())
        my_turn = not my_turn
