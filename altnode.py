#possible alternative node system
class node:
    def __init__ (self, x,y, parent=None,children=[],deadend=False):
        self.x=x
        self.y=y
        self.parent=parent
        self.children=children
        if self.parent!=None:
            self.parent.addchild(self)
    def addchild(self,child):
        self.children.append(child)

pos00=node(0,0) #
pos01=node(0,1,pos00) #
pos02=node(0,2,pos01) #
pos03=node(0,3,pos02) #
pos04=node(0,4,pos03) #
pos14=node(1,4,pos04) #
pos15=node(1,5,pos14) #
pos13=node(1,3,pos14) #
pos05=node(0,5,pos15)
pos16=node(1,6,pos15)
pos23=node(2,3,pos13)
pos12=node(1,2,pos13)
