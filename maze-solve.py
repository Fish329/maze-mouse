class node:
    def __init__(self,data,left=None,right=None,center=None,depth=0):
        self.data=data
        self.left=left
        self.right=right
        self.center=center
        self.depth=depth
    
    def insert(self,data,pos): #Add a left, right, or center child.
        if pos=="L":
            self.left=node(data,depth=self.depth+1)
        elif pos=="R":
            self.right=node(data,depth=self.depth+1)
        elif pos=="C":
            self.center=node(data,depth=self.depth+1)
    def traverse(self,iterations,pos): 
        recurse=self
        for i in range(iterations):
            if pos=="L":
                recurse=recurse.left
            elif pos=="C":
                recurse=recurse.center
            elif pos=="R":
                recurse=recurse.right
        return recurse
            
root=node(497) #0,0
root.insert(431,"L") #0,0 to 0,1
root.left.insert(365,"L") #0,1 to 0,2
root.left.left.insert(299,"L") #0,2 to 0,3
root.left.left.left.insert(233,"L") #0,3 to 0,4
root.left.left.left.left.insert(237,"L") #0,4 to 1,4
root.traverse(5,"L").insert(171,"L") #1,4 to 1,5
root.traverse(5,"L").insert(303,"R") #1,4 to 1,3
root.traverse(6,"L").insert(105,"L") #1,5 to 1,6
#THIS IS WIP, the tree is not fully built yet

#The maze, crushed down into one string
mazepos="+---+---+---+---+---+---+---+---+|       |                       |+   +---+   +---+---+   +---+   +|   |           |   |   |       |+   +   +---+   +   +---+   +---+|       |   |   |               |+---+   +   +---+   +---+   +---+|       |   |       |   |   |   |+   +   +   +       +   +   +   +|   |       |       |   |   |   |+   +   +   +---+---+   +   +   +|   |   |                       |+   +   +---+---+---+---+   +   +|   |                   |   |   |+   +   +---+---+   +   +   +   +|   |           |   |       |   |+---+---+---+---+---+---+---+---+"
#maze width: 33 chars
#height: 17
curpos=497
# up 1 space: -66
# down 1 space: +66
# left 1 space: -4
# right 1 space: +4
def drawmaze(curpos,mazepos):
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
