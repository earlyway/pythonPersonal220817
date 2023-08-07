'''
남은 기능과 테스트

1. obj1, obj2 에 따라 다르게 constraint 을 거는 것.
2. 카드같은 얇은 오브젝트도 테스트해봐야함.
3. 하나의 vset로 여러 오브젝트를 const 할수있는지 테스트
4. 손가락을 따라오는 큐브만 vset1로 쓰고 나머지 const 관련 기능들은 다른 vset2, vset3, …. 로 분할해도 되는지 테스트.
'''
import math

class followCube(vrAEBase):
    global cTh
    global cIn
    cTh = vrNodeService.findNode("cubeThumb4")
    cIn = vrNodeService.findNode("cubeIndex4")
    
    
    global constrained_movin_Tumbler1_NS
    constrained_movin_Tumbler1_NS = vrNodeService.findNode("obj1")
    
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
        print("1")
        self.addLoop()
        print("followCube Start")
        
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        print("recEvent On")
        
    def ffc_distance_Th_In(self):
        cTh.setWorldTranslation(LL_thumb_4.getWorldTranslation())
        cIn.setWorldTranslation(LL_index_4.getWorldTranslation())
        
        global c_t_QM
        global c_i_QM
        c_t_QM = vrdNode.getWorldTransform(cTh)
        c_i_QM = vrdNode.getWorldTransform(cIn)
    
        global c_t_QM_Vect
        global c_i_QM_Vect
        c_t_QM_Vect = vrMathService.getTranslation(c_t_QM)
        c_i_QM_Vect = vrMathService.getTranslation(c_i_QM)
        
    def loop(self):
        self.ffc_distance_Th_In()
        
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force followCube")
        

class distances_obj1(vrAEBase):
    global deleteConst
    deleteConst = False
    global isParentConst
    isParentConst = False
    global dis_standard2
    dis_standard2 = 0
    print("3")

    
    def __init__(self, isColl_Argu):
        vrAEBase.__init__(self)
        self.addLoop()
        self.subLoop()
        self.setActive(true)
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
    def Clear(self):
        amount = vrConstraintService.getConstraints()
        for i in amount:
            vrConstraintService.deleteConstraint(i)
            
    def ConstOn_Th_In(self):
        self.Clear()
        self.left_Constraint_target = vrConstraintService.createParentConstraint([leftController.getNode()], constrained_movin_Tumbler1_NS, True)
        deleteConst = True
        isParentConst = True
        print("4")
        
    def ConstOff_Th_In(self):
        self.Clear()
        deleteConst = False
        isParentConst = False
        self.subLoop()
        print("constraintOff and loop stop")
        
    def dis_measure2(self):
        dis_standard2 = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        print("dis_standard2 : " + str(dis_standard2))
        return dis_standard2
        
        
    
    def loop(self, isColl_Argu):
        print("deleteConst : " + str(deleteConst))
        print("(isColl_Argu : " + str(isColl_Argu))
        print("isParentConst : " + str(isParentConst))
        
        if  deleteConst == False and isColl_Argu == True and isParentConst == False:
            self.ConstOn_Th_In()
            print("ConstOn_Th_In")
            self.dis_measure2()
            
            if dis_standard < dis_standard2:
                self.ConstOff_Th_In()
            
        elif deleteConst == False and isColl_Argu == False and isParentConst == False:
            self.ConstOff_Th_In()
            print("ConstOff_Th_In")

    def substractLoop(self):
        self.subLoop()
        #CollisionAnd.substractLoopC()
        print("loop stop by force distance_cal")
        

    
        
        
class CollisionAnd_obj1(vrAEBase):
    global isColl
    isColl = False 
    global dis_standard
    dis_standard = 0
    
    
    def __init__(self, cols):
        vrAEBase.__init__(self)
        self.dis_measure()
        print("2")
        self.addLoop()
        print("collisionAnd_obj1 Start")
        self.cols = cols
        self.setActive(true)
    
        
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
    def dis_measure(self):
        dis_standard = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        print("dis_standard : " + str(dis_standard))
        return dis_standard
        
    def loop(self):
        
        if self.isActive() == true:
            collide = 0
                                            # collide = 0 으로 초기화
            l = len(self.cols)                    # 들어온 list형 인자값의 개수를 l로 정의
            for i in range(l):                   # l 숫자만큼 for문
                if not self.cols[i].isColliding():# list형 index를 하나씩 불러와 isColliding을 출력해서 False 형태라면
                    break                         # break로 인해 for문을 멈추고 다음 if collide == l: 로 넘어간다.  
                else:                             # 그외 나머지 경우라면(isColliding들이 True값이 나오면)
                    collide += 1                  #0으로 초기화했던 collide 값에 1씩 더해줌.
            if collide == l:
                print("sticker")
                isColl = True                   #l 숫자만큼 for문이 끝나고 만약 collide 값이 l 숫자와 같다면
                #self.callAllConnected()             #호출된 모든 연결 Connected 를 가져옴. 그리고 loop. 아래처럼 ?.connect 형태의 것만 가져오는 것임. 주의!
                distances_instance.loop(True)
            else :
                isColl = False
                distances_instance.loop(False)

    def substractLoop(self):
        self.subLoop()
        print("loop stop by force 3 collid")
    
    

#--------------------------------------------------------------

print("test line-------------------------")
    

cdscd = followCube() #loop1

# create some collision objects #
collx = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
colly = vrCollision([constrained_movin_Tumbler1_NS], [cIn])


collxy = CollisionAnd_obj1([collx, colly]) #loop2
#collxy.connect("print 'WM-------------------'")

distances_instance = distances_obj1(False)

#collxy.connect(distances_class)


vrK = vrKey(Key_R)

elfeo = None
vrK.connect(cdscd.substractLoop)
vrK.connect(distances_instance.substractLoop)
print("collxy type : " + str(type(collxy)) )
#vrK.connect(collxy(elfeo).substractLoop)
vrK.connect(collxy.substractLoop)

