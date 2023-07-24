'''
수정 필요!!
followCube가 먼저 되어야하고

그 다음 collisionAnd

그리고나서 distance 구하는 것이 되어야함.
'''
import math

class followCube(vrAEBase):
    global cTh
    global cIn
    cTh = vrNodeService.findNode("cubeThumb4")
    cIn = vrNodeService.findNode("cubeIndex4")
    
    global constrained_movin_Tumbler1_NS
    constrained_movin_Tumbler1_NS = vrNodeService.findNode("moving_Tumbler1")
    
    global leftController
    leftController = vrDeviceService.getVRDevice("left-controller")
    
    global LL_thumb_4
    global LL_index_4
    LL_thumb_4 = vrNodeService.findNode('L_thumb_4_INT', root=getInternalRootNode())
    LL_index_4 = vrNodeService.findNode('L_index_4_INT', root=getInternalRootNode())
    
    global distance_cal
    distance_cal = 0
    
    global left_Constraint_target
    left_Constraint_target = None
    
    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        print("recEvent On")
    def ffc(self):  #finger follow cube
        print(LL_thumb_4.getWorldTranslation())
        cTh.setWorldTranslation(LL_thumb_4.getWorldTranslation())
        cIn.setWorldTranslation(LL_index_4.getWorldTranslation())
    def distance_Th_In(self):
        global c_t_QM
        global c_i_QM
        c_t_QM = vrdNode.getWorldTransform(cTh)
        c_i_QM = vrdNode.getWorldTransform(cIn)
    
        global  c_t_QM_Vect
        global c_i_QM_Vect
        c_t_QM_Vect = vrMathService.getTranslation(c_t_QM)
        c_i_QM_Vect = vrMathService.getTranslation(c_i_QM)
        
    def ConstOn_Th_In(self):
        self.Clear()
        self.left_Constraint_target = vrConstraintService.createParentConstraint([leftController.getNode()], constrained_movin_Tumbler1_NS, True)
    def ConstOff_Th_In(self):
        self.Clear()
        self.subLoop()
        print("constraint loop stop")
    def Clear(self):
        amount = vrConstraintService.getConstraints()
        for i in amount:
            vrConstraintService.deleteConstraint(i)
    def loop(self):
        self.ffc()
        self.distance_Th_In()
        distance_cal = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        print(distance_cal)
        
        if distance_cal < 66:
            self.ConstOn_Th_In()
            print("ConstOn_Th_In")
        elif distance_cal >= 66:
            self.ConstOff_Th_In()
            print("ConstOff_Th_In")
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force")
        
        
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


# create some collision objects #
colla = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
collb = vrCollision([constrained_movin_Tumbler1_NS], [cIn])

collab = CollisionAnd([colla, collb])
collab.connect("print 'WUMM!'")
collab.connect(followCube)

print("just move Object_A so it collides with Object_B\n and Object_C so it collides with Object_D.")
'''
vrK = vrKey(Key_R)
cb = followCube()
vrK.connect(cb.substractLoop)
'''