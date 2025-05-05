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
root.insert(0,1,"L") #0,0 to 0,1
root.left.insert(0,2,"L") #0,1 to 0,2
root.left.left.insert(0,3,"L") #0,2 to 0,3
root.left.left.left.insert(0,4,"L") #0,3 to 0,4
root.left.left.left.left.insert(1,4,"L") #0,4 to 1,4
root.trav(5,"L").insert(1,5,"L") #1,4 to 1,5
root.trav(5,"L").insert(1,3,"R") #1,4 to 1,3
root.trav(6,"L").insert(1,6,"L") #1,5 to 1,6
root.trav(6,"L").insert(0,5,"R") #1,5 to 0,5
root.trav(5,"L").right.insert(1,2,"L") #1,3 to 1,2
root.trav(5,"L").right.insert(2,3,"R") #1,3 to 2,3
root.trav(7,"L").insert(2,6,"L") #1,6 to 2,6
root.trav(6,"L").right.insert(0,6,"L") #0,5 to 0,6
root.trav(6,"L").right.left.insert(1,1,"L")#1,2 to 1,1
root.trav(5,"L").right.right.insert(2,4,"L")#2,3 to 2,4
root.trav(5,"L").right.right.insert(2,2,"R")#2,3 to 2,2
root.trav(8,"L").insert(3,6,"L") #2,6 to 3,6
root.trav(8,"L").insert(2,7,"R") #2,6 to 2,7
root.trav(6,"L").right.left.insert(0,7,"L") #0,6 to 0,7
root.trav(6,"L").right.left.left.insert(1,0,"L") #1,1 to 1,0
root.trav(6,"L").right.left.left.insert(2,1,"R") #1,1 to 2,1
root.trav(5,"L").right.right.left.insert(2,5,"L") #2,4 to 2,5
root.trav(5,"L").trav(3,"R").insert(3,2,"L")#2,2 to 3,2
root.trav(9,"L").insert(3,5,"L")#3,6 to 3,5
root.trav(8,"L").right.insert(3,7,"L") #2,7 to 3,7
root.trav(6,"L").right.left.left.insert(1,7,"L")#0,7 to 1,7
root.trav(6,"L").right.trav(3,"L").insert(2,0,"L")#1,0 to 2,0
root.trav(6,"L").right.left.left.right.insert(3,1,"L")#2,1 to 3,1
root.trav(5,"L").trav(3,"R").left.insert(4,2,"L")#3,2 to 4,2
root.trav(8,"L").right.left.insert(4,7,"L")#3,7 to 4,7
root.trav(6,"L").right.trav(4,"L").insert(3,0,"L")#2,0 to 3,0
root.trav(6,"L").right.left.left.right.left.insert(4,1,"L")#3,1 to 4,1
root.trav(5,"L").trav(3,"R").left.left.insert(5,2,"L")#4,2 to 5,2
root.trav(8,"L").right.left.left.insert(5,7,"L")#4,7 to 5,7
root.trav(6,"L").right.left.left.right.left.left.insert(5,1,"L")#4,1 to 5,1
root.trav(6,"L").right.left.left.right.left.left.insert(4,0,"R")#4,1 to 4,0
root.trav(5,"L").trav(3,"R").trav(3,"L").insert(5,3,"L")#5,2 to 5,3
root.trav(5,"L").trav(3,"R").trav(3,"L").insert(6,2,"R")#5,2 to 6,2
root.trav(8,"L").right.trav(3,"L").insert(5,6,"L")#5,7 to 5,6
root.trav(8,"L").right.trav(3,"L").insert(6,7,"R")#5,7 to 6,7
root.trav(6,"L").right.left.left.right.trav(3,"L").insert(5,0,"L")#5,1 to 5,0
root.trav(5,"L").trav(3,"R").trav(4,"L").insert(5,4,"L")#5,3 to 5,4
root.trav(8,"L").right.trav(3,"L").right.insert(7,2,"L")#6,2 to 7,2
root.trav(8,"L").right.trav(3,"L").right.insert(6,3,"R")#6,2 to 6,3
root.trav(8,"L").right.trav(3,"L").right.insert(7,7,"L")#6,7 to 7,7
root.trav(6,"L").right.left.left.right.trav(4,"L").insert(6,0,"L")#5,0 to 6,0
root.trav(8,"L").right.trav(3,"L").right.left.insert(7,3,"L")#7,2 to 7,3
root.trav(8,"L").right.trav(3,"L").right.left.insert(7,1,"R")#7,2 to 7,1
root.trav(8,"L").right.trav(3,"L").right.right.insert(6,4,"L")#6,3 to 6,4
root.trav(8,"L").right.trav(3,"L").right.left.insert(7,6,"L")#7,7 to 7,6
root.trav(6,"L").right.left.left.right.trav(5,"L").insert(6,1,"L")#6,0 to 6,1
root.trav(8,"L").right.trav(3,"L").right.left.left.insert(7,4,"L")#7,3 to 7,4
root.trav(8,"L").right.trav(3,"L").right.left.right.insert(7,0,"L")#7,1 to 7,0
root.trav(8,"L").right.trav(3,"L").right.right.left.insert(6,5,"L")#6,4 to 6,5
root.trav(8,"L").right.trav(3,"L").right.left.left.insert(6,6,"L")#7,6 to 6,6
move=root.trav(5,"L").trav(3,"R").trav(3,"L").right
root.trav(6,"L").right.left.left.right.trav(5,"L").left=move #6,1 to 6,2
root.trav(8,"L").right.trav(3,"L").right.right.left.left.insert(5,5,"L")#6,5 to 5,5
root.trav(8,"L").right.trav(3,"L").right.right.left.left.insert(7,5,"R")#6,5 to 7,5
move=root.trav(8,"L").right.trav(3,"L").right.right.left.left
root.trav(8,"L").right.trav(3,"L").right.trav(3,"L").left=move #6,6 to 6,5
root.trav(8,"L").right.trav(3,"L").right.right.trav(3,"L").insert(4,5,"L") #5,5 to 4,5
root.trav(8,"L").right.trav(3,"L").right.right.trav(4,"L").insert(4,6,"L") #4,5 to 4,6
root.trav(8,"L").right.trav(3,"L").right.right.trav(4,"L").insert(4,4,"L") #4,5 to 4,4 (END)
myNode=root
myNode.display()
