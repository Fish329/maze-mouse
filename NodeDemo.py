class node:
    def __init__(self,data,pos=None,left=None,right=None,center=None,depth=0):
        self.data=data
        self.left=left
        self.right=right
        self.center=center
        self.depth=depth
        self.pos=pos
    
    def insert(self,data,pos): #Add a left, right, or center child.
        if pos=="L":
            self.left=node(data,pos,depth=self.depth+1)
        elif pos=="R":
            self.right=node(data,pos,depth=self.depth+1)
        elif pos=="C":
            self.center=node(data,pos,depth=self.depth+1)
    
    def display(self): #Print own data, run the same code for left child, center child, and right child, if they have them
        if self.depth>0:
            for i in range(self.depth-1):
                print("│",end="")
            print("├",end="")
            print(self.data,"(",self.pos,")",sep="")
        else:
            print(self.data)
        if self.left:
            self.left.display()
        if self.center:
            self.center.display()
        if self.right:
            self.right.display()
    
       

root=node("Door") #create tree
root.insert("Foyer","L")
root.insert("Kitchen","R")
root.insert("Living Room","C")
root.left.insert("Den","L")
root.left.insert("Bedrooms","R")
root.right.insert("Dining Room","L")
root.right.insert("Bathroom","R")
myNode=root
myNode.display()
