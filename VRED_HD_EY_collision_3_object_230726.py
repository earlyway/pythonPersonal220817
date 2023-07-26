'''
실행하면 큐브가 콜리전될때 constraint가 on 되고
콜리전이 하나라도 해제가 되면 constriant가 off 됨

global 전역변수화가 되면 self 없어도 됨.


실행하다가 루프를 멈추고싶다면
187줄~ 마지막 줄의 주석을 제거하고 실행하면 루프가 멈춤.


'''
import math

class followCube(vrAEBase):
    global cTh
    global cIn
    cTh = vrNodeService.findNode("cubeThumb4")
    cIn = vrNodeService.findNode("cubeIndex4")
    
    global constrained_movin_Tumbler1_NS
    constrained_movin_Tumbler1_NS = vrNodeService.findNode("CubeBlender")
    
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
        #print("ffc " + str(LL_thumb_4.getWorldTranslation()))
        #print("2")
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
        #print("3")
        
    def loop(self):
        self.ffc_distance_Th_In()
        
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force followCube")
        
         
class distances(vrAEBase):
    print("distance class enter 1")
    global deleteConst
    deleteConst = False
    global isParentConst
    isParentConst = False
    
    def __init__(self, isColl_Argu):
        vrAEBase.__init__(self)
        print("distance class enter 2")
        #self.isColl_Argu = isColl_Argu
        self.addLoop()
        self.subLoop()
        print("distance class enter 2-1")
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
        
        
    def ConstOff_Th_In(self):
        self.Clear()
        deleteConst = False
        isParentConst = False
        self.subLoop()
        print("constraint loop stop")
    
    def loop(self, isColl_Argu):
        print("distances class loop start")

        print(deleteConst)
        print(isColl_Argu)
        print(isParentConst)
        
        if  deleteConst == False and isColl_Argu == True and isParentConst == False:
            self.ConstOn_Th_In()
            print("ConstOn_Th_In")
            print("6")
        elif deleteConst == False and isColl_Argu == False and isParentConst == False:
            self.ConstOff_Th_In()
            print("ConstOff_Th_In")
            print("7")
    def substractLoop(self):
        self.subLoop()
        #CollisionAnd.substractLoopC()
        print("loop stop by force distance_cal")
    
        
class CollisionAnd(vrAEBase):
    global isColl
    isColl = False  
    def __init__(self, cols):
        vrAEBase.__init__(self)
        self.addLoop()
        print("collisionAnd Start")
        self.cols = cols
        self.setActive(true)
        print("4")
        
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
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
                print("sticker12")
                isColl = False
                distances_instance.loop(False)
                
        print("isColl : " + str(isColl))
                       
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force 3 collid")
    
    
   
#--------------------------------------------------------------
    
   
cdscd = followCube() #loop1

# create some collision objects #
collx = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
colly = vrCollision([constrained_movin_Tumbler1_NS], [cIn])

collxy = CollisionAnd([collx, colly]) #loop2
#collxy.connect("print 'WM-------------------'")

distances_instance = distances(False)

#collxy.connect(distances_class)


'''
vrK = vrKey(Key_R)

elfeo = None
vrK.connect(cdscd.substractLoop())
vrK.connect(distances_instance.substractLoop())
print("collxy type : " + str(type(collxy)) )
vrK.connect(collxy.substractLoop())
'''
