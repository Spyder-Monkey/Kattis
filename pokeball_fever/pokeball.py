"""
    Start with 100 pokeballs
    keep throwing pokeballs until:
        a. catch
        b. run out of pokeballs
    Each pokeball thrown has a P constant probability of success
    If catch on LAST pokeball -> don't refill until next encounter
"""

def main():
    line = input().split(' ')
    n = int(line[0])
    p = float(line[1])
    # ratio = p.as_integer_ratio()

    encounters = n
    pokeballs = 100
    spent = 0

    if p == 0.000:
        print('%.9f' % (n*5))
    elif p == 1.000:
        print("{0:.9f}".format(((int)(n/100)-1)*5))
    else:
        import random
        while encounters > 0:
            while pokeballs > 0:
                if random.random() <= p:
                    pokeballs -= 1
                    break

                # spent += (0.05 * (1 - (1-p)**pokeballs))
                spent += (5 * (p * (1-p)**pokeballs))
                print(spent)
                pokeballs -=1
            encounters-=1
            print("++++++++++++++")

            if pokeballs == 0:
                pokeballs = 100


        print("{0:.9f}".format(spent))



if __name__=="__main__":
    main()