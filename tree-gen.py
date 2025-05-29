#comically large WIP
import random
class node:
    def __init__(self,data,left=None,center=None,right=None):
        self.data=data
        self.left=left
        self.right=right
        self.center=center
    def insL(self):
        if random.randrange(0,2):
            self.left=node(random.randrange(0,100))
            if random.randrange(0,2):
                self.left.insL()
                self.left.insC()
                self.left.insR()
    def insC(self):
        if random.randrange(0,2):
            self.center=node(random.randrange(0,100))
            if random.randrange(0,2):
                self.center.insL()
                self.center.insC()
                self.center.insR()
    def insR(self):
        if random.randrange(0,2):
            self.right=node(random.randrange(0,100))
            if random.randrange(0,2):
                self.right.insL()
                self.right.insC()
                self.right.insR()
    def display(self):
        
root=node(random.randrange(0,100))
root.insL()
root.insC()
root.insR()
