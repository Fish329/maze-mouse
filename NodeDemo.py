class node:
    def __init__(self,x,y,pos=None,le=None,ri=None,ce=None,depth=0):
        self.x=x
        self.y=y
        self.le=le
        self.ri=ri
        self.ce=ce
        self.depth=depth
        self.pos=pos
    
    def insL(self,wnode):
            self.le=wnode
            wnode.depth=self.depth+1
            wnode.pos="L"
    def insR(self,wnode):
            self.ri=wnode
            wnode.depth=self.depth+1
            wnode.pos="R"
    def insC(self,wnode):
            self.ce=wnode
            wnode.depth=self.depth+1
            wnode.pos="C"
            
    def trav(self,iterations,pos): #Traverse, to marginally shorten the commands
        recurse=self
        for i in range(iterations):
            if pos=="L":
                recurse=recurse.left
            elif pos=="C":
                recurse=recurse.center
            elif pos=="R":
                recurse=recurse.right
        return recurse
    
    def display(self): #Print own data, run the same code for left child, center child, and right child, if they have them
        if self.depth>0:
            for i in range(self.depth):
                print("-",end="")
            print("(",self.x,",",self.y,") ","(",self.pos,")",sep="")
        else:
            print("(",self.x,",",self.y,")",sep="")
        if self.le:
            self.le.display()
        if self.ce:
            self.ce.display()
        if self.ri:
            self.ri.display()

c00=node(0,0)
c01=node(0,1)
c02=node(0,2)
c03=node(0,3)
c04=node(0,4)
c05=node(0,5)
c06=node(0,6)
c07=node(0,7)
c10=node(1,0)
c11=node(1,1)
c12=node(1,2)
c13=node(1,3)
c14=node(1,4)
c15=node(1,5)
c16=node(1,6)
c17=node(1,7)
c20=node(2,0)
c21=node(2,1)
c22=node(2,2)
c23=node(2,3)
c24=node(2,4)
c25=node(2,5)
c26=node(2,6)
c27=node(2,7)
c30=node(3,0)
c31=node(3,1)
c32=node(3,2)
c33=node(3,3)
c34=node(3,4)
c35=node(3,5)
c36=node(3,6)
c37=node(3,7)
c40=node(4,0)
c41=node(4,1)
c42=node(4,2)
c43=node(4,3)
c44=node(4,4)
c45=node(4,5)
c46=node(4,6)
c47=node(4,7)
c50=node(5,0)
c51=node(5,1)
c52=node(5,2)
c53=node(5,3)
c54=node(5,4)
c55=node(5,5)
c56=node(5,6)
c57=node(5,7)
c60=node(6,0)
c61=node(6,1)
c62=node(6,2)
c63=node(6,3)
c64=node(6,4)
c65=node(6,5)
c66=node(6,6)
c67=node(6,7)
c70=node(7,0)
c71=node(7,1)
c72=node(7,2)
c73=node(7,3)
c74=node(7,4)
c75=node(7,5)
c76=node(7,6)
c77=node(7,7)

c00.insC(c01)
c01.insC(c02)
c02.insC(c03)
c03.insC(c04)
c04.insL(c14)
c14.insL(c15)
c14.insR(c13)
c15.insL(c05)
c15.insC(c16)
c13.insL(c23)
c13.insC(c12)
c05.insC(c06)
c16.insL(c26)
c23.insL(c24)
c23.insR(c22)
c12.insC(c11)
c06.insC(c07)
c26.insL(c27)
c26.insC(c36)
c24.insC(c25)
c22.insL(c32)
c11.insC(c10)
c11.insL(c21)
c07.insL(c17)
c27.insL(c37)
c36.insR(c35)
c32.insC(c42)
c10.insL(c20)
c21.insC(c31)
c37.insC(c47)
c42.insC(c52)
c20.insC(c30)
c31.insC(c41)
c47.insC(c57)
c52.insL(c53)
c52.insC(c62)
c41.insL(c40)
c41.insC(c51)
c57.insL(c56)
c57.insC(c67)
c53.insC(c54)
c62.insC(c72)
c62.insL(c63)#
c51.insR(c50)#
c67.insC(c77)#
c72.insL(c73)#
c72.insR(c71)#
#WIP
