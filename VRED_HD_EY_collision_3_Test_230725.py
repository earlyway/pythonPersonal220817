'''
오브젝트 a,b,c가 있고 b를 중심으로 콜리전이 될때 console에
1 vc
2 iia
class test print rpp
method print LC
가 반복해서 출력됨.

주석처리된
collab.connect(classTest.methodTest(cols)) 와 collab.connect(classTest())
를 해제하면 변형세트를 실행했을 때, 최초로 한번 console print 됨.
'''

class classTest(vrAEBase):
     def __init__(self):
        vrAEBase.__init__(self)
        print("class test print rpp")
        
     def methodTest(self):
         print("method print LC")


class CollisionAnd(vrAEBase):
    def __init__(self, cols):
        vrAEBase.__init__(self)
        self.addLoop()
        self.cols = cols
        self.setActive(true)
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
    def loop(self):
        if self.isActive() == true:
            collide = 0
            l = len(self.cols)
            for i in range(l):
                if not self.cols[i].isColliding():
                    break
                else:
                    collide += 1
            if collide == l:
                self.callAllConnected()

def vc():
    print("1 vc")
    
def iia():
    print("2 iia")
    
def rpp():
    classTest()
    
def LC():
    ar = None
    classTest.methodTest(ar)


#find collision Node
obja = findNode("Object_A")
objb = findNode("Object_B")
objc = findNode("Object_C")


# create some collision objects #
colla = vrCollision([obja], [objb])
collb = vrCollision([objb], [objc])

cols = None
collab = CollisionAnd([colla, collb])
collab.connect(vc)
collab.connect(iia)
collab.connect(rpp)
collab.connect(LC)
#collab.connect(classTest.methodTest(cols))
#collab.connect(classTest())



