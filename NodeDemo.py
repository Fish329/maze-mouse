class node:
    def __init__(self,x,y,pos=None,left=None,right=None,center=None,depth=0):
        self.x=x
        self.y=y
        self.left=left
        self.right=right
        self.center=center
        self.depth=depth
        self.pos=pos
    
    def insert(self,x,y,pos): #Add a left, right, or center child.
        if pos=="L":
            self.left=node(x,y,pos,depth=self.depth+1)
        elif pos=="R":
            self.right=node(x,y,pos,depth=self.depth+1)
        elif pos=="C":
            self.center=node(x,y,pos,depth=self.depth+1)
            
    def trav(self,iterations,pos): #Traverse, to marginally shorten the commands
        recurse=self
        for i in range(iterations):
            if pos=="L":
                recurse=recurse.left
            elif pos=="C":
                recurse=recurse.center
            elif pos=="R":
                recurse=recurse.right
        return recurse
    
    def display(self): #Print own data, run the same code for left child, center child, and right child, if they have them
        if self.depth>0:
            for i in range(self.depth):
                print("-",end="")
            print("(",self.x,",",self.y,") ","(",self.pos,")",sep="")
        else:
            print("(",self.x,",",self.y,")",sep="")
        if self.left:
            self.left.display()
        if self.center:
            self.center.display()
        if self.right:
            self.right.display()
    
       

root=node(0,0) #0,0
root.insert(0,1,"C") #0,0 to 0,1
root.center.insert(0,2,"C") #0,1 to 0,2
root.trav(2,"C").insert(0,3,"C") #0,2 to 0,3
root.trav(3,"C").insert(0,4,"C") #0,3 to 0,4
root.trav(4,"C").insert(1,4,"R") #0,4 to 1,4
root.trav(4,"C").right.insert(1,5,"L") #1,4 to 1,5
root.trav(4,"C").right.insert(1,3,"R") #1,4 to 1,3
root.trav(4,"C").right.left.insert(0,5,"L") #1,5 to 0,5
root.trav(4,"C").right.left.insert(1,6,"C") #1,5 to 1,6
root.trav(4,"C").right.right.insert(1,2,"C") #1,3 to 1,2
root.trav(4,"C").right.right.insert(2,3,"L") #1,3 to 2,3
root.trav(4,"C").right.left.left.insert(0,6,"R")#0,5 to 0,6
root.trav(4,"C").right.left.center.insert(2,6,"L")#1,6 to 2,6
root.trav(4,"C").right.right.center.insert(1,1,"C")#1,2 to 1,1
root.trav(4,"C").right.right.left.insert(2,4,"L")#2,3 to 2,4
root.trav(4,"C").right.right.left.insert(2,2,"R")#2,3 to 2,2
root.trav(4,"C").right.left.left.right.insert(0,7,"C")#0,6 to 0,7
root.trav(4,"C").right.left.center.left.insert(3,6,"C")#2,6 to 3,6
root.trav(4,"C").right.right.trav(2,"C").insert(2,1,"L")#1,1 to 2,1
root.trav(4,"C").right.right.trav(2,"C").insert(1,0,"C")#1,1 to 1,0
root.trav(4,"C").right.right.left.left.insert(2,5,"C")#2,4 to 2,5
root.trav(4,"C").right.right.left.right.insert(3,2,"L")#2,2 to 3,2
root.trav(4,"C").right.left.left.right.center.insert(1,7,"R")#0,7 to 1,7
root.trav(4,"C").right.left.center.left.center.insert(3,5,"R")#3,6 to 3,5
root.trav(4,"C").right.right.trav(2,"C").left.insert(3,1,"C")#2,1 to 3,1
root.trav(4,"C").right.right.left.right.left.insert(2,0,"L")#1,0 to 2,0
root.trav(4,"C").right.right.left.right.left.insert(4,2,"C")#3,2 to 4,2
root.trav(4,"C").right.right.trav(2,"C").left.center.insert(4,1,"C") #3,1 to 4,1
root.trav(4,"C").right.right.left.right.left.left.insert(3,0,"C")#2,0 to 3,0
root.trav(4,"C").right.right.left.right.left.center.insert(5,3,"C")#4,2 to 5,2
root.trav(4,"C").right.right.trav(2,"C").left.trav(2,"C").insert(4,0,"R")#4,1 to 4,0
root.trav(4,"C").right.right.trav(2,"C").left.trav(2,"C").insert(5,1,"C")#4,1 to 5,1#
root.trav(4,"C").right.right.left.right.left.trav(2,"C").insert(5,3,"L")#5,2 to 5,3#
root.trav(4,"C").right.right.left.right.left.trav(2,"C").insert(6,2,"C")#5,2 to 6,2#
#WIP
myNode=root
myNode.display()
