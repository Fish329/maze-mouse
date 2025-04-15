#The maze, crushed down into one string
mazepos="+---+---+---+---+---+---+---+---+|       |                       |+   +---+   +---+---+   +---+   +|   |           |   |   |       |+   +   +---+   +   +---+   +---+|       |   |   |               |+---+   +   +---+   +---+   +---+|       |   |       |   |   |   |+   +   +   +       +   +   +   +|   |       |       |   |   |   |+   +   +   +---+---+   +   +   +|   |   |                       |+   +   +---+---+---+---+   +   +|   |                   |   |   |+   +   +---+---+   +   +   +   +|   |           |   |       |   |+---+---+---+---+---+---+---+---+"
#maze width: 33 chars
#height: 17
curpos=497
# up 1 space: -66
# down 1 space: +66
# left 1 space: -4
# right 1 space: +4
while True: #play loop
    itr=0 #counter
    for i in range(17): #print 17 lines
        for j in range(33): #print 33 chars per line
            if curpos==itr: #if the mouse's position is equal to the current tile's position, replace it
                print("@",end="")
            else:
                print (list(mazepos)[itr],end="") #otherwise print the tile
            itr=itr+1
        print("",itr-1,end="") #print end tile's position for easier counting
        print("")
    print("pos:",curpos) 
    while True: #input loop
        move=input("Move which way? U/D/L/R (walls not yet functional, moving out of bounds causes issues) ")
        if move=="U": #move mouse according to input
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
        if curpos<35 or curpos>525: #basic out of bounds checker, only handles top and bottom bounds, left and right bounds still cause issues
            print("ERROR: out of bounds") #if the current position is too big or small to be within an actual tile position, return to input loop
            if move=="U": #move mouse back
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
        
