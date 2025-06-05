#this is wip
import random
#define nodes
class node:
    def __init__(self,data,depth=0,children=0,left=None,center=None,right=None,parent=None):
        self.data=data
        self.depth=depth
        self.left=left
        self.right=right
        self.center=center
        self.parent=parent
        self.children=children
    #define functions
    def spawn(self):
        pool=[0,1,2]
        for i in range(2):
            pick=random.choice(pool)
            if i>0:
                if random.randrange(0,2)==0:
                    pool.remove(pick)
                    continue
            if pick==0:
                self.insL()
            elif pick==1:
                self.insC()
            elif pick==2:
                self.insR()
            pool.remove(pick)
            
    def insL(self): 
        self.left=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        self.children+=1
        if self.depth<2:
            if self.children>1:
                if random.randrange(0,2)==0:
                    return
            self.left.spawn()

    def insC(self):
        self.center=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        self.children+=1
        if self.depth<2:
            if self.children>1:
                if random.randrange(0,2)==0:
                    return
            self.center.spawn()
            
    def insR(self):
        self.right=node(random.randrange(0,100),depth=self.depth+1,parent=self)
        self.children+=1
        if self.depth<2:
            if self.children>1:
                if random.randrange(0,2)==0:
                    return
            self.right.spawn()

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
root.spawn()
print("S:",end="")
root.display()
#this is wip
