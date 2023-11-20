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
    import vrNodeUtils


except ImportError:
    importError = True
    pass

import uiTools

listToLoad = False
vrTOC_form, vrTOC_base = uiTools.loadUiType("010_editVer5.ui")


class vrWindowClass(vrTOC_form, vrTOC_base):
    
    global comboBox_vset_list
    comboBox_vset_list = []
    
    def __init__(self, parent = None) :
        #Setup and connect the plugins UI.
        super(vrWindowClass, self).__init__(parent)
        parent.layout().addWidget(self)
        self.parent = parent
        self.setupUi(self)
        
        self.ui_pushbutton_Lefthand.clicked.connect(self.LHandFunction) 
        self.ui_pushbutton_Righthand.clicked.connect(self.RHandFunction)
        
        self.ui_pushbutton_Lefthand.clicked.connect(self.LHand_cc) 
        self.ui_pushbutton_Righthand.clicked.connect(self.RHand_cc)
        
        self.ui_pushbutton_load.clicked.connect(self.loadFunction)
        self.ui_pushbutton_reset.clicked.connect(self.resetFunction)
        
        self.vset_select_combo_box1.currentIndexChanged.connect(self.ComboBox1Click) 
        
        self.vset_select_combo_box1_radio_on.toggled.connect(self.radioBox1) 
        
        self.ui_horizontalSlider.valueChanged.connect(self.sensitivity_scale)
        
        self.ui_pushbutton_create.clicked.connect(self.createFunction)
        self.transparency_radio_on.toggled.connect(self.trnsRadioBox)
        
    def createFunction(self) :
        if vrNodeService.findNode("cubeIndex4").getName() == "cubeIndex4" and vrNodeService.findNode("cubeThumb4").getName() == "cubeThumb4":
            print("create skip")
        else :
            print("create start")
            temp_cubeI = vrNodeUtils.createSphere(2, 10, 0.5,0.5,0.5)
            temp_cubeI.setName("cubeIndex4")
            
            temp_cubeT = vrNodeUtils.createSphere(2, 10, 0.5,0.5,0.5)
            temp_cubeT.setName("cubeThumb4")
            
    def trnsRadioBox(self) :
        trnsthumb = vrScenegraph.findNode("cubeThumb4")
        trnsindex = vrScenegraph.findNode("cubeIndex4")
        if self.transparency_radio_on.isChecked() :
            vrScenegraph.showNode(trnsthumb)
            vrScenegraph.showNode(trnsindex)
        else :
            vrScenegraph.hideNode(trnsthumb)
            vrScenegraph.hideNode(trnsindex)
        
        
    def LHandFunction(self) :
        #lhand vset 호출
        vrVariants.selectVariantSet("set_LHand")
        
        self.ui_pushbutton_Lefthand.setCheckable(True)
        self.ui_pushbutton_Righthand.setCheckable(False)
        
        self.groupBox_2.setEnabled(True) 
    
    def RHandFunction(self) :
        #rhand vset 호출
        vrVariants.selectVariantSet("set_RHand")
        
        self.ui_pushbutton_Lefthand.setCheckable(False)
        self.ui_pushbutton_Righthand.setCheckable(True)
        
        self.groupBox_2.setEnabled(True)
        
    def LHand_cc(self):
        self.ui_pushbutton_Lefthand.setStyleSheet("font: bold 16px")
        self.ui_pushbutton_Righthand.setStyleSheet("background-color : dark gray")
        
    def RHand_cc(self):
        self.ui_pushbutton_Lefthand.setStyleSheet("background-color : dark gray")
        self.ui_pushbutton_Righthand.setStyleSheet("font: bold 16px")
        
    def loadFunction(self) :
        self.vset_select_combo_box1.clear() 
        global comboBox_vset_list
        comboBox_vset_list = [] 
        vred_vset_list1 = vrVariantSets.getVariantSets()
        
        for element1 in vred_vset_list1 : 
            if "func_" in element1:         
                comboBox_vset_list.append(element1)  
                
        #print("comboBox vset list = " + str(comboBox_vset_list))
        self.vset_select_combo_box1.addItems(comboBox_vset_list)
        
        self.groupBox_3.setEnabled(True) 
        self.vset_select_combo_box1.setEnabled(True) 
        self.ui_pushbutton_reset.setEnabled(True)
        
    def resetFunction(self) :
        print("reset btn Clicked")
        self.vset_select_combo_box1.clear() 
        
        self.vset_select_combo_box1_radio_off.setChecked(True)

        vrVariants.selectVariantSet("vset_reset_btn") 
        
        self.ui_pushbutton_Lefthand.setStyleSheet("background-color : dark gray")
        self.ui_pushbutton_Righthand.setStyleSheet("background-color : dark gray")
        
        self.groupBox_2.setEnabled(False) 
        self.groupBox_3.setEnabled(False)
        self.ui_pushbutton_reset.setEnabled(False)

    def ComboBox1Click(self) : 
        if self.vset_select_combo_box1.currentText() == comboBox_vset_list[0] :
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[1] :
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[2] :
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[3] :
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())
            
        elif self.vset_select_combo_box1.currentText() == comboBox_vset_list[4] :
            vrVariants.selectVariantSet(self.vset_select_combo_box1.currentText())    
            
    def radioBox1(self):
        if self.vset_select_combo_box1_radio_on.isChecked() : 
            print("RB1 on checked")
            rightnowOnVset = self.vset_select_combo_box1.currentText()
            print("rightnowOn" + str(rightnowOnVset))
            vrVariants.selectVariantSet("_" + rightnowOnVset[5:] + "_show")           
        else : 
            print("RB1 off checked")
            rightnowOffVset = self.vset_select_combo_box1.currentText()
            vrVariants.selectVariantSet("_" + rightnowOffVset[5:] + "_hide")
            
            
    def sensitivity_scale(self, val):
        print("sensitivity_scale changed!!")
        print(val)  
        self.slider_label.setText(str(val)) 
        
        thumb_scale = vrScenegraph.findNode("cubeThumb4")
        index_scale = vrScenegraph.findNode("cubeIndex4")
        
        thumb_scale.setScale(val * (1/100), val * (1/100), val * (1/100)) 
        index_scale.setScale(val * (1/100), val * (1/100), val * (1/100))


if not importError:
    viewpointPlugin = vrWindowClass(VREDPluginWidget)
