#this is wip
import random
#define nodes
class node:
    def __init__(self,data,depth=0,left=None,center=None,right=None,parent=None):
        self.data=data
        self.depth=depth
        self.left=left
        self.right=right
        self.center=center
        parent=parent
    #define functions
    def insL(self,final): 
        self.left=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        if self.depth<1:
            rng=random.randrange(0,3)
            if rng==0:
                self.left.insL(final)
            elif rng==1:
                   self.left.insC(final)
            elif rng==2:
                self.left.insR(final)
        elif final==0:
            print("this is valid syntax")
                    
    def insC(self,final):
        self.center=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        if self.depth<2:
            rng=random.randrange(0,3)
            if rng==0:
                self.center.insL(final)
            elif rng==1:
                self.center.insC(final)
            elif rng==2:
                self.center.insR(final)
            
    def insR(self,final):
        self.right=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        if self.depth<2:
            rng=random.randrange(0,3)
            if rng==0:
               self.right.insL(final)
            elif rng==1:
                self.right.insC(final)
            elif rng==2:
                self.right.insR(final)

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
final=0
root.insL(final)
root.insC(final)
root.insR(final)
print("S:",end="")
root.display()
#this is wip
