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
        self.left=node(random.randrange(0,100),depth=self.depth+1)
        if self.depth<3:
            rng=random.randrange(0,3)
            if rng==0:
                self.left.insL()
            elif rng==1:
                   self.left.insC()
            elif rng==2:
                self.left.insR()
                    
    def insC(self):
        self.center=node(random.randrange(0,100),depth=self.depth+1)
        if self.depth<3:
            rng=random.randrange(0,3)
            if rng==0:
                self.center.insL()
            elif rng==1:
                self.center.insC()
            elif rng==2:
                self.center.insR()
            
    def insR(self):
        self.right=node(random.randrange(0,100),depth=self.depth+1)
        if self.depth<3:
            rng=random.randrange(0,3)
            if rng==0:
               self.right.insL()
            elif rng==1:
                self.right.insC()
            elif rng==2:
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
