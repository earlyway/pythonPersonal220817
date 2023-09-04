import math
#C:\Users\besti\Documents\Autodesk\Vred-15.0\ScriptPlugins
class followCube(vrAEBase):
    global cTh
    global cIn
    cTh = vrNodeService.findNode("cubeThumb4")
    cIn = vrNodeService.findNode("cubeIndex4")
    
    global constrained_movin_Tumbler1_NS
    constrained_movin_Tumbler1_NS = vrNodeService.findNode("powerbank2")
    
    
    global rightController
    rightController = vrDeviceService.getVRDevice("right-controller")
    
    global RR_thumb_4
    global RR_index_4
    RR_thumb_4 = vrNodeService.findNode('R_thumb_4_INT', root=getInternalRootNode())
    RR_index_4 = vrNodeService.findNode('R_index_4_INT', root=getInternalRootNode())
    
    global right_Constraint_target
    right_Constraint_target = None
    
    global dis_standard_check
    dis_standard_check = False
    
    global dis_standard
    dis_standard = 0
    
    global dis_standard2
    dis_standard2 = 0
    
    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()
        
    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        
    def ffc_distance_Th_In(self):
        cTh.setWorldTranslation(RR_thumb_4.getWorldTranslation())
        cIn.setWorldTranslation(RR_index_4.getWorldTranslation())
        
        global c_t_QM
        global c_i_QM
        c_t_QM = vrdNode.getWorldTransform(cTh)
        c_i_QM = vrdNode.getWorldTransform(cIn)
    
        global c_t_QM_Vect
        global c_i_QM_Vect
        c_t_QM_Vect = vrMathService.getTranslation(c_t_QM)
        c_i_QM_Vect = vrMathService.getTranslation(c_i_QM)
        
    def dis_measure(self): #collision 되었을때, const on 유지 or Off 실행의 기준이 되는 dis_standard 를 리턴
        global dis_standard
        dis_standard = 0
        global dis_standard_check
        dis_standard = math.sqrt(
                    (c_t_QM_Vect.x() - c_i_QM_Vect.x())**2 +
                    (c_t_QM_Vect.y() - c_i_QM_Vect.y())**2 +
                    (c_t_QM_Vect.z() - c_i_QM_Vect.z())**2
                    )
        dis_standard_check = True
        return dis_standard
        
    def loop(self):
        self.ffc_distance_Th_In()
        
    def substractLoop(self):
        self.subLoop()
        
         
class distances_obj1(vrAEBase):
    def __init__(self, isColl_Argu):
        vrAEBase.__init__(self)
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
        self.right_Constraint_target = vrConstraintService.createParentConstraint([rightController.getNode()], constrained_movin_Tumbler1_NS, True)
        #change material transparency 0->1
        findMat = vrMaterialService.findMaterial("Material.003")
        getTr = vrdBRDFMaterial.getTransparency(findMat)
        colorVect = QVector3D(0.25, 0.25, 0.25)
        getTr.setSeeThrough(colorVect)
        
    def ConstOff_Th_In(self):
        global dis_standard
        global dis_standard_check
        self.Clear()
        
        dis_standard_check = False
        dis_standard = 0
        #change material transparency 1->0
        findMat = vrMaterialService.findMaterial("Material.003")
        getTr = vrdBRDFMaterial.getTransparency(findMat)
        colorVect = QVector3D(0, 0, 0)
        getTr.setSeeThrough(colorVect)
        
        self.subLoop()
        
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
        print("loop stop by force distance_obj1")
        

class CollisionAnd_obj1(vrAEBase):
    global isColl
    global dis_standard_check
    isColl = False 
    def __init__(self, cols):
        vrAEBase.__init__(self)
        self.addLoop()
        self.cols = cols
        self.setActive(True)
        
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
                print("sticker")
                isColl = True
                #self.callAllConnected()
                print("dis_standard_check----1" + str(dis_standard_check))
                if dis_standard_check == False :
                    cdscd.dis_measure()
                    print("dis_standard_check----2" + str(dis_standard_check))
                    print("extract dis_standard " + str(dis_standard))
                distances_instance.loop(True)
            else :
                isColl = False
                print("dis_standard_check----1-1" + str(dis_standard_check))
                distances_instance.loop(False)

    def substractLoop(self):
        self.subLoop()
        print("loop stop by force 3 collid")
        


#find collision area, find sorted obj
area1 = findNode("c_area_1")

areaObjInputed = vrScenegraph.findNode("powerbank2")
    #위(line 10)에 powerbank2 를 이미 변수선언 했는데 여기서(line 198) 다시 변수 선언을 한 이유는 같은 findNode 라도 상속받는 함수가 다르기 때문이다.
    #위의 powerbank2 는 vrNodeService 라는 함수(python api v2)에서 상속받는 findNode 로 return 타입이 vrdNode 이다.
    #하지만 vrCollision 에 들어가는 타입은 vrNodePtr 타입으로 들어가야하므로 vrdNode 로 return 되는 위(line 10)의 변수값을 사용할 수 없다. 그래서 vrScenegraph 함수(python api v1)를 상속받는 findNode 를 사용한 것이다.
def areaStand1():
    areaObjInputed.setRotation(0,0,180)
    aoi1 = areaObjInputed.getWorldTranslation()
    areaObjInputed.setWorldTranslation(aoi1[0], aoi1[1], float(890.0))
    


#--------------------------------------------------------------
#--------------------------------------------------------------

print("test line-------------------------")
    
#follow to finger tip with cube
cdscd = followCube()

# create some collision objects
collx = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
colly = vrCollision([constrained_movin_Tumbler1_NS], [cIn])

distances_instance = distances_obj1(False)

collxy = CollisionAnd_obj1([collx, colly]) 
#collxy.connect("print 'WM-------------------'")


#create collision area
collArea1 = vrCollision([areaObjInputed], [area1])
collArea1.connect(areaStand1)


#Stop all loop and delete all constraint
vrK = vrKey(Key_R)

vrK.connect(cdscd.substractLoop)
vrK.connect(distances_instance.substractLoop)
vrK.connect(collxy.substractLoop)
vrK.connect(distances_instance.ConstOff_Th_In)