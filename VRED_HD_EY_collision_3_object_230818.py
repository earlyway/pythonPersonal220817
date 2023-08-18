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
    
    global left_Constraint_target
    left_Constraint_target = None
    
    global dis_standard_check
    dis_standard_check = False
    
    global dis_standard
    dis_standard = 0
    
    global dis_standard2
    dis_standard2 = 0
    
    def __init__(self):
        vrAEBase.__init__(self)
        print("1 followCube")
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
        
    def dis_measure(self): #collision 되었을때, const on 유지 or Off 실행의 기준
        global dis_standard
        dis_standard = 0
        global dis_standard_check
        dis_standard = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        #print("dis_standard : " + str(dis_standard))
        dis_standard_check = True
        print("got the 1")
        return dis_standard
        
    def loop(self):
        self.ffc_distance_Th_In()
        
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force followCube")
        
         
class distances_obj1(vrAEBase):
    def __init__(self, isColl_Argu):
        vrAEBase.__init__(self)
        print("3 distances_obj1")
        self.addLoop()
        self.subLoop()
        self.setActive(True)
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
    def Clear(self):
        amount = vrConstraintService.getConstraints()
        for i in amount:
            vrConstraintService.deleteConstraint(i)
            
    def ConstOn_Th_In(self):
        self.Clear()
        self.left_Constraint_target = vrConstraintService.createParentConstraint([leftController.getNode()], constrained_movin_Tumbler1_NS, True)
        print("4")
        findMat = vrMaterialService.findMaterial("Reflective Plastic")
        getTr = vrdBRDFMaterial.getTransparency(findMat)
        colorVect = QVector3D(0.25, 0.25, 0.25)
        getTr.setSeeThrough(colorVect)
        
    def ConstOff_Th_In(self):
        global dis_standard
        global dis_standard_check
        self.Clear()
        
        dis_standard_check = False
        dis_standard = 0
        print("got the 0")
        
        findMat = vrMaterialService.findMaterial("Reflective Plastic")
        getTr = vrdBRDFMaterial.getTransparency(findMat)
        colorVect = QVector3D(0, 0, 0)
        getTr.setSeeThrough(colorVect)
        
        self.subLoop()
        print("constraintOff and loop stop")
        
    def dis_measure2(self): # 기준이 된 큐브간 거리보다 작으면 const on 유지, 크면 const off 실행
        global dis_standard2
        dis_standard2 = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        print("dis_standard2 : " + str(dis_standard2))
        return dis_standard2
        
    
    def loop(self, isColl_Argu):
        print("(isColl_Argu : " + str(isColl_Argu))
        if isColl_Argu == True :
            self.ConstOn_Th_In()
            print("ConstOn_Th_In")
            self.dis_measure2()
            print("dis_standard_True : " + str(dis_standard))
            print("dis_standard2_True : " + str(dis_standard2))
            print("dis_standard_check_True : " + str(dis_standard_check))
            if dis_standard_check == True and dis_standard < dis_standard2:
                self.ConstOff_Th_In()
            
        elif isColl_Argu == False :
            #self.ConstOff_Th_In()
            print("ConstOff_Th_In_if1")
            self.dis_measure2()
            print("dis_standard_False : " + str(dis_standard))
            print("dis_standard2_False : " + str(dis_standard2))
            print("dis_standard_check_False : " + str(dis_standard_check))
            if dis_standard_check == True and dis_standard < dis_standard2:
                self.ConstOff_Th_In()
                print("ConstOff_Th_In_if2")

    def substractLoop(self):
        self.subLoop()
        #CollisionAnd.substractLoopC()
        print("loop stop by force distance_obj1")
        

class CollisionAnd_obj1(vrAEBase):
    global isColl
    global dis_standard_check
    isColl = False 
    def __init__(self, cols):
        vrAEBase.__init__(self)
        self.addLoop()
        print("collisionAnd_obj1 Start")
        self.cols = cols
        self.setActive(True)
        
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
                print("dis_standard_check----1" + str(dis_standard_check))
                if dis_standard_check == False :
                    cdscd.dis_measure()
                    print("dis_standard_check----2" + str(dis_standard_check))
                    print("extract dis_standard " + str(dis_standard))
                distances_instance.loop(True)
            else :
                isColl = False
                '''
                if dis_standard_check == True:
                    cdscd.dis_measure()
                '''
                print("dis_standard_check----1-1" + str(dis_standard_check))
                distances_instance.loop(False)
                       
    def substractLoop(self):
        self.subLoop()
        print("loop stop by force 3 collid")
        
class Collision_cube_dist_standard(vrAEBase):
    def __init__(self, temp):
        vrAEBase.__init__(self)
        self.temp = temp
        cldk = len(temp)
        
        if dis_standard_check == False :
            cdscd.dis_measure()
        else:
            print("cldk" + str(cldk))
        
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
        
#--------------------------------------------------------------

print("test line-------------------------")
    
#global cdscd
cdscd = followCube() #loop1

# create some collision objects #
collx = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
colly = vrCollision([constrained_movin_Tumbler1_NS], [cIn])

distances_instance = distances_obj1(False)

#collxy_dist_standard = Collision_cube_dist_standard([collx, colly])
collxy = CollisionAnd_obj1([collx, colly]) 
#collxy.connect("print 'WM-------------------'")



#collxy.connect(distances_class)


vrK = vrKey(Key_R)

elfeo = None
vrK.connect(cdscd.substractLoop)
vrK.connect(distances_instance.substractLoop)
print("collxy type : " + str(type(collxy)) )
#vrK.connect(collxy(elfeo).substractLoop)
vrK.connect(collxy.substractLoop)
vrK.connect(distances_instance.ConstOff_Th_In)