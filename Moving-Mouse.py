mazepos="+---+---+---+---+---+---+---+---+|       |                       |+   +---+   +---+---+   +---+   +|   |           |   |   |       |+   +   +---+   +   +---+   +---+|       |   |   |               |+---+   +   +---+   +---+   +---+|       |   |       |   |   |   |+   +   +   +       +   +   +   +|   |       |       |   |   |   |+   +   +   +---+---+   +   +   +|   |   |                       |+   +   +---+---+---+---+   +   +|   |                   |   |   |+   +   +---+---+   +   +   +   +|   |           |   |       |   |+---+---+---+---+---+---+---+---+"


#maze width: 33 chars
#height: 17
curpos=497
# up 1 space: -66
# down 1 space: +66
# left 1 space: -4
# right 1 space: +4
while True:
    itr=0
    for i in range(17):
        for j in range(33):
            if curpos==itr:
                print("@",end="")
            else:
                print (list(mazepos)[itr],end="")
            itr=itr+1
        print("",itr-1,end="")
        print("")
    print("pos:",curpos)
    while True:
        move=input("Move which way? U/D/L/R (walls not yet functional, moving out of bounds causes issues) ")
        if move=="U":
            curpos=curpos-66
        elif move=="D":
            curpos=curpos+66
        elif move=="L":
            curpos=curpos-4
        elif move=="R":
            curpos=curpos+4
        else:
            print("ERROR: please choose from the list given.")
            continue
        if curpos<35:
            print("ERROR: out of bounds")
            if move=="U":
                curpos=curpos+66
            elif move=="D":
                curpos=curpos-66
            elif move=="L":
                curpos=curpos+4
            elif move=="R":
                curpos=curpos-4
            continue
        else:
            break
        
