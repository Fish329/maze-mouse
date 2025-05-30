#This program is not guaranteed to generate a tree of depth 4, but it can.
import random
#define nodes
class node:
    def __init__(self,data,depth=0,left=None,center=None,right=None):
        self.data=data
        self.depth=depth
        self.left=left
        self.right=right
        self.center=center
    #define functions
    def insL(self): 
        if random.randrange(0,2): #flip a coin, if heads, add node to left
            self.left=node(random.randrange(0,100),depth=self.depth+1)
            if random.randrange(0,2): #flip a coin again and go through these trials for child
                self.left.insL()
                self.left.insC()
                self.left.insR()
    def insC(self):
        if random.randrange(0,2):
            self.center=node(random.randrange(0,100),depth=self.depth+1)
            if random.randrange(0,2):
                self.center.insL()
                self.center.insC()
                self.center.insR()
    def insR(self):
        if random.randrange(0,2):
            self.right=node(random.randrange(0,100),depth=self.depth+1)
            if random.randrange(0,2):
                self.right.insL()
                self.right.insC()
                self.right.insR()
    def display(self):
        for i in range(self.depth):
            print("-",end="")
        print(" ",self.data," (",self.depth,")",sep="")
        if self.left:
            print("L: ",end="")
            self.left.display()
        if self.center:
            print("C: ",end="")
            self.center.display()
        if self.right:
            print("R: ",end="")
            self.right.display()
        
root=node(random.randrange(0,100))
root.insL()
root.insC()
root.insR()
print("S:",end="")
root.display()
#This program is not guaranteed to generate a tree of depth 4, but it can.
