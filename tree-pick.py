class node:
    def __init__(self,x,y,depth=0,childI=None,childII=None):
        self.x=x
        self.y=y
        self.depth=depth
        self.childI=childI
        self.childII=childII
    
    def display(self):
        for i in range(self.depth):
            print("-",end="",sep="")
        print("(",self.x,",",self.y,")",sep="")
        if self.childI:
            self.childI.depth=self.depth+1
            self.childI.display()
        if self.childII:
            self.childII.depth=self.depth+1
            self.childII.display()
        
l00=node(0,0)
l01=node(0,1)
l02=node(0,2)
l10=node(1,0)
l11=node(1,1)
l12=node(1,2)
l20=node(2,0)
l21=node(2,1)
l22=node(2,2)

def maze1():
    l00.childI=l01
    l00.childII=l10
    l01.childI=l02
    l10.childI=l20
    l02.childI=l12
    l20.childI=l21
    l21.childI=l22
    l12.childI=l11
    l22.childI=l12
def maze2():
    l00.childI=l91
def maze3():
    pass #wip
def maze4():
    pass #wip
l00.display()
