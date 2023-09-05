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


vrTOC_form, vrTOC_base = uiTools.loadUiType("010.ui")


class vrWindowClass(vrTOC_form, vrTOC_base):
    
    global comboBox_vset_list
    comboBox_vset_list = []
    
    def __init__(self, parent=None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        
        self.ui_pushbutton_load.clicked.connect(self.loadFunction) 
        self.ui_pushbutton_reset.clicked.connect(self.resetFunction)
        
        self.vset_select_combo_box1.currentIndexChanged.connect(self.ComboBox1Click)
        self.vset_select_combo_box2.currentIndexChanged.connect(self.ComboBox2Click)
        
        self.vset_select_combo_box1_radio_on.toggled.connect(self.radioBox1)
        self.vset_select_combo_box2_radio_on.toggled.connect(self.radioBox2)


    def loadFunction(self) :
        self.vset_select_combo_box1.clear() #초기화
        self.vset_select_combo_box2.clear() #초기화
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
        self.vset_select_combo_box2.addItems(comboBox_vset_list)
        #self.vset_select_combo_box1.setCurrentIndex(0) #0905
        self.vset_select_combo_box2.setCurrentIndex(1)
        
        
    def resetFunction(self) :
        print("reset btn Clicked")
        self.vset_select_combo_box1.clear() #초기화
        self.vset_select_combo_box2.clear() #초기화
        
        self.vset_select_combo_box1_radio_off.checked() #0905 radio button 디폴트값인 off로 지정.
        self.vset_select_combo_box2_radio_off.checked()
        
        pb2 = vrNodePtr.findNode("powerbank2") #0905 오브젝트를 특정위치로 리셋
        pb2.setWorldTranslation(1250, 1575, 1200)#0905
        pb2.setRotation(0,0,-180)#0905
        
        tbr = vrNodePtr.findNode("moving_Tumbler1")
        tbr.setWorldTranslation(1340, 1600, 1000)
        tbr.setRotation(0,0,0)
        
        ccb = vrNodePtr.findNode("credit_card_blue")
        ccb.setWorldTranslation(1500, 1650, 1000)
        ccb.setRotation(0,0,-180)

        vrVariants.selectVariantSet("vset_reset_btn") #0905 vred의 vset 호출. 여기엔 constraint 삭제, loop 삭제, 사용하지 않는 material 삭제, 모든 오브젝트를 hide.
        

    def ComboBox1Click(self) : # combobox 를 클릭해 리스트중 하나를 클릭하면 클릭된 리스트 이름을 비교.
        print("combobox1 clicked")
        if self.vset_select_combo_box1.currentText() == comboBox_vset_list[0] :
            print("create power bank model")
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[1] :
            print("create func_tumbler model")
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[2] :
            print("create func_creditCard model")
            
            
    def ComboBox2Click(self) :
        print("combobox2 clicked")
        
        if self.vset_select_combo_box2.currentText() == comboBox_vset_list[0] :
            print("create power bank model")
            
        elif self.vset_select_combo_box2.currentText() == comboBox_vset_list[1] :
            print("create func_tumbler model")
            
        elif self.vset_select_combo_box2.currentText() == comboBox_vset_list[2] :
            print("create func_creditCard model")
            
            
    def radioBox1(self):
        if self.vset_select_combo_box1_radio_on.isChecked() : 
            print("RB1 on checked")
            
            rightnowOnVset = self.vset_select_combo_box1.currentText()
            print("rightnowOn" + str(rightnowOnVset))
            testA = vrVariants.selectVariantSet("_" + rightnowOnVset + "show")#0905 여기가 작동하지 않는중.. testA print를 하면 None 값이 출력되는 상황.
            print(testA)
            
        else : 
            print("RB1 off checked")
            
            rightnowOffVset = self.vset_select_combo_box1.currentText()
            testB = vrVariants.selectVariantSet("_" + rightnowOffVset + "hide")#0905
            print(testB)
        
    def radioBox2(self):
        if self.vset_select_combo_box2_radio_on.isChecked() : 
            print("RB2 on checked")
            
            rightnowOnVset2 = self.vset_select_combo_box2.currentText()
            vrVariants.selectVariantSet("_" + rightnowOnVset2 + "show")#0905
        elif self.vset_select_combo_box2_radio_off.isChecked() : 
            print("RB2 off checked")
            
            rightnowOffVset2 = self.vset_select_combo_box1.currentText()
            vrVariants.selectVariantSet("_" + rightnowOffVset2 + "hide")#0905


if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
