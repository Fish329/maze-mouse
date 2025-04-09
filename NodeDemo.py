class node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    def insert(self,data,pos):
        if pos=="L":
            self.left=node(data)
        elif pos=="R":
            self.right=node(data)
    
    def traverse(self,pos):
        cur=0
        if pos=="L":
            cur=self.left
        elif pos=="R":
            cur=self.right
        return cur
    
    def display(self):
        print(self.data)
        if self.left:
            print("L: ",end="")
            self.left.display()
        if self.right:
            print("R: ",end="")
            self.right.display()
       

root=node("Door")
root.insert("Foyer","L")
root.insert("Kitchen","R")
root.left.insert("Den","L")
root.left.insert("Bedrooms","R")
root.right.insert("Dining Room","L")
root.right.insert("Bathroom","R")
myNode=root
myNode.display()
