import random
class node:
    def __init__(self,data,parent=None,left=None,center=None,right=None,depth=0,endExist=False,end=False):
        self.left=left #left child
        self.center=center #center child
        self.right=right #right child
        self.depth=depth #node depth
        self.parent=parent #this node's parent
        self.endExist=endExist #flag for if the end node has been created
        self.end=end #flag for if this node is the end node
        self.data=data #Node's data
        if self.parent!=None:
            self.depth=self.parent.depth+1
            
    def spawn(self):
        if self.depth<3:
            roll=random.randrange(1,4)
            for i in range(roll):
                pool=["L","C","R"]
                if self.left:
                    pool.remove("L")
                if self.center:
                    pool.remove("C")
                if self.right:
                    pool.remove("R")
                pick=random.choice(pool)
                if pick=="L":
                    self.left=node(random.randrange(0,100),self,endExist=self.endExist)
                    self.left.spawn()
                if pick=="C":
                    self.center=node(random.randrange(0,100),self,endExist=self.endExist)
                    self.center.spawn()
                if pick=="R":
                    self.right=node(random.randrange(0,100),self,endExist=self.endExist)
                    self.right.spawn()
        else:
            if self.endExist==False:
                self.end=True
                self.tellUp()
        
    def display(self):
        for i in (range(self.depth)):
            print("-",end="")
        print(self.data,end="")
        if self.end==True:
            print(" FINISH")
        else:
            print("")
        if self.left:
            print("L:",end="")
            self.left.display()
        if self.center:
            print("C:",end="")
            self.center.display()
        if self.right:
            print("R:",end="")
            self.right.display()
            
    def tellUp(self):
        self.endExist=True
        if self.parent and self.parent.endExist==False:
            self.parent.tellDown()
    
    def tellDown(self):
        self.endExist=True
        if self.left!=None and self.left.endExist==False:
            self.left.endExist=True
        if self.center!=None and self.center.endExist==False:
            self.center.endExist=True
        if self.right!=None and self.right.endExist==False:
            self.right.endExist=True
        if self.parent!=None and self.parent.endExist==False:
            self.parent.tellDown()
                
root=node(random.randrange(0,100))
root.spawn()
root.display()
#this is wip
