class node:
    def __init__(self,data,left=None,right=None,center=None):
        self.data=data
        self.left=left
        self.right=right
        self.center=center
    
    def insert(self,data,pos): #Add a left, right, or center child.
        if pos=="L":
            self.left=node(data)
        elif pos=="R":
            self.right=node(data)
        elif pos=="C":
            self.center=node(data)
    
    def display(self): #Print own data, run the same code for left child, center child, and right child, if they have them
        print(self.data)
        if self.left:
            print("L: ",end="")
            self.left.display()
        if self.center:
            print("C: ",end="")
            self.center.display()
        if self.right:
            print("R: ",end="")
            self.right.display()
        print("-BT-") #Represents a backtrack
    
       

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
