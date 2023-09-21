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
    

except ImportError:
    importError = True
    pass

import uiTools

listToLoad = False


vrTOC_form, vrTOC_base = uiTools.loadUiType("010_editVer3.ui")


class vrWindowClass(vrTOC_form, vrTOC_base):
    
    global comboBox_vset_list
    comboBox_vset_list = []
    
    def __init__(self, parent = None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        
        self.ui_pushbutton_Lefthand.clicked.connect(self.LHandFunction) #버튼이 클릭되면 펑션을 호출
        self.ui_pushbutton_Righthand.clicked.connect(self.RHandFunction)
        
        self.ui_pushbutton_Lefthand.clicked.connect(self.LHand_cc) #버튼 클릭 신호가 감지되면 펑션을 호출
        self.ui_pushbutton_Righthand.clicked.connect(self.RHand_cc)
        
        self.ui_pushbutton_load.clicked.connect(self.loadFunction)
        self.ui_pushbutton_reset.clicked.connect(self.resetFunction)
        
        self.vset_select_combo_box1.currentIndexChanged.connect(self.ComboBox1Click) #콤보 박스의 현재 인덱스가 변경되면 펑션을 호출
        #self.vset_select_combo_box2.currentIndexChanged.connect(self.ComboBox2Click)
        
        self.vset_select_combo_box1_radio_on.toggled.connect(self.radioBox1) #라디오 버튼이 변경될때마다 펑션을 호출
        #self.vset_select_combo_box2_radio_on.toggled.connect(self.radioBox2)
        
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
        
        
        vrVariants.selectVariantSet("func_creditCard")
        vred_vset_list1 = vrVariantSets.getVariantSets()
        print(vred_vset_list1)
        
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
            
            
    def ComboBox2Click(self) :
        print("combobox2 clicked")
        
        if self.vset_select_combo_box2.currentText() == comboBox_vset_list[0] :
            print("create power bank model")
            vrVariants.selectVariantSet(self.vset_select_combo_box2.currentText())
            
        elif self.vset_select_combo_box2.currentText() == comboBox_vset_list[1] :
            print("create func_tumbler model")
            vrVariants.selectVariantSet(self.vset_select_combo_box2.currentText())
            
        elif self.vset_select_combo_box2.currentText() == comboBox_vset_list[2] :
            print("create func_creditCard model")
            vrVariants.selectVariantSet(self.vset_select_combo_box2.currentText())
            
            
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
            
        
    def radioBox2(self):
        if self.vset_select_combo_box2_radio_on.isChecked() : 
            print("RB2 on checked")
            rightnowOnVset2 = self.vset_select_combo_box2.currentText()
            print(rightnowOnVset2[5:])
            vrVariants.selectVariantSet("_" + rightnowOnVset2[5:] + "_show")
        else:
            print("RB2 off checked")
            rightnowOffVset2 = self.vset_select_combo_box2.currentText() #0911
            print(rightnowOffVset2[5:])
            vrVariants.selectVariantSet("_" + rightnowOffVset2[5:] + "_hide")


if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
