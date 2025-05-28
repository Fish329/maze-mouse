import random
class node:
    def __init__(self,x,y,special=None,pos=None,le=None,ri=None,ce=None,depth=0,opt=False):
        self.x=x
        self.y=y
        self.le=le
        self.ri=ri
        self.ce=ce
        self.depth=depth
        self.pos=pos
        self.special=special
        self.opt=opt
    
    def insL(self,wnode): #insert a node at the left position
            self.le=wnode
            wnode.depth=self.depth+1
            if wnode.pos!=None:
                wnode.pos="X"
            else:
                wnode.pos="L"
    def insR(self,wnode): #insert at the right position
            self.ri=wnode
            wnode.depth=self.depth+1
            if wnode.pos!=None:
                wnode.pos="X"
            else:
                wnode.pos="R"
    def insC(self,wnode): #insert at the center position
            self.ce=wnode
            wnode.depth=self.depth+1
            if wnode.pos!=None:
                wnode.pos="X"
            else:
                wnode.pos="C"
    
    def display(self,parent): #Print own data, run the same code for left child, center child, and right child, if they have them
        if self.depth>0:
            for i in range(self.depth):
                print("-",end="")
            print("(",self.x,",",self.y,") (",self.pos,") ",sep="",end="")
        else:
            print("(",self.x,",",self.y,") ",sep="",end="")
        if self.special:
            print(self.special)
        else:
            print("")
        if self.le:
            self.le.depth=self.depth+1
            self.le.pos="L"
            self.le.display(self)
        if self.ce:
            self.ce.depth=self.depth+1
            self.ce.pos="C"
            self.ce.display(self)
        if self.ri:
            self.ri.depth=self.depth+1
            self.ri.pos="R"
            self.ri.display(self)

def twoByTwo():
    #define nodes
    c00=node(0,0,"START")
    c01=node(0,1)
    c10=node(1,0)
    c11=node(1,1,"FINISH")
    #define starting connections
    seed=random.randrange(0,2)
    if seed==0:
        c00.insR(c10)
        c10.special="DEAD END"
        c00.insC(c01)
        c01.insR(c11)
    elif seed==1:
        c00.insC(c01)
        c01.special="DEAD END"
        c00.insR(c10)
        c10.insL(c11)
    print("Seed:",seed)
    c00.display(None)
twoByTwo()
