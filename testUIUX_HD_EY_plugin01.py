from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Signal,Slot, QThread,QTimer

importError = False
try:
    import vrController
    import vrFileIO
    import vrMovieExport
    import vrOSGWidget
    import vrScenegraph
    import vrNodePtr
    import vrVariantSets
    import vrVariants
    import time
    import math
    import vrAEBase
    

except ImportError:
    importError = True
    pass

import uiTools

listToLoad = False


vrTOC_form, vrTOC_base = uiTools.loadUiType("temp.ui")

###------------------------------------

class followCube():
    global cTh
    global cIn
    cTh = vrNodeService.findNode("cubeThumb4")
    cIn = vrNodeService.findNode("cubeIndex4")
    
    global constrained_movin_Tumbler1_NS
    constrained_movin_Tumbler1_NS = vrNodeService.findNode("powerbank2")
    
    
    #global rightController
    #rightController = vrDeviceService.getVRDevice("right-controller")
    
    #global RR_thumb_4
    #global RR_index_4
    #RR_thumb_4 = vrNodeService.findNode('R_thumb_4_INT', root=getInternalRootNode())
    #RR_index_4 = vrNodeService.findNode('R_index_4_INT', root=getInternalRootNode())
    
    #global right_Constraint_target
    #right_Constraint_target = None
    
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
        if setL == True and setR == False :
            cTh.setWorldTranslation(LL_thumb_4.getWorldTranslation())
            cIn.setWorldTranslation(LL_index_4.getWorldTranslation())
        elif setL == False and setR == True :
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
        
class distances_obj1():
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

        if setL == True and setR == False :
            self.left_Constraint_target = vrConstraintService.createParentConstraint([leftController.getNode()], constrained_movin_Tumbler1_NS, True)
        elif setL == False and setR == True :
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
        #print("dis_standard2 : " + str(dis_standard2))
        return dis_standard2
        
    
    def loop(self, isColl_Argu):
        #print("(isColl_Argu : " + str(isColl_Argu))
        if isColl_Argu == True :
            self.ConstOn_Th_In()
            #print("ConstOn_Th_In")
            self.dis_measure2()
            #print("dis_standard_True : " + str(dis_standard))
            #print("dis_standard2_True : " + str(dis_standard2))
            #print("dis_standard_check_True : " + str(dis_standard_check))
            if dis_standard_check == True and dis_standard < dis_standard2:
                self.ConstOff_Th_In()
            
        elif isColl_Argu == False :
            #print("ConstOff_Th_In_if1")
            self.dis_measure2()
            #print("dis_standard_False : " + str(dis_standard))
            #print("dis_standard2_False : " + str(dis_standard2))
            #print("dis_standard_check_False : " + str(dis_standard_check))
            if dis_standard_check == True and dis_standard < dis_standard2:
                self.ConstOff_Th_In()
                print("ConstOff_Th_In_if2")

    def substractLoop(self):
        self.subLoop()
        print("loop stop by force distance_obj1")
        

class CollisionAnd_obj1():
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
                #print("dis_standard_check----1" + str(dis_standard_check))
                if dis_standard_check == False :
                    cdscd.dis_measure()
                    #print("dis_standard_check----2" + str(dis_standard_check))
                    #print("extract dis_standard " + str(dis_standard))
                distances_instance.loop(True)
            else :
                isColl = False
                #print("dis_standard_check----1-1" + str(dis_standard_check))
                distances_instance.loop(False)

    def substractLoop(self):
        self.subLoop()
        print("loop stop by force 3 collid")

#find collision area, find sorted obj
area1 = findNode("c_area_1")

area_powerbank_Inputed = vrScenegraph.findNode("powerbank2")

def areaStand1():
    area_powerbank_Inputed.setRotation(0,0,180)
    aoi1 = area_powerbank_Inputed.getWorldTranslation()
    area_powerbank_Inputed.setWorldTranslation(aoi1[0], aoi1[1], float(890.0))
    


###------------------------------------------------------------

class vrWindowClass(vrTOC_form, vrTOC_base):
    
    global comboBox_vset_list
    comboBox_vset_list = []
    
    def __init__(self, parent = None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        
        #self.ui_pushbutton_Lefthand.clicked.connect(self.LHand_cc) #버튼 클릭 신호가 감지되면 펑션을 호출
        #self.ui_pushbutton_Righthand.clicked.connect(self.RHand_cc)
        
        #self.vset_select_combo_box1.currentIndexChanged.connect(self.ComboBox1Click) #콤보 박스의 현재 인덱스가 변경되면 펑션을 호출
        
        #self.vset_select_combo_box1_radio_on.toggled.connect(self.radioBox1) #라디오 버튼이 변경될때마다 펑션을 호출
        
        #self.ui_horizontalSlider.valueChanged.connect(self.sensitivity_scale)
        
        self.psbtn_update.clicked.connect(self.update_button)
        
        self.radiobtn_lefthand.toggled.connect(self.radio_Lhand)
        
        self.psbtn_obj_hand_start.clicked.connect(self.obj_hand_start)
        
    def LHandFunction(self) :
        #lhand vset 호출
        vrVariants.selectVariantSet("set_LHand") # 왼손/오른손 변경 버튼
        
        self.ui_pushbutton_Lefthand.setCheckable(True)
        self.ui_pushbutton_Righthand.setCheckable(False)
        
        self.groupBox_2.setEnabled(True) # hand side가 선택되면 다음 단계의 버튼이 활성화됨
    
    def RHandFunction(self) :
        #rhand vset 호출
        vrVariants.selectVariantSet("set_RHand") # 왼손/오른손 변경 버튼
        
        self.ui_pushbutton_Lefthand.setCheckable(False)
        self.ui_pushbutton_Righthand.setCheckable(True)
        
        self.groupBox_2.setEnabled(True)
        
    def LHand_cc(self):
        #self.ui_pushbutton_Lefthand.setStyleSheet("background-color : orange")
        self.ui_pushbutton_Lefthand.setStyleSheet("font: bold 16px")
        self.ui_pushbutton_Righthand.setStyleSheet("background-color : dark gray")
        
    def RHand_cc(self):
        self.ui_pushbutton_Lefthand.setStyleSheet("background-color : dark gray")
        #self.ui_pushbutton_Righthand.setStyleSheet("background-color : orange")
        self.ui_pushbutton_Righthand.setStyleSheet("font: bold 16px")
        
    def loadFunction(self) :
        self.vset_select_combo_box1.clear() #초기화
        #self.vset_select_combo_box2.clear()
        global comboBox_vset_list
        comboBox_vset_list = [] #load 버튼을 누를때마다 combobox list를 초기화. 이걸 하지않으면 list가 쌓임.
        
        
        #vrVariants.selectVariantSet("func_creditCard")
        vred_vset_list1 = vrVariantSets.getVariantSets()
        #print(vred_vset_list1)
        
        for element1 in vred_vset_list1 : 
            if "func_" in element1:         
                comboBox_vset_list.append(element1)  
                
        print("comboBox vset list = " + str(comboBox_vset_list))
        
        self.vset_select_combo_box1.addItems(comboBox_vset_list)
        #self.vset_select_combo_box1.setCurrentIndex(0)
        #self.vset_select_combo_box2.addItems(comboBox_vset_list)
        #self.vset_select_combo_box2.setCurrentIndex(1)
        
        self.groupBox_3.setEnabled(True) # load 버튼을 클릭하게 되면 다음 단계가 활성화.
        self.vset_select_combo_box1.setEnabled(True) # combobox 가 비활성화 상태로 유지되는 현상 체크
        self.ui_pushbutton_reset.setEnabled(True)
        
        
    def resetFunction(self) :
        print("reset btn Clicked")
        self.vset_select_combo_box1.clear() #초기화
        #self.vset_select_combo_box2.clear() #초기화
        
        self.vset_select_combo_box1_radio_off.setChecked(True)# radio button 디폴트값인 off로 지정.
        #self.vset_select_combo_box2_radio_off.setChecked(True)
        

        vrVariants.selectVariantSet("vset_reset_btn") #0905 vred의 vset 호출. 여기엔 constraint 삭제, loop 삭제, 사용하지 않는 material 삭제, 모든 오브젝트를 hide.
        
        self.ui_pushbutton_Lefthand.setStyleSheet("background-color : dark gray")
        self.ui_pushbutton_Righthand.setStyleSheet("background-color : dark gray")
        
        self.groupBox_2.setEnabled(False) # 리셋버튼을 누르면 상태를 비활성화.
        self.groupBox_3.setEnabled(False)
        self.ui_pushbutton_reset.setEnabled(False)

    def ComboBox1Click(self) : # combobox 를 클릭해 리스트중 하나를 클릭하면 클릭된 리스트 이름을 비교.
        print("combobox1 clicked")
        if self.vset_select_combo_box1.currentText() == comboBox_vset_list[0] :
            print("create power bank model")
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[1] :
            print("create func_tumbler model")
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[2] :
            print("create func_creditCard model")
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
            
    def radioBox1(self):
        if self.vset_select_combo_box1_radio_on.isChecked() : 
            print("RB1 on checked")
            rightnowOnVset = self.vset_select_combo_box1.currentText()
            print("rightnowOn" + str(rightnowOnVset))
            vrVariants.selectVariantSet("_" + rightnowOnVset[5:] + "_show")# func_objName 에서 slice 후 덧붙여서 vset호출           
        else : 
            print("RB1 off checked")
            rightnowOffVset = self.vset_select_combo_box1.currentText()
            vrVariants.selectVariantSet("_" + rightnowOffVset[5:] + "_hide")
            
            
    def sensitivity_scale(self, val):
        print("sensitivity_scale changed!!")
        print(val)  #slider 로 변경되는 값을 터미널에 출력
        self.slider_label.setText(str(val)) # label 값을 slider bar 값으로 set
        
        thumb_scale = vrScenegraph.findNode("cubeThumb4")
        index_scale = vrScenegraph.findNode("cubeIndex4")
        
        thumb_scale.setScale(val * (1/100), val * (1/100), val * (1/100)) # scale 값 반영
        index_scale.setScale(val * (1/100), val * (1/100), val * (1/100))
        
    def update_button(self) :
        global obj_list
        obj_list = []
        
        self.cbbox_updated.clear() #콤보박스 초기화
        
        goon = vrNodeService.findNode("objFolder") #오브젝트가 모여있는 폴더 찾기
        #찾은 폴더에서 각 노드들의 이름을 가져오기
        
        obj_list = goon.getChildren() #각 노드의 id가 list형태로 들어옴. 이것을 이름으로 가져와야함.
        
        for obj_list_element in obj_list:
            obj_list_element_name = obj_list_element.getName()
            print(obj_list_element_name) # 이름으로 가져오기 성공
            
        self.cbbox_updated.addItems(obj_list_element_name)
        '''
        for ind in range(goon.getChildCount()):
            child = goon.getChild(ind)
            if child.getName() == "9":
                print("detect 9!!")
                '''
                
    def radio_Lhand(self):
        global hand_select
        if self.radiobtn_lefthand.isChecked() :
            print("left")
            hand_select = "left-controller"
        else :
            print("right")
            hand_select = "right-controller"
            
    def obj_hand_start(self):
        print("aa2")
        #follow to finger tip with cube
        cdscd = followCube()

        # create some collision objects
        collx = vrCollision([cTh], [constrained_movin_Tumbler1_NS])
        colly = vrCollision([constrained_movin_Tumbler1_NS], [cIn])

        distances_instance = distances_obj1(False)

        collxy = CollisionAnd_obj1([collx, colly]) 
        #collxy.connect("print 'WM-------------------'")


        #create collision area
        collArea1 = vrCollision([area_powerbank_Inputed], [area1])
        collArea1.connect(areaStand1)
        
        





if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
